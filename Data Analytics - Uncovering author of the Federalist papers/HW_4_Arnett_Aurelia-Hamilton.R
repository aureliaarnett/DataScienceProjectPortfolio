# Aurelia Arnett
# IST 707 Assignment 4 - Hamilton
# ** Majority of code used was provided by Professor Gates in lecture 4 on 10-27-2019

#install.packages("tm")
library(tm)
library(stringr)
library(wordcloud)
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
NovelsCorpusHamDispt <- Corpus(DirSource("HamiltonFilesDispt"))
(getTransformations()) ## These work with library tm
(ndocs<-length(NovelsCorpusHamDispt)) ## HM & Jay docs removed

# Confirm docs have been read in
(summary(NovelsCorpusHamDispt))  ## This will list the docs in the corpus
(meta(NovelsCorpusHamDispt[[12]])) ## meta data are data hidden within a doc - like id
(meta(NovelsCorpusHamDispt[[1]],5)) ## show the ID of doc number 1


# Data Cleansing
(minTermFreq <- ndocs * 0.01) # ignore words that appear less than 1% of the time in the documents
(maxTermFreq <- ndocs * .50) # ignore overly common words that appear more than 50% of the time in the documents



# Determine if there are words to be removed (build a word cloud)
library("SnowballC")
Novels_dtm_HamDispt <- DocumentTermMatrix(NovelsCorpusHamDispt,
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

(inspect(Novels_dtm_HamDispt))  ## This takes a look at a subset - a peak
DTM_mat <- as.matrix(Novels_dtm_HamDispt)
(DTM_mat[1:13,1:10])


(WordFreq <- colSums(as.matrix(Novels_dtm_HamDispt)))

(head(WordFreq))
(length(WordFreq))
ord <- order(WordFreq)
(WordFreq[head(ord)])
(WordFreq[tail(ord)])
## Row Sums
(Row_Sum_Per_doc <- rowSums((as.matrix(Novels_dtm_HamDispt))))


## Copy of a matrix format of the data
Novels_M <- as.matrix(Novels_dtm_HamDispt)
(Novels_M[1:13,1:5])

## Normalized Matrix of the data
Novels_M_N1 <- apply(Novels_M, 1, function(i) round(i/sum(i),5))
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
Novels_DF <- as.data.frame(as.matrix(Novels_dtm_HamDispt))
length(Novels_DF)
(head(Novels_DF))
str(Novels_DF)
(Novels_DF$abolit)
(nrow(Novels_DF))  ## Each row is a novel

######### Next - you can convert a matrix (or normalized matrix) to a DF
Novels_DF_From_Matrix_N<-as.data.frame(Novels_Matrix_Norm)
length(Novels_DF_From_Matrix_N)
(head(Novels_DF_From_Matrix_N))



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
(Novels_Matrix_Norm[c(1:6),c(1:5)])
## 3) For fun, let's also do this for a non-normalized matrix
##    I will use Novels_M from above
## Let's look at it
(Novels_M[c(1:6),])



###############################################################################
################# Build distance MEASURES using the dist function #############
###############################################################################
## Make sure these distance matrices make sense.
distMatrix_E <- dist(Novels_M, method="euclidean")
print(distMatrix_E)

distMatrix_E_norm <- dist(Novels_Matrix_Norm, method="euclidean")
print(distMatrix_E_norm)

distMatrix_C <- dist(Novels_M, method="cosine")
print(distMatrix_C)

distMatrix_C_norm <- dist(Novels_Matrix_Norm, method="cosine")
print(distMatrix_C_norm)
###########################################################################



############# Clustering #############################
## Hierarchical
## Euclidean
groups_E <- hclust(distMatrix_E,method="ward.D")
plot(groups_E, cex=.7, hang=-1)
rect.hclust(groups_E, k=3)

## Euclidean for Normalized Matrix
groups_E_n <- hclust(distMatrix_E_norm,method="ward.D")
plot(groups_E_n, cex=.7, hang=-1)
rect.hclust(groups_E, k=3)

## Cosine Similarity
groups_C <- hclust(distMatrix_C,method="ward.D")
plot(groups_C, cex=0.7, hang=-1)
rect.hclust(groups_C, k=3)

## Cosine Similarity for Normalized Matrix
groups_C_n <- hclust(distMatrix_C_norm,method="ward.D")
plot(groups_C_n, cex=0.7, hang=-1)
rect.hclust(groups_C_n, k=3)

distance0 <- get_dist(Novels_Matrix_Norm,method = "euclidean")
fviz_dist(distance0, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))

distance1 <- get_dist(Novels_Matrix_Norm,method = "manhattan")
fviz_dist(distance1, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))



############# Clustering #############################
## k-means
## Next, our current matrix does NOT have the columns as the docs
## so we need to transpose it first....
## Run the following twice...
(nrow(Novels_Matrix_Norm))
(ncol(Novels_Matrix_Norm))
#str(m_norm)
## k means
kmeansFIT_1 <- kmeans(Novels_Matrix_Norm,centers=3)
(kmeansFIT_1)
#print("Kmeans details:")
(summary(kmeansFIT_1))
(kmeansFIT_1$cluster)



## One issue here is that kmeans does not
## allow us to use cosine sim
## This is creating results that are not as good. 
####################

### This is a cluster vis
fviz_cluster(kmeansFIT_1, Novels_M)
## --------------------------------------------
#########################################################




############# Clustering #############################
## Hierarchical
################# Expectation Maximization ---------
## When Clustering, there are many options. 

ClusFI <- Mclust(Novels_M,G=3)
(ClusFI)
summary(ClusFI)
#plot(ClusFI, what = "classification")



