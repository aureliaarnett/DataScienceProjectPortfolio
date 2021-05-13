# Understanding immigration patterns to increase survival rates

## Table of contents
* [General info](#general-info)
* [Technologies used](#technologies-used)
* [R methods used](#r-methods-used)
* [Code example](#code-example)
* [Screenshots from analysis](#screenshots-from-analysis)
* [Contact](#contact)

## General info
> This project analyzes immigration trends to understand patterns that exist and recommend solutions to increase human survival rates.

## Technologies used
* R

## R methods used
* F

## Code example
# Turn character data to factor
MissingMigrantsDF <- MissingMigrantsDF %>% 
  mutate_if(is.character, funs(as.factor))

# Create data frame for ARM
MissingMigrantsARM <- as.data.frame(MissingMigrantsDF) %>% 
  select(-Reported_Date) %>% 
  mutate_if(is.character, funs(as.factor))
# Remove columns as other column is the sum of these two columns
MissingMigrantsARM <- MissingMigrantsARM[,-4:-5]
# Take out column of cause of dealth not categorized
MissingMigrantsARM <- MissingMigrantsARM[,-9]

# Discretize data 
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


## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
