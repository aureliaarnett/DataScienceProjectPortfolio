# Aurelia Arnett

# Choose a corpus: Gutenbook
import nltk
from nltk.corpus import gutenberg

gutenberg_text = gutenberg.raw()
#print(gutenberg_text[:150], '\n')


### Split the raw text into senteces ###
#gutenberg_tokens = gutenberg.words()
#print(gutenberg_tokens[:20])
gutenberg_split = nltk.sent_tokenize(gutenberg_text)                            # main step here
print('Split the raw text into sentences:')
print(gutenberg_split[:2])
print()


### tokenize the list of sentences ###
tokenize_gutenberg = [nltk.word_tokenize(sent) for sent in gutenberg_split]     # main step here
print('Tokenize the list of sentences:')
print(tokenize_gutenberg[:2])
print()


### run the tagger on the list of sentences (result is a list of lists of (word, tag) pairs) ###
# we will use the t2 tagger
# but first, must create a trained tagger:
from nltk.corpus import treebank
treebank_tagged = treebank.tagged_sents()
size = int(len(treebank_tagged) * 0.9)
treebank_train = treebank_tagged[:size]
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(treebank_train, backoff=t0)
t2 = nltk.BigramTagger(treebank_train, backoff=t1)

# now apply the tagger to the gutenberg tokens:
tag_gutenberg = [t2.tag(tokens) for tokens in tokenize_gutenberg]
### tagging: [nltk.pos_tag(tokens) for tokens in tokenize_gutenberg]             # main step here
print('Apply tagger to the gutenberg tokens:')
print(tag_gutenberg[:2])
print()


### flatten the list to get just one list of (word, tag) ### 
flatten_gutenberg = [pair for sent in tag_gutenberg for pair in sent]            # main step here
print('Flatten the list to get just one list of (word, tag):')
print(flatten_gutenberg[:50])
print()

### freq dist of tags ###
flatten_gutenberg_fd = nltk.FreqDist(tag for (word, tag) in flatten_gutenberg)
# print(flatten_gutenberg_fd.keys(), '\n') #observe tags
print('Print a Freq Dist of the most common tags:')
for tag,freq in flatten_gutenberg_fd.most_common():
    print(tag,freq)



### PRECISION: ###
# adjust = len(flatten_gutenberg) / len(flat_treebank)
