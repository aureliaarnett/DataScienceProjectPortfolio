# Aurelia Arnett
# IST 707 Assignment 4 - All Data
# ** Majority of code used was provided by Professor Gates in lecture 4 on 10-27-2019

#install.packages("tm")
library(tm)
library(stringr)
library(wordcloud)
##set working directory
## ONCE: install.packages("slam")
library(slam)
library(quanteda)
## ONCE: install.packages("quanteda")
library(arules)
##ONCE: install.packages('proxy')
library(proxy)
library(cluster)
library(stringi)
library(proxy)
library(Matrix)
# install.packages('tidytext')
library(tidytext) # convert DTM to DF
library(plyr) ## for adply
library(ggplot2)
library(factoextra) # for fviz
# install.packages('mclust')
library(mclust) # for Mclust EM clustering


# Set Directory:
setwd("C:\\Users\\aua\\Documents\\IST707 Week 4 HW")

# Load Corpus:
NovelsCorpus <- Corpus(DirSource("FedPapersCorpus"))
(getTransformations()) ## These work with library tm
(ndocs<-length(NovelsCorpus)) ## HM & Jay docs removed

# Confirm docs have been read in
(summary(NovelsCorpus))  ## This will list the docs in the corpus
(meta(NovelsCorpus[[12]])) ## meta data are data hidden within a doc - like id
(meta(NovelsCorpus[[1]],5)) ## show the ID of doc number 1


# Data Cleansing
(minTermFreq <- ndocs * 0.01) # ignore words that appear less than 1% of the time in the documents
(maxTermFreq <- ndocs * .50) # ignore overly common words that appear more than 50% of the time in the documents



# Determine if there are words to be removed (build a word cloud)
library("SnowballC")
Novels_dtm <- DocumentTermMatrix(NovelsCorpus,
                                 control = list(
                                   stopwords = TRUE, ## remove normal stopwords
                                   wordLengths=c(4, 10), ## get rid of words of len 3 or smaller or larger than 10
                                   removePunctuation = TRUE,
                                   removeNumbers = TRUE,
                                   tolower=TRUE,
                                   stemming = TRUE,
                                   remove_separators = TRUE,
                                   bounds = list(global = c(minTermFreq, maxTermFreq))
                                 ))

(inspect(Novels_dtm))  ## This takes a look at a subset - a peak
DTM_mat <- as.matrix(Novels_dtm)
(DTM_mat[1:13,1:10])


/(WordFreq <- colSums(as.matrix(Novels_dtm)))

(head(WordFreq))
(length(WordFreq))
ord <- order(WordFreq)
(WordFreq[head(ord)])
(WordFreq[tail(ord)])
## Row Sums
(Row_Sum_Per_doc <- rowSums((as.matrix(Novels_dtm))))


#############################################################
########### Creating and testing a small function ###########
#############################################################
## Create a small pretend matrix
## Using 1 in apply does rows, using a 2 does columns
(mymat = matrix(1:12,3,4))
freqs2 <- apply(mymat, 1, function(i) i/sum(i))  ## this normalizes
## Oddly, this re-organizes the matrix - so I need to transpose back
(t(freqs2))
## OK - so this works. Now I can use this to control the normalization of
## my matrix...
#############################################################

## Copy of a matrix format of the data
Novels_M <- as.matrix(Novels_dtm)
(Novels_M[1:13,1:5])

## Normalized Matrix of the data
Novels_M_N1 <- apply(Novels_M, 1, function(i) round(i/sum(i),3))
(Novels_M_N1[1:13,1:5])
## NOTICE: Applying this function flips the data...see above.
## So, we need to TRANSPOSE IT (flip it back)  The "t" means transpose
Novels_Matrix_Norm <- t(Novels_M_N1)
(Novels_Matrix_Norm[1:13,1:10])

############## Always look at what you have created ##################
## Have a look at the original and the norm to make sure
(Novels_M[1:13,1:10])
(Novels_Matrix_Norm[1:13,1:10])


##################################################################
###############   Convert to dataframe     #######################
##################################################################
## It is important to be able to convert between format.
## Different models require or use different formats.
## First - you can convert a DTM object into a DF...
(inspect(Novels_dtm))
Novels_DF <- as.data.frame(as.matrix(Novels_dtm))
(head(Novels_DF))
str(Novels_DF)
(Novels_DF$aunt)
(nrow(Novels_DF))  ## Each row is a novel

