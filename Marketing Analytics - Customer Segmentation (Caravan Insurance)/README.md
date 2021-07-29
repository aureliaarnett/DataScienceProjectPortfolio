# Predicting customer buying behaviors using segmentation analysis

## Table of contents
* [General info](#general-info)
* [Data source](#data-source)
* [Technologies used](#technologies-used)
* [Methods used](#methods-used)
* [Code example](#code-example)
* [Screenshots](#screenshots)
* [Contact](#contact)

## General info
> This project explores customer segmentation techniques to identify clusters of customers that are likely to purchase the carravan insurrance policy and predict their buying behavior based on clusters of existing policy holders. 

## Data source
Sources from: https://www.kaggle.com/uciml/caravan-insurance-challenge#caravan-insurance-challenge.csv

## Technologies used
* R (Data modeling)
* Excel (Regression)

## Methods used
* Logistic regression
* Statistical analysis
* Naive Bayes clustering
* K-Means clustering
* Random Forest decision tree

## Code example
#NB Pre-Processing\
caravan_df_trainNB <- caravan_df_train\
caravan_df_testNB <- caravan_df_test\
\
caravan_df_trainNB$Customer_Subtype <- as.factor(caravan_df_trainNB$Customer_Subtype)\
caravan_df_testNB$Customer_Subtype <- as.factor(caravan_df_testNB$Customer_Subtype)\
caravan_df_trainNB$Customer_main_type <- as.factor(caravan_df_trainNB$Customer_main_type)\
caravan_df_testNB$Customer_main_type <- as.factor(caravan_df_testNB$Customer_main_type)\
\
#Classification Using Naive Bayes\
library(e1071)\
#Can handle both categorical and numeric input,\
#but output must be categorical\
caravan_df_trainNB$Number_of_mobile_home_policies <- factor(caravan_df_trainNB$Number_of_mobile_home_policies, labels = c(0,1))\
model <- naiveBayes(as.factor(Number_of_mobile_home_policies)~., data=caravan_df_trainNB)\
model\
#NB Prediction\
tst <- caravan_df_testNB[,-86]\
prediction <- predict(model, newdata = tst)\
table(caravan_df_testNB$Number_of_mobile_home_policies, prediction, dnn=list('actual','predicted'))\

## Screenshots
**Naive Bayes** -- where column 1 represents the average A-priori probability and column 2 represents the standard deviation of customers within the variable type (ex: demographic) who are customers and non-customers.
![image](https://user-images.githubusercontent.com/75768214/127575126-d96c8928-f52f-44e1-b985-7cf71d62e6e7.png)
\
\
**Logistic Regression** -- correlation matrix determining which variable types are most relevant to the carravan insurrance policy.
![image](https://user-images.githubusercontent.com/75768214/127575660-f9f24036-a7b4-428c-bd44-77e394f2bcc2.png)

## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
