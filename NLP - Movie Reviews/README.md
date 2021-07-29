# Classifying text sentiment of IMDb movie reviews

## Table of contents
* [General info](#general-info)
* [Data source](#data-source)
* [Technologies used](#technologies-used)
* [Methods used](#methods-used)
* [Code example](#code-example)
* [Screenshots from analysis](#screenshots-from-analysis)
* [Contact](#contact)

## General info
> This project uses text sentiment analysis to determine the connotation of 50K+ moview reviews and 160K phrases by demonstrating an understanding of classification and by developing a series of feature sets for the data and applying a classifier to understand the accuracy. Finally, cross-validation is applied to obtain tighter results through precision, recall, and F1 variables. 

## Data source
Sourced from: https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews\
The dataset contains 156,060 phrases with a sentiment assigned to each, ranging from 0 to 4. This range represents negative, somewhat negative, neutral, somewhat positive, and positive sentiments, meaning a higher value digit denoting a more positive sentiment.

## Technologies used
* Anaconda (python)

## Methods used
* NLP/NLTK
* Feature set text classifiers
* Feature functions: Bag of words, bigram features, and POS features
* Cross-validation to turn precision, recall, and F1 variables

## Code example
**DEFINRE THE FEATURE FUNCTIONS**\
#1. Bag of words: define a feature function of a corpus to track true/false if keyword is in the corpus\
#define features (keywords) of a document for a BOW/unigram baseline\
#each feature is 'contains(keyword)' and is true or false depending\
#on whether that keyword is in the document\
def phrase_features(phrase, word_features):\
    phrase_words = set(phrase)\
    features = {}\
    for word in word_features:\
        features['V_{}'.format(word)] = (word in phrase_words)\
    return features\
\
#2. Bigram Features\
#define features that include words as before \
#add the most frequent significant bigrams\
#this function takes the list of words in a document as an argument and returns a feature dictionary\
#it depends on the variables word_features and bigram_features\
def bigram_document_features(document, word_features, bigram_features):\
    document_words = set(document)\
    document_bigrams = nltk.bigrams(document)\
    features = {}\
    for word in word_features:\
        features['V_{}'.format(word)] = (word in document_words)\
    for bigram in bigram_features:\
        features['B_{}_{}'.format(bigram[0], bigram[1])] = (bigram in document_bigrams)  \  
    return features\
\
#3. POS Features\
#this function takes a document list of words and returns a feature dictionary\
#it runs the default pos tagger (the Stanford tagger) on the document\
#and counts 4 types of pos tags to use as features\
def POS_features(document, word_features):\
    document_words = set(document)\
    tagged_words = nltk.pos_tag(document)\
    features = {}\
    for word in word_features:\
        features['contains({})'.format(word)] = (word in document_words)\
    numNoun = 0\
    numVerb = 0\
    numAdj = 0\
    numAdverb = 0\
    for (word, tag) in tagged_words:\
        if tag.startswith('N'): numNoun += 1\
        if tag.startswith('V'): numVerb += 1\
        if tag.startswith('J'): numAdj += 1\
        if tag.startswith('R'): numAdverb += 1\
    features['nouns'] = numNoun\
    features['verbs'] = numVerb\
    features['adjectives'] = numAdj\
    features['adverbs'] = numAdverb\
    return features\
.\
.\
.\
**APPLY BOW FEATURE FUNCTION**\
 #1. Bag of words feature sets\
  print('Bag of words analysis')\
  phrase_list = [word for (sent,cat) in phrasedocs for word in sent] # create an organized list containing the phrase (sent) and it's sentiment (cat)\
  BagOfWords = nltk.FreqDist(phrase_list) # create a freq dist from the list\
  BoW_items = BagOfWords.most_common(1500) # find most common words\
  BoW_features = [word for (word, freq) in BoW_items] # define features from the most common words\
  BoWfeaturesets = [(phrase_features(d, BoW_features), c) for (d, c) in phrasedocs] # create a feature set from the features of most common words\
#print(BoWfeaturesets[10])\
\
  #train BoW classifier\
  #Bag of words: NB Classifer\
  BoW_train_set, BoW_test_set = BoWfeaturesets[1000:], BoWfeaturesets[:1000] # create train and test data sets (67% by 33%)\
  BoWclassifier = nltk.NaiveBayesClassifier.train(BoW_train_set) # build the classifier\
#print('Classifer:', BoWclassifier)\
  print('Bag of Words classifier accuracy: ', nltk.classify.accuracy(BoWclassifier, BoW_test_set)) # check the accuracy\
  print(BoWclassifier.show_most_informative_features(30)) # show most informative features\
\
  #Cross-validation: Precision, recall, and F1\
  word_list = [n for (p,n) in phrasedocs]  # n for score, p for phrase\
  labels = list(set(word_list))    # gets only unique labels\
  num_folds = 5\
  cross_validation_PRF(num_folds, BoWfeaturesets, labels) # cross validation accuracy to obtain precision\
  print()\


## Screenshots from analysis
Data accuracy results for the original, processed (ex: stop words removed) data
![image](https://user-images.githubusercontent.com/75768214/127576656-276f0d72-ef01-4468-b12c-b22b7d53e22f.png)
\
\
**Increasing accuracy using negation feature function**\
Train & test the model:\
![image](https://user-images.githubusercontent.com/75768214/127576737-7504f5ef-37a7-47fb-8bcc-fb98637bb21c.png)
\
\
Apply negation features with unigram feature sets
![image](https://user-images.githubusercontent.com/75768214/127576785-5123ea15-c422-4f4d-9a29-d8fd6dbf34cf.png)


## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
