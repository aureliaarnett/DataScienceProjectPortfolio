# Uncovering the authors of the Federalist papers - Hamilton, Madison, or Jay

## Table of contents
* [General info](#general-info)
* [Technologies used](#technologies-used)
* [Python methods used](#python-methods-used)
* [Code example](#code-example)
* [Screenshots from analysis](#screenshots-from-analysis)
* [Contact](#contact)

## General info
> This project evaluates 51 essays known to be written by Hamilton, 15 essays known to be written by Madison, 3 essays known to be written by both Hamilton and Madison, and 5 essays known to be written by Jay to predict the author of 11 mystery documents using clustering techniques and data mining in R.

## Technologies used
* R

## Python methods used
* Format the .csv data into a corpus (collection of written texts)
* Convert corpus text into a data term matrix in R
* Evaluate distance measures between 2 Hamilton docs and 2 Madison docs to uncover text similarities (Euclidean and Cosine similarity calculations)
* K-means clustering
* Expectation-maximization algorithm

## Code example
#Load Corpus:\
NovelsCorpusHamDispt <- Corpus(DirSource("HamiltonFilesDispt"))\
(getTransformations()) ## These work with library tm\
(ndocs<-length(NovelsCorpusHamDispt)) ## HM & Jay docs removed\
\
#Confirm docs have been read in\
(summary(NovelsCorpusHamDispt))  ## This will list the docs in the corpus\
(meta(NovelsCorpusHamDispt[[12]])) ## meta data are data hidden within a doc - like id\
(meta(NovelsCorpusHamDispt[[1]],5)) ## show the ID of doc number 1\
\
#Data Cleansing\
(minTermFreq <- ndocs * 0.01) # ignore words that appear less than 1% of the time in the documents\
(maxTermFreq <- ndocs * .50) # ignore overly common words that appear more than 50% of the time in the documents\
\
#Determine if there are words to be removed (build a word cloud)\
library("SnowballC")\
Novels_dtm_HamDispt <- DocumentTermMatrix(NovelsCorpusHamDispt,\
                                 control = list(\
                                   stopwords = TRUE, ## remove normal stopwords\
                                   wordLengths=c(4, 10), ## get rid of words of len 3 or smaller or larger than 10\
                                   removePunctuation = TRUE,\
                                   removeNumbers = TRUE,\
                                   tolower=TRUE,\
                                   stemming = TRUE,\
                                   remove_separators = TRUE,\
                                   bounds = list(global = c(minTermFreq, maxTermFreq))\
                                 ))\
(inspect(Novels_dtm_HamDispt))  ## This takes a look at a subset - a peak\
DTM_mat <- as.matrix(Novels_dtm_HamDispt)\
(DTM_mat[1:13,1:10])\
\
(WordFreq <- colSums(as.matrix(Novels_dtm_HamDispt)))\
\
(head(WordFreq))\
(length(WordFreq))\
ord <- order(WordFreq)\
(WordFreq[head(ord)])\
(WordFreq[tail(ord)])\
#Row Sums\
(Row_Sum_Per_doc <- rowSums((as.matrix(Novels_dtm_HamDispt))))\
\
#Copy of a matrix format of the data\
Novels_M <- as.matrix(Novels_dtm_HamDispt)\
(Novels_M[1:13,1:5])\
\
#Normalized Matrix of the data\
Novels_M_N1 <- apply(Novels_M, 1, function(i) round(i/sum(i),5))\
(Novels_M_N1[1:13,1:5])\
#NOTICE: Applying this function flips the data...see above.\
#So, we need to TRANSPOSE IT (flip it back)  The "t" means transpose\
Novels_Matrix_Norm <- t(Novels_M_N1)\
(Novels_Matrix_Norm[1:13,1:10])\

#Screenshots from analysis
**Load all essays into a corpus**: Hierarchical cluster diagram of a corpus with all essays included\
![image](https://user-images.githubusercontent.com/75768214/118076678-863bc700-b367-11eb-8f7a-40339954b94b.png)

Cluster visualization for k-means calculations associated with the Hamilton and Hamilton-Madison corpus\
![image](https://user-images.githubusercontent.com/75768214/118077045-34477100-b368-11eb-814b-790fa247764d.png)

Cluster visualization for k-means calculations associated with the Madison and Hamilton-Madison corpus\
![image](https://user-images.githubusercontent.com/75768214/118077062-3dd0d900-b368-11eb-9724-05412c263523.png)


## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
