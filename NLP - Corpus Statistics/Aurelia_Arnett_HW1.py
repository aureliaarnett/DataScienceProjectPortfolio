# Aurelia Arnett
# IST 664 - NLP
# Homework Assignment 1: Comparing Corpora with Corpus Statistics
# Purpose: To run word frequencies, bigram grequencies, and mutual information scores on the documents;
# Then select items from these lists to make a comparison between the two documents

import nltk
# nltk.download()
# from nltk.book import * # needed if importing from the nltk.book package

### Part 1: Pick two documents ###
#bring in the Gutenberg project
nltk.corpus.gutenberg.fileids() 

# Document 1: 'carroll-alice.txt', which is doc 7 in the Gutenberg project
aliceTxt = nltk.corpus.gutenberg.fileids()[7] # Store the Alice book in a callable term
print('Document 1:', aliceTxt)                # Confirm you've selected the right book

# Document 2: 'shakespeare-caesar.txt', which is doc 14 in the Gutenberg project

caesarTxt = nltk.corpus.gutenberg.fileids()[14]  # Store the Moby Dick book in a callable term (Gutenberg project)
print('Document 2:', caesarTxt)                  # Confirm you've selected the right book
print()




### Part 2: Examine text in the documents & decide how to process words ###
# Pre-processing:

# Alice Document
aliceTxt = nltk.corpus.gutenberg.raw(aliceTxt)       # Extract raw text to examine how words may be written: Ex. "Alice's" has an appostrophe we wouldn't want to lose
aliceTxt = aliceTxt.replace("'", "")                 # Remove apostrophes that would separate one word into 3 tokens: Ex. Alice's would be tokenized to Alice, ', and s
#print(aliceTxt[:100])                               # Confirm removal of apostrophes
aliceWords = nltk.word_tokenize(aliceTxt)            # Now we can tokenize the Alice txt file
#print('Preview Text:', aliceWords[:100])            # Initial preview of tokens
#print()
aliceWords = [w.lower() for w in aliceWords]         # All tokens to lower case
#print('Confirm Lower Case:', aliceWords[:100])      # Confirm tokens are lower case
#print()
## Note: It can be seen that there are many non-alphabetical tokens! Let's remove to focus on alphabetic English words only

# Define a function to remove non-alphabetic tokens:
import re
def alpha_filter(w):
  pattern = re.compile('^[^a-z]+$')   # Regular Expression pattern to match word of non-alphabetical characters
  if (pattern.match(w)):
    return True
  else:
    return False

aliceWords = [w for w in aliceWords if not alpha_filter(w)]  
#print(aliceWords[:100])
## Note: Now we see words that add very little value such as 'of'. Let's remove stop words!

nltkstopwords = nltk.corpus.stopwords.words('english')         # import stop words
aliceWords = [w for w in aliceWords if not w in nltkstopwords] # Remove stop words
#print(aliceWords[:100])
# The Alice book is ready for analysis!


# Caesar Document
# It is safe to assume that a lot of the observations found in the un-processed Alice text will occur in the Caesar text
# Let's repeat the same cleansing
caesarTxt = nltk.corpus.gutenberg.raw(caesarTxt)       # Extract raw text to examine how words may be written
caesarTxt = caesarTxt.replace("'", "")                 # Remove apostrophes that would separate one word into 3 tokens
#print(caesarTxt[:100])                                # Confirm removal of apostrophes
caesarWords = nltk.word_tokenize(caesarTxt)            # Now we can tokenize the Caesar txt file
#print('Preview Text:', caesarWords[:100])             # Initial preview of tokens
#print()
caesarWords = [w.lower() for w in caesarWords]         # All tokens to lower case
#print('Confirm Lower Case:', caesarWords[:100])       # Confirm tokens are lower case
#print()
caesarWords = [w for w in caesarWords if not alpha_filter(w)]  # Remove non-alphabetic characters
#print(caesarWords[:100])
caesarWords = [w for w in caesarWords if not w in nltkstopwords] # Remove stop words
#print(caesarWords[:100])
# The Caesar book is ready for analysis!



# 2.a: List the top 50 words by frequency (normalized by the length of the document)
from nltk import FreqDist

# Alice Document
print('Alice Book - Top 50 words by frequency:')
aliceDist = FreqDist(aliceWords)      # Create a frequency distribution of the words in the Alice pre-processed text
aliceDist = aliceDist.most_common(50) # Determine top 50 most frequent words
# Print out the most frequent words and it's frequency
for item in aliceDist:
   print(item[0], '\t', item[1])


# Caesar Document
print('Julius Caesar Book - Top 50 words by frequency:')
caesarDist = FreqDist(caesarWords)      # Create a frequency distribution of the words in the Caesar pre-processed text
caesarDist = caesarDist.most_common(50) # Determine top 50 most frequent words
# Print out the most frequent words and it's frequency
for item in caesarDist:
   print(item[0], '\t', item[1])


