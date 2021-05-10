# Aurelia Arnett & Teja Sanaka
# Unrocessed Data File -- Experiment 1; comparing the accuracy of the unprocessed data to the processed data


'''
  This program shell reads phrase data for the kaggle phrase sentiment classification problem.
  The input to the program is the path to the kaggle directory "corpus" and a limit number.
  The program reads all of the kaggle phrases, and then picks a random selection of the limit number.
  It creates a "phrasedocs" variable with a list of phrases consisting of a pair
    with the list of tokenized words from the phrase and the label number from 1 to 4
  It prints a few example phrases.
  In comments, it is shown how to get word lists from the two sentiment lexicons:
      subjectivity and LIWC, if you want to use them in your features
  Your task is to generate features sets and train and test a classifier.

  Usage:  python classifyKaggle.py  <corpus directory path> <limit number>
'''
# open python and nltk packages needed for processing
import os
import sys
import random
import nltk
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk.probability import FreqDist, DictionaryProbDist, ELEProbDist, sum_logs
from nltk.corpus import sentence_polarity

# Adding bigram features:
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()

# Adding trigram features:
# from nltk.collocations import TrigramCollocationFinder # Already imported above
trigram_measures = nltk.collocations.TrigramAssocMeasures()


######## Experiment Options ######## 
#import sentiment_read_subjectivity
# initialize the positive, neutral and negative word lists
#(positivelist, neutrallist, negativelist) = sentiment_read_subjectivity.read_three_types('SentimentLexicons/subjclueslen1-HLTEMNLP05.tff')

#import sentiment_read_LIWC_pos_neg_words
# initialize positve and negative word prefix lists from LIWC 
#   note there is another function isPresent to test if a word's prefix is in the list
#(poslist, neglist) = sentiment_read_LIWC_pos_neg_words.read_words()

# FEATURE FUNCTIONS HERE
# 1. Bag of words: define a feature function of a corpus to track true/false if keyword is in the corpus
# define features (keywords) of a document for a BOW/unigram baseline
# each feature is 'contains(keyword)' and is true or false depending
# on whether that keyword is in the document
def phrase_features(phrase, word_features):
    phrase_words = set(phrase)
    features = {}
    for word in word_features:
        features['V_{}'.format(word)] = (word in phrase_words)
    return features

# 2. Bigram Features
# define features that include words as before 
# add the most frequent significant bigrams
# this function takes the list of words in a document as an argument and returns a feature dictionary
# it depends on the variables word_features and bigram_features
def bigram_document_features(document, word_features, bigram_features):
    document_words = set(document)
    document_bigrams = nltk.bigrams(document)
    features = {}
    for word in word_features:
        features['V_{}'.format(word)] = (word in document_words)
    for bigram in bigram_features:
        features['B_{}_{}'.format(bigram[0], bigram[1])] = (bigram in document_bigrams)    
    return features

