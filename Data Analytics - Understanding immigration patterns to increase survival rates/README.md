# Understanding immigration patterns to increase survival rates

## Table of contents
* [General info](#general-info)
* [Technologies used](#technologies-used)
* [R methods used](#r-methods-used)
* [Code example](#code-example)
* [Screenshots from analysis](#screenshots-from-analysis)
* [Contact](#contact)

## General info
> This project analyzes immigration trends (origin and destination, time of year, transportation methods) to understand patterns that exist and recommends solutions to increase human survival rates.

## Technologies used
* R

## R methods used
* Association Rule Mining
* Naive Bayes
* Decision Tree
* Random Forest

## Code example
#Turn character data to factor\
MissingMigrantsDF <- MissingMigrantsDF %>%\
  mutate_if(is.character, funs(as.factor))\
\
#Create data frame for ARM
MissingMigrantsARM <- as.data.frame(MissingMigrantsDF) %>%\
  select(-Reported_Date) %>%\
  mutate_if(is.character, funs(as.factor))\
#Remove columns as other column is the sum of these two columns\
MissingMigrantsARM <- MissingMigrantsARM[,-4:-5]\
#Take out column of cause of dealth not categorized\
MissingMigrantsARM <- MissingMigrantsARM[,-9]\
\
#Discretize data\
MissingMigrantsARM$Total_Dead_Missing <-\
  cut(MissingMigrantsARM$Total_Dead_Missing, breaks=c(-Inf, 5, 10, 50, Inf),\
      labels=c("Low", "Med","High", "Very_High"))\
MissingMigrantsARM$Num_of_Survivors <-\
  cut(MissingMigrantsARM$Num_of_Survivors, breaks=c(-Inf, 5, 10, 50, Inf),\
      labels=c("Low", "Med","High", "Very_High"))\
MissingMigrantsARM$Num_of_Females <-\
  cut(MissingMigrantsARM$Num_of_Females, breaks=c(-Inf, 0, 5, 10, 50, Inf),\
      labels=c("Zero", "Low", "Med","High", "Very_High"))\
MissingMigrantsARM$Num_of_Males <-\
  cut(MissingMigrantsARM$Num_of_Males, breaks=c(-Inf, 0, 5, 10, 50, Inf),\
      labels=c("Zero", "Low", "Med","High", "Very_High"))\
MissingMigrantsARM$Num_of_Children <-\
  cut(MissingMigrantsARM$Num_of_Children, breaks=c(-Inf, 0, 5, 10, 50, Inf),\
      labels=c("Zero", "Low", "Med","High", "Very_High"))\
#str(MissingMigrantsARM)\
\
MissingMigrantsARM1 <- subset.data.frame(MissingMigrantsARM, Total_Dead_Missing == "Very_High")\

## Screenshots from analysis
**Data discovery to visualize trends**\
Total Dead and Missing Migrants by Reported Year and Region of Incident\
![image](https://user-images.githubusercontent.com/75768214/118079598-5263a000-b36d-11eb-8199-d1e83c859478.png)

Total Dead and Missing Migrants by Region of Incident and Category\
![image](https://user-images.githubusercontent.com/75768214/118079684-77f0a980-b36d-11eb-9673-78c43b994acb.png)

Total Dead and Missing Migrants by Region of Incident and Category\
![image](https://user-images.githubusercontent.com/75768214/118079720-8343d500-b36d-11eb-8f02-e3fa94a2e44c.png)

Total Dead and Missing Migrants by Reported Year and Gender\
![image](https://user-images.githubusercontent.com/75768214/118079733-8a6ae300-b36d-11eb-9363-1104afb87b0e.png)

**Data analysis to recommend assistant efforts**\
Decision Tree output\
![image](https://user-images.githubusercontent.com/75768214/118079964-02d1a400-b36e-11eb-89c7-b879ba69bef7.png)

## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
