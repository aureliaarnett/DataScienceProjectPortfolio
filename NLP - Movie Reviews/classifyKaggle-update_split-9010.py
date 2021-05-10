# Aurelia Arnett & Teja Sanaka
# Updating Train/Test split to 90/10
# Applying new change to the bag of words feature sets

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


# FEATURE FUNCTIONS HERE
# Bag of words: define a feature function of a corpus to track true/false if keyword is in the corpus
# define features (keywords) of a document for a BOW/unigram baseline
# each feature is 'contains(keyword)' and is true or false depending
# on whether that keyword is in the document
def phrase_features(phrase, word_features):
    phrase_words = set(phrase)
    features = {}
    for word in word_features:
        features['V_{}'.format(word)] = (word in phrase_words)
    return features

# POS Features
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



# use NLTK to compute evaluation measures from a reflist of gold labels
#    and a testlist of predicted labels for all labels in a list
# returns lists of precision and recall for each label



# function to read kaggle training file, train and test a classifier 
def processkaggle(dirPath,limitStr):
  # convert the limit argument from a string to an int
  limit = int(limitStr)
  
  os.chdir(dirPath)

  nltkstopwords = nltk.corpus.stopwords.words('english') # import stop words

  f = open('./train.tsv', 'r')
  # loop over lines in the file and use the first limit of them
  phrasedata = []
  for line in f:
    # ignore the first line starting with Phrase and read all lines
    if (not line.startswith('Phrase')):
      # remove final end of line character
      line = line.strip()
      # Pre-processing: re-attaching 's contraction words separated by a space
      line = line.replace(" '", "")      # ex. It 's
      # Pre-processing: re-attaching n't contraction words separated by a space
      line = line.replace(" n't", "n't") # ex. Is n't
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
    # Pre-processing: tokens to lowercase
    tokens = [w.lower() for w in tokens]
    # Pre-processing: removing nltk stopwords
    tokens = [w for w in tokens if not w in nltkstopwords]
    phrasedocs.append((tokens, int(phrase[1])))

  # print a few
  for phrase in phrasedocs[:10]:
    print(phrase)

  # Address polarity of the phrases 
  phrasedocs = [(sent, cat) for cat in sentence_polarity.categories() 
    for sent in sentence_polarity.sents(categories=cat)]

  print()

  # Bag of words feature sets
  print('Bag of words analysis - 90/10 Split')
  phrase_list = [word for (sent,cat) in phrasedocs for word in sent] # create an organized list containing the phrase (sent) and it's sentiment (cat)
  BagOfWords = nltk.FreqDist(phrase_list) # create a freq dist from the list
  BoW_items = BagOfWords.most_common(1500) # find most common words
  BoW_features = [word for (word, freq) in BoW_items] # define features from the most common words
  BoWfeaturesets = [(phrase_features(d, BoW_features), c) for (d, c) in phrasedocs] # create a feature set from the features of most common words

  # train BoW classifier with NB
  BoW_train_set, BoW_test_set = BoWfeaturesets[1350:], BoWfeaturesets[:1350] # create train and test data sets (90% by 10%)
  BoWclassifier = nltk.NaiveBayesClassifier.train(BoW_train_set) # build the classifier
  print('Bag of Words classifier accuracy: ', nltk.classify.accuracy(BoWclassifier, BoW_test_set)) # check the accuracy
  print()

  print('POS analysis - 90/10 Split')
  POS_featuresets = [(POS_features(d, BoW_features), c) for (d, c) in phrasedocs]
  # train POS classifier
  # train a classifier and report accuracy
  POS_train_set, POS_test_set = POS_featuresets[1350:], POS_featuresets[:1350]
  POSclassifier = nltk.NaiveBayesClassifier.train(POS_train_set)
  print('POS classifier accuracy: ', nltk.classify.accuracy(POSclassifier, POS_test_set))


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