######### Next - you can convert a matrix (or normalized matrix) to a DF
Novels_DF_From_Matrix_N<-as.data.frame(Novels_Matrix_Norm)


#######################################################################
#############   Making Word Clouds ####################################
#######################################################################
## This requires a matrix - I will use Novels_M from above. 
## It is NOT mornalized as I want the frequency counts!
## Let's look at the matrix first
(Novels_M[c(1:11),c(3850:3900)])
wordcloud(colnames(Novels_M), Novels_M[1, ], max.words = 20) # words in doc dispt_fed_49 

############### Look at most frequent words by sorting ###############
(head(sort(Novels_M[1,], decreasing = TRUE), n=20)) # n = total num of words in doc dispt_fed_49 
(head(sort(Novels_M[2,], decreasing = TRUE), n=20)) # n = total num of words in doc dispt_fed_50


#######################################################################
##############        Distance Measures          ######################
#######################################################################
## Each row of data is a novel in this case
## The data in each row are the number of time that each word occurs
## The words are the columns
## So, distances can be measured between each pair of rows (or each novel)
## We can determine which novels (rows of numeric word frequencies) are "closer" 
########################################################################
## 1) I need a matrix format
## 2) I will use the matrix above that I created and normalized: Novels_Matrix_Norm
## Let's look at it
(Novels_Matrix_Norm[c(1:6),c(3850:3900)])
## 3) For fun, let's also do this for a non-normalized matrix
##    I will use Novels_M from above
## Let's look at it
(Novels_M[c(1:6),c(3850:3900)])

## Make copies 
m  <- Novels_M
m_norm <-Novels_Matrix_Norm
(str(m_norm))


###############################################################################
################# Build distance MEASURES using the dist function #############
###############################################################################
## Make sure these distance matrices make sense.
distMatrix_E <- dist(m, method="euclidean")
print(distMatrix_E)

distMatrix_E_norm <- dist(m_norm, method="euclidean")
print(distMatrix_E_norm)

distMatrix_C <- dist(m, method="cosine")
print(distMatrix_C)

distMatrix_C_norm <- dist(m_norm, method="cosine")
print(distMatrix_C_norm)
###########################################################################





############# Clustering #############################
## Hierarchical

## Euclidean
groups_E <- hclust(distMatrix_E,method="ward.D")
plot(groups_E, cex=0.9, hang=-1)
rect.hclust(groups_E, k=4)

## Cosine Similarity
groups_C <- hclust(distMatrix_C,method="ward.D")
plot(groups_C, cex=0.9, hang=-1)
rect.hclust(groups_C, k=4)

## Cosine Similarity for Normalized Matrix
groups_C_n <- hclust(distMatrix_C_norm,method="ward.D")
plot(groups_C_n, cex=0.9, hang=-1)
rect.hclust(groups_C_n, k=4)



distance0 <- get_dist(m_norm,method = "euclidean")
fviz_dist(distance0, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))
distance1 <- get_dist(m_norm,method = "manhattan")
fviz_dist(distance1, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))
distance2 <- get_dist(m_norm,method = "pearson")
fviz_dist(distance2, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))
distance3 <- get_dist(m_norm,method = "canberra")
fviz_dist(distance3, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))
distance4 <- get_dist(m_norm,method = "spearman")
fviz_dist(distance4, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))


## Next, our current matrix does NOT have the columns as the docs
## so we need to transpose it first....
## Run the following twice...
(nrow(m))
(ncol(m))
#str(m_norm)
## k means
kmeansFIT_1 <- kmeans(m,centers=4)
(kmeansFIT_1)
#print("Kmeans details:")
(summary(kmeansFIT_1))
(kmeansFIT_1$cluster)



## One issue here is that kmeans does not
## allow us to use cosine sim
## This is creating results that are not as good. 
####################

### This is a cluster vis
fviz_cluster(kmeansFIT_1, m)
## --------------------------------------------
#########################################################

################# Expectation Maximization ---------
## When Clustering, there are many options. 
## I cannot run this as it requires more than 18 Gigs...

ClusFI <- Mclust(m,G=6)
(ClusFI)
summary(ClusFI)
#plot(ClusFI, what = "classification")


########### Frequencies and Associations ###################

## Find frequenct words...
(findFreqTerms(Novels_dtm, 2500))
## Find assocations with aselected conf
(findAssocs(Novels_dtm, 'satisfaction', 0.95))