# 2.b: List the top 50 bigrams by frequencies
# Import file to set up bigrams and bigram measures:
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures() # Define a function we will use to apply bigram measures to the texts

# Alice Document
print('Alice Book - Top 50 bigrams by frequency:')
aliceBigrams = list(nltk.bigrams(aliceWords))  # Uncover bigram pairs in the Alice book
# Let's compare the bigrams to the text in the words:
#print(aliceWords[:51])
#print()
#print(aliceBigrams[:50])

# Let's calculate the frequency score of the bigrams in the Alice text:
aliceFinder = BigramCollocationFinder.from_words(aliceWords)       # Create the bigram finder
aliceScored = aliceFinder.score_ngrams(bigram_measures.raw_freq)   # Score the bigrams by frequency
# Print the raw bigrams:
for bscore in aliceScored[:50]:
   print(bscore)


# Caesar Document
print('Julius Caesar - Top 50 bigrams by frequency:')
caesarBigrams = list(nltk.bigrams(caesarWords))  # Uncover bigram pairs in the Caesar book
# Let's compare the bigrams to the text in the words:
#print(caesarWords[:51])
#print()
#print(caesarBigrams[:50])

# Let's calculate the frequency score of the bigrams in the Caesar text:
caesarFinder = BigramCollocationFinder.from_words(caesarWords)       # Create the bigram finder
caesarScored = caesarFinder.score_ngrams(bigram_measures.raw_freq)   # Score the bigrams by frequency
# Print the raw bigrams:
for bscore in caesarScored[:50]:
   print(bscore)


# 2.c: List the top 50 bigrams by their mutual information (pmi) scores (min freq 5)

# Alice Document
print('Alice Book - Top 50 bigrams by PMI score:')
# For the PMI score, I will update the frequency filter of 5
aliceFinderPMI = aliceFinder = BigramCollocationFinder.from_words(aliceWords) # Recall the finder but add PMI to the callable term to reduce overwriting the original finder
aliceFinderPMI.apply_freq_filter(5)                                           # Apply frequency filter of 5
aliceScoredPMI = aliceFinderPMI.score_ngrams(bigram_measures.pmi)             # Score the bigrams using PMI
# Print the PMI scored bigrams:
for bscore in aliceScoredPMI[:50]:
   print(bscore)


# Caesar Document
print('Julius Caesar Book - Top 50 bigrams by PMI score:')
# Again, I will update the frequency filter of 5
caesarFinderPMI = caesarFinder = BigramCollocationFinder.from_words(caesarWords) # Recall the finder but add PMI to the callable term to reduce overwriting the original finder
caesarFinderPMI.apply_freq_filter(5)                                             # Apply frequency filter of 5
caesarScoredPMI = caesarFinderPMI.score_ngrams(bigram_measures.pmi)              # Score the bigrams using PMI
# Print the PMI scored bigrams:
for bscore in caesarScoredPMI[:50]:
   print(bscore)



# Additional merit: Trigram lists
#from nltk.collocations import TrigramCollocationFinder     # pulling this in for trigram reference but we already imported this through import * during bigram code
#from nltk.metrics import TrigramAssocMeasures
trigram_measures = nltk.collocations.TrigramAssocMeasures() # Define a function we will use to apply trigram measures to the texts

# Alice Document
print('Alice Book - Trigrams')
aliceTrigrams = list(nltk.trigrams(aliceWords))                                 # Uncover trigram pairs in the Alice book
print(aliceTrigrams[:50])
aliceFinderTri = TrigramCollocationFinder.from_words(aliceWords)                # Create the trigram finder
#aliceScoredTri = aliceFinderTri.score_ngrams(trigram_measures.raw_freq)        # Score the trigrams by raw frequency to test
aliceFinderTri.apply_freq_filter(3)                                             # Apply a frequency score of 3 --> Note that 5 resulted in very little output
aliceScoredPMITri = aliceFinderTri.score_ngrams(trigram_measures.raw_freq)      # Score the trigrams using PMI
# Print the raw trigrams:
for bscore in aliceScoredPMITri[:50]:
   print(bscore)


# Caesar Document
print('Julius Caesar Book - Trigrams')
caesarTrigrams = list(nltk.trigrams(caesarWords))                                 # Uncover trigram pairs in the Caesar book
#print(caesarTrigrams[:50])
caesarFinderTri = TrigramCollocationFinder.from_words(caesarWords)                # Create the trigram finder
#caesarScoredTri = caesarFinderTri.score_ngrams(trigram_measures.raw_freq)        # Score the trigrams by raw frequency to test
caesarFinderTri.apply_freq_filter(3)                                              # Apply a frequency score of 3
caesarScoredPMITri = caesarFinderTri.score_ngrams(trigram_measures.raw_freq)      # Score the trigrams using PMI
# Print the raw trigrams:
for bscore in caesarScoredPMITri[:50]:
   print(bscore)



# Part 3: Describe a problem or question based on the differences between the two documents
## Let's compare author writing style based on the code output --> see report