# 3. POS Features
# this function takes a document list of words and returns a feature dictionary
# it runs the default pos tagger (the Stanford tagger) on the document
#   and counts 4 types of pos tags to use as features
def POS_features(document, word_features):
    document_words = set(document)
    tagged_words = nltk.pos_tag(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    numNoun = 0
    numVerb = 0
    numAdj = 0
    numAdverb = 0
    for (word, tag) in tagged_words:
        if tag.startswith('N'): numNoun += 1
        if tag.startswith('V'): numVerb += 1
        if tag.startswith('J'): numAdj += 1
        if tag.startswith('R'): numAdverb += 1
    features['nouns'] = numNoun
    features['verbs'] = numVerb
    features['adjectives'] = numAdj
    features['adverbs'] = numAdverb
    return features

## cross-validation ##
# this function takes the number of folds, the feature sets and the labels
# it iterates over the folds, using different sections for training and testing in turn
#   it prints the performance for each fold and the average performance at the end
def cross_validation_PRF(num_folds, featuresets, labels):
    subset_size = int(len(featuresets)/num_folds)
    print('Each fold size:', subset_size)
    # for the number of labels - start the totals lists with zeroes
    num_labels = len(labels)
    total_precision_list = [0] * num_labels
    total_recall_list = [0] * num_labels
    total_F1_list = [0] * num_labels

    # iterate over the folds
    for i in range(num_folds):
        test_this_round = featuresets[(i*subset_size):][:subset_size]
        train_this_round = featuresets[:(i*subset_size)] + featuresets[((i+1)*subset_size):]
        # train using train_this_round
        classifier = nltk.NaiveBayesClassifier.train(train_this_round)
        # evaluate against test_this_round to produce the gold and predicted labels
        goldlist = []
        predictedlist = []
        for (features, label) in test_this_round:
            goldlist.append(label)
            predictedlist.append(classifier.classify(features))

        # computes evaluation measures for this fold and
        #   returns list of measures for each label
        print('Fold', i)
        (precision_list, recall_list, F1_list) \
                  = eval_measures(goldlist, predictedlist, labels)
        
        print('\tPrecision\tRecall\t\tF1')
        # print measures for each label
        for i, lab in enumerate(labels):
            print(lab, '\t', "{:10.3f}".format(precision_list[i]), \
              "{:10.3f}".format(recall_list[i]), "{:10.3f}".format(F1_list[i]))
        
        # for each label add to the sums in the total lists
        for i in range(num_labels):
            # for each label, add the 3 measures to the 3 lists of totals
            total_precision_list[i] += precision_list[i]
            total_recall_list[i] += recall_list[i]
            total_F1_list[i] += F1_list[i]

    # find precision, recall and F measure averaged over all rounds for all labels
    # compute averages from the totals lists
    precision_list = [tot/num_folds for tot in total_precision_list]
    recall_list = [tot/num_folds for tot in total_recall_list]
    F1_list = [tot/num_folds for tot in total_F1_list]
    # the evaluation measures in a table with one row per label
    print('\nAverage Precision\tRecall\t\tF1 \tPer Label')
    # print measures for each label
    for i, lab in enumerate(labels):
        print(lab, '\t', "{:10.3f}".format(precision_list[i]), \
          "{:10.3f}".format(recall_list[i]), "{:10.3f}".format(F1_list[i]))
    
    # print macro average over all labels - treats each label equally
    print('\nMacro Average Precision\tRecall\t\tF1 \tOver All Labels')
    print('\t', "{:10.3f}".format(sum(precision_list)/num_labels), \
          "{:10.3f}".format(sum(recall_list)/num_labels), \
          "{:10.3f}".format(sum(F1_list)/num_labels))

    # for micro averaging, weight the scores for each label by the number of items
    #    this is better for labels with imbalance
    # first intialize a dictionary for label counts and then count them
    label_counts = {}
    for lab in labels:
      label_counts[lab] = 0 
    # count the labels
    for (doc, lab) in featuresets:
      label_counts[lab] += 1
    # make weights compared to the number of documents in featuresets
    num_docs = len(featuresets)
    label_weights = [(label_counts[lab] / num_docs) for lab in labels]
    print('\nLabel Counts', label_counts)
    #print('Label weights', label_weights)
    # print macro average over all labels
    print('Micro Average Precision\tRecall\t\tF1 \tOver All Labels')
    precision = sum([a * b for a,b in zip(precision_list, label_weights)])
    recall = sum([a * b for a,b in zip(recall_list, label_weights)])
    F1 = sum([a * b for a,b in zip(F1_list, label_weights)])
    print( '\t', "{:10.3f}".format(precision), \
      "{:10.3f}".format(recall), "{:10.3f}".format(F1))

## Precision, recall, F1 ##
# Function to compute precision, recall and F1 for each label
#  and for any number of labels
# Input: list of gold labels, list of predicted labels (in same order)
# Output: returns lists of precision, recall and F1 for each label
#      (for computing averages across folds and labels)
def eval_measures(gold, predicted, labels):
    
    # these lists have values for each label 
    recall_list = []
    precision_list = []
    F1_list = []

    for lab in labels:
        # for each label, compare gold and predicted lists and compute values
        TP = FP = FN = TN = 0
        for i, val in enumerate(gold):
            if val == lab and predicted[i] == lab:  TP += 1
            if val == lab and predicted[i] != lab:  FN += 1
            if val != lab and predicted[i] == lab:  FP += 1
            if val != lab and predicted[i] != lab:  TN += 1
        # use these to compute recall, precision, F1
        # for small numbers, guard against dividing by zero in computing measures
        if (TP == 0) or (FP == 0) or (FN == 0):
          recall_list.append (0)
          precision_list.append (0)
          F1_list.append(0)
        else:
          recall = TP / (TP + FP)
          precision = TP / (TP + FN)
          recall_list.append(recall)
          precision_list.append(precision)
          F1_list.append( 2 * (recall * precision) / (recall + precision))

    # the evaluation measures in a table with one row per label
    return (precision_list, recall_list, F1_list)


#import sentiment_read_subjectivity
# initialize the positive, neutral and negative word lists
#(positivelist, neutrallist, negativelist) = sentiment_read_subjectivity.read_three_types('SentimentLexicons/subjclueslen1-HLTEMNLP05.tff')

#import sentiment_read_LIWC_pos_neg_words
# initialize positve and negative word prefix lists from LIWC 
#   note there is another function isPresent to test if a word's prefix is in the list
#(poslist, neglist) = sentiment_read_LIWC_pos_neg_words.read_words()

# define a feature definition function here

# use NLTK to compute evaluation measures from a reflist of gold labels
#    and a testlist of predicted labels for all labels in a list
# returns lists of precision and recall for each label


# function to read kaggle training file, train and test a classifier 
def processkaggle(dirPath,limitStr):
  # convert the limit argument from a string to an int
  limit = int(limitStr)
  
  os.chdir(dirPath)
  
  f = open('./train.tsv', 'r')
  # loop over lines in the file and use the first limit of them
  phrasedata = []
  for line in f:
    # ignore the first line starting with Phrase and read all lines
    if (not line.startswith('Phrase')):
      # remove final end of line character
      line = line.strip()
      # each line has 4 items separated by tabs
      # ignore the phrase and sentence ids, and keep the phrase and sentiment
      phrasedata.append(line.split('\t')[2:4])
  
  
  # pick a random sample of length limit because of phrase overlapping sequences
  random.shuffle(phrasedata)
  phraselist = phrasedata[:limit]

  print('Read', len(phrasedata), 'phrases, using', len(phraselist), 'random phrases')

  for phrase in phraselist[:10]:
    print (phrase)
  
  # create list of phrase documents as (list of words, label)
  phrasedocs = []
  # add all the phrases
  for phrase in phraselist:
    tokens = nltk.word_tokenize(phrase[0])
    phrasedocs.append((tokens, int(phrase[1])))
  
  # print a few
  for phrase in phrasedocs[:10]:
    print (phrase)

  # Address polarity of the phrases 
  phrasedocs = [(sent, cat) for cat in sentence_polarity.categories() 
    for sent in sentence_polarity.sents(categories=cat)]

  # 1. Bag of words feature sets
  print('Bag of words analysis')
  phrase_list = [word for (sent,cat) in phrasedocs for word in sent] # create an organized list containing the phrase (sent) and it's sentiment (cat)
  BagOfWords = nltk.FreqDist(phrase_list) # create a freq dist from the list
  BoW_items = BagOfWords.most_common(1500) # find most common words
  BoW_features = [word for (word, freq) in BoW_items] # define features from the most common words
  BoWfeaturesets = [(phrase_features(d, BoW_features), c) for (d, c) in phrasedocs] # create a feature set from the features of most common words


  # train BoW classifier
  # 1. Bag of words: NB Classifer
  BoW_train_set, BoW_test_set = BoWfeaturesets[1000:], BoWfeaturesets[:1000] # create train and test data sets (67% by 33%)
  BoWclassifier = nltk.NaiveBayesClassifier.train(BoW_train_set) # build the classifier

  print('Bag of Words classifier accuracy: ', nltk.classify.accuracy(BoWclassifier, BoW_test_set)) # check the accuracy
#  print(BoWclassifier.show_most_informative_features(30)) # show most informative features

  # Cross-validation: Precision, recall, and F1
  word_list = [n for (p,n) in phrasedocs]  # n for score, p for phrase
  labels = list(set(word_list))    # gets only unique labels
  num_folds = 5
  cross_validation_PRF(num_folds, BoWfeaturesets, labels) # cross validation accuracy to obtain precision
  print()


  # 2. Bigram Feature Sets
  print('Bigram analysis')
  bigramFinder = BigramCollocationFinder.from_words(phrase_list) # Create bigram finder on all the words in the sequence
  bigram_features = bigramFinder.nbest(bigram_measures.chi_sq, 500) # Using Chi Sq instead of freq dist
  # create feature sets for all sentences
  bigram_featuresets = [(bigram_document_features(d, BoW_features, bigram_features), c) for (d, c) in phrasedocs]

  # train bigram classifier
  # train a classifier and report accuracy
  bigram_train_set, bigram_test_set = bigram_featuresets[1000:], bigram_featuresets[:1000]
  bigramClassifier = nltk.NaiveBayesClassifier.train(bigram_train_set)
  print('Bigram classifier accuracy: ', nltk.classify.accuracy(bigramClassifier, bigram_test_set))

  # Cross-validation: Precision, recall, and F1
  cross_validation_PRF(num_folds, bigram_featuresets, labels) # cross validation accuracy to obtain precision
  print()
  

  # 3. POS Feature Sets
  print('POS analysis')
  POS_featuresets = [(POS_features(d, BoW_features), c) for (d, c) in phrasedocs]

  # train POS classifier
  # train a classifier and report accuracy
  POS_train_set, POS_test_set = POS_featuresets[1000:], POS_featuresets[:1000]
  POSclassifier = nltk.NaiveBayesClassifier.train(POS_train_set)
  print('POS classifier accuracy: ', nltk.classify.accuracy(POSclassifier, POS_test_set))

  # Cross-validation: Precision, recall, and F1
  cross_validation_PRF(num_folds, POS_featuresets, labels) # cross validation accuracy to obtain precision
  print()





"""
commandline interface takes a directory name with kaggle subdirectory for train.tsv
   and a limit to the number of kaggle phrases to use
It then processes the files and trains a kaggle movie review sentiment classifier.

"""
if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print ('usage: classifyKaggle.py <corpus-dir> <limit>')
        sys.exit(0)
    processkaggle(sys.argv[1], sys.argv[2])
