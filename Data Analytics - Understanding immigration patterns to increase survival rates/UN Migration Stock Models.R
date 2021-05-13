# Modeling for UN Migrant Stock Dataset

## Set WD ##
setwd("C:\\Users\\aua\\Documents\\IST707 Final Project")

## Clean the Data ## 
library(readxl)
library(sqldf)

originCountryList <-
  c(
    'Total',
    'Other South',
    'Other North',
    'Afghanistan',
    'Albania',
    'Algeria',
    'American Samoa',
    'Andorra',
    'Angola',
    'Anguilla',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Aruba',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bermuda',
    'Bhutan',
    'Bolivia (Plurinational State of)',
    'Bonaire, Sint Eustatius and Saba',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'British Virgin Islands',
    'Brunei Darussalam',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cabo Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cayman Islands',
    'Central African Republic',
    'Chad',
    'Channel Islands',
    'Chile',
    'China',
    'China, Hong Kong SAR',
    'China, Macao SAR',
    'Colombia',
    'Comoros',
    'Congo',
    'Cook Islands',
    'Costa Rica',
    'Côte d\'Ivoire',
    'Croatia',
    'Cuba',
    'Curaçao',
    'Cyprus',
    'Czechia',
    'Dem. People\'s Republic of Korea',
    'Democratic Republic of the Congo',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini',
    'Ethiopia',
    'Falkland Islands (Malvinas)',
    'Faroe Islands',
    'Fiji',
    'Finland',
    'France',
    'French Guiana',
    'French Polynesia',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Gibraltar',
    'Greece',
    'Greenland',
    'Grenada',
    'Guadeloupe',
    'Guam',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Holy See',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran (Islamic Republic of)',
    'Iraq',
    'Ireland',
    'Isle of Man',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Kuwait',
    'Kyrgyzstan',
    'Lao People\'s Democratic Republic',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Martinique',
    'Mauritania',
    'Mauritius',
    'Mayotte',
    'Mexico',
    'Micronesia (Fed. States of)',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Montserrat',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Caledonia',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Niue',
    'North Macedonia',
    'Northern Mariana Islands',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Puerto Rico',
    'Qatar',
    'Republic of Korea',
    'Republic of Moldova',
    'Réunion',
    'Romania',
    'Russian Federation',
    'Rwanda',
    'Saint Helena',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Pierre and Miquelon',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Sint Maarten (Dutch part)',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'State of Palestine',
    'Sudan',
    'Suriname',
    'Sweden',
    'Switzerland',
    'Syrian Arab Republic',
    'Tajikistan',
    'Thailand',
    'Timor-Leste',
    'Togo',
    'Tokelau',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Turks and Caicos Islands',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United Republic of Tanzania',
    'United States of America',
    'United States Virgin Islands',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Venezuela (Bolivarian Republic of)',
    'Viet Nam',
    'Wallis and Futuna Islands',
    'Western Sahara',
    'Yemen',
    'Zambia',
    'Zimbabwe'
  )

# Read table for total population data
migrantDataTotal <- read_xlsx("UN_MigrantStockByOriginAndDestination_2019.xlsx", sheet="Table 1",
                              range = "A16:IG1997", col_names = TRUE)

# Omit unnecessary fields
migrantDataTotal<-migrantDataTotal[,-c(2,4,5,6)]
migrantDataTotal

# Rename 'Year' and 'Country' fields
colnames(migrantDataTotal)[1] <- "Year"
colnames(migrantDataTotal)[2] <- "Country"

# Ensure columns are correct data types
migrantDataTotal$Year <- as.Date(paste(migrantDataTotal$Year, 12, 31, sep = "-"))
migrantDataTotal[originCountryList] <- sapply(migrantDataTotal[originCountryList],as.integer)
migrantDataTotal[originCountryList] <- sapply(migrantDataTotal[originCountryList],as.numeric)

# Omit regions that aren't countrys
migrantDataTotalCountryOnly <- sqldf("select * from migrantDataTotal where Country not in (
    'WORLD',
    'UN development groups',
    'More developed regions',
    'Less developed regions',
    'World Bank income groups',
    'High-income countries',
    'Middle-income countries',
    'Low-income countries',
    'No income group available',
    'Geographic regions',
    'Africa',
    'Asia',
    'Europe',
    'Latin America and the Caribbean',
    'Northern America',
    'Oceania',
    'Sustainable Development Goal (SDG) regions',
    'SUB-SAHARAN AFRICA',
    'Eastern Africa',
    'Middle Africa',
    'Southern Africa',
    'Western Africa',
    'NORTHERN AFRICA AND WESTERN ASIA',
    'Northern Africa',
    'Western Asia',
    'CENTRAL AND SOUTHERN ASIA',
    'Central Asia',
    'Southern Asia',
    'EASTERN AND SOUTH-EASTERN ASIA',
    'Eastern Asia',
    'South-Eastern Asia',
    'LATIN AMERICA AND THE CARIBBEAN',
    'Caribbean',
    'Central America',
    'South America',
    'OCEANIA',
    'Australia / New Zealand',
    'Melanesia',
    'Micronesia',
    'Polynesia',
    'EUROPE AND NORTHERN AMERICA',
    'EUROPE',
    'Eastern Europe',
    'Northern Europe',
    'Southern Europe',
    'Western Europe',
    'NORTHERN AMERICA',
    'Least developed countries',
    'Less developed regions, excluding least developed countries',
    'Upper-middle-income countries',
    'Lower-middle-income countries'
  )")

# Read table for male data
migrantDataMale <- read_xlsx("UN_MigrantStockByOriginAndDestination_2019.xlsx", sheet="Table 2",
                             range = "A16:IG1997", col_names = TRUE)

# Omit unnecessary fields
migrantDataMale<-migrantDataMale[,-c(2,4,5,6)]

# Rename 'Year' and 'Country' fields
colnames(migrantDataMale)[1] <- "Year"
colnames(migrantDataMale)[2] <- "Country"

# Ensure columns are correct data types
migrantDataMale$Year <- as.Date(paste(migrantDataMale$Year, 12, 31, sep = "-"))
migrantDataMale[originCountryList] <- sapply(migrantDataMale[originCountryList],as.integer)
migrantDataMale[originCountryList] <- sapply(migrantDataMale[originCountryList],as.numeric)

# Omit regions that aren't countrys
migrantDataMaleCountryOnly <- sqldf("select * from migrantDataMale where Country not in (
    'WORLD',
    'UN development groups',
    'More developed regions',
    'Less developed regions',
    'World Bank income groups',
    'High-income countries',
    'Middle-income countries',
    'Low-income countries',
    'No income group available',
    'Geographic regions',
    'Africa',
    'Asia',
    'Europe',
    'Latin America and the Caribbean',
    'Northern America',
    'Oceania',
    'Sustainable Development Goal (SDG) regions',
    'SUB-SAHARAN AFRICA',
    'Eastern Africa',
    'Middle Africa',
    'Southern Africa',
    'Western Africa',
    'NORTHERN AFRICA AND WESTERN ASIA',
    'Northern Africa',
    'Western Asia',
    'CENTRAL AND SOUTHERN ASIA',
    'Central Asia',
    'Southern Asia',
    'EASTERN AND SOUTH-EASTERN ASIA',
    'Eastern Asia',
    'South-Eastern Asia',
    'LATIN AMERICA AND THE CARIBBEAN',
    'Caribbean',
    'Central America',
    'South America',
    'OCEANIA',
    'Australia / New Zealand',
    'Melanesia',
    'Micronesia',
    'Polynesia',
    'EUROPE AND NORTHERN AMERICA',
    'EUROPE',
    'Eastern Europe',
    'Northern Europe',
    'Southern Europe',
    'Western Europe',
    'NORTHERN AMERICA',
    'Least developed countries',
    'Less developed regions, excluding least developed countries',
    'Upper-middle-income countries',
    'Lower-middle-income countries'
  )")

# Read table for female data
migrantDataFemale <- read_xlsx("UN_MigrantStockByOriginAndDestination_2019.xlsx", sheet="Table 2",
                               range = "A16:IG1997", col_names = TRUE)

# Omit unnecessary fields
migrantDataFemale<-migrantDataFemale[,-c(2,4,5,6)]

# Rename 'Year' and 'Country' fields
colnames(migrantDataFemale)[1] <- "Year"
colnames(migrantDataFemale)[2] <- "Country"

# Ensure columns are correct data types
migrantDataFemale$Year <- as.Date(paste(migrantDataFemale$Year, 12, 31, sep = "-"))
migrantDataFemale[originCountryList] <- sapply(migrantDataFemale[originCountryList],as.integer)
migrantDataFemale[originCountryList] <- sapply(migrantDataFemale[originCountryList],as.numeric)

# Omit regions that aren't countrys
migrantDataFemaleCountryOnly <- sqldf("select * from migrantDataFemale where Country not in (
    'WORLD',
    'UN development groups',
    'More developed regions',
    'Less developed regions',
    'World Bank income groups',
    'High-income countries',
    'Middle-income countries',
    'Low-income countries',
    'No income group available',
    'Geographic regions',
    'Africa',
    'Asia',
    'Europe',
    'Latin America and the Caribbean',
    'Northern America',
    'Oceania',
    'Sustainable Development Goal (SDG) regions',
    'SUB-SAHARAN AFRICA',
    'Eastern Africa',
    'Middle Africa',
    'Southern Africa',
    'Western Africa',
    'NORTHERN AFRICA AND WESTERN ASIA',
    'Northern Africa',
    'Western Asia',
    'CENTRAL AND SOUTHERN ASIA',
    'Central Asia',
    'Southern Asia',
    'EASTERN AND SOUTH-EASTERN ASIA',
    'Eastern Asia',
    'South-Eastern Asia',
    'LATIN AMERICA AND THE CARIBBEAN',
    'Caribbean',
    'Central America',
    'South America',
    'OCEANIA',
    'Australia / New Zealand',
    'Melanesia',
    'Micronesia',
    'Polynesia',
    'EUROPE AND NORTHERN AMERICA',
    'EUROPE',
    'Eastern Europe',
    'Northern Europe',
    'Southern Europe',
    'Western Europe',
    'NORTHERN AMERICA',
    'Least developed countries',
    'Less developed regions, excluding least developed countries',
    'Upper-middle-income countries',
    'Lower-middle-income countries'
  )")

' Note from the above
- 3 datasets exist: total, male, and female information on the migrant data

Questions to answer:
1. Which countries have the highest immigration rates than others?
2. Which countries have the highest emigration rates than others?
3. Which two countries have to most migrants between each other?
5. Which gender has the highest immigration rates?
'

## Model ##
library(e1071)
library(mlr)
library(caret)
library(datasets)
library(ggplot2)
library(MASS)

## Visualize ## 
colnames(migrantDataTotalCountryOnly)
migrantDataMaleCountryOnly
migrantDataFemaleCountryOnly

## Train & Test data ##
# Test set
testData <- "UNMigrantTest.csv"
testDataDF <- read.csv(testData, header = TRUE)
(head(testDataDF))

# Train set
trainData <- "UNMigrantTrain.csv"
trainDataDF <- read.csv(trainData, header = TRUE)
(head(trainDataDF))

migrantDataTotNoYr <- migrantDataTotalCountryOnly[,-1]
str(migrantDataTotalCountryOnly)
migrantDataTotNoYr <- migrantDataTotNoYr[,-2:-4] # remove total column & 'other' data
migrantDataTotNoYr[1:5,1:5]
migrantDataTotNoYr$Country
## Country = desintation; remaining countries (the column data) = origin

# change 'Country' column to a factor
migrantDataTotNoYr['Country'] <- as.factor(migrantDataTotNoYr['Country'])

## Question 1: Which countries have the highest immigration rates than others? ##
## SVM
rainSVM <- svm(destination~., data=trainDataDF, kernel="linear", cost=.1, scale=FALSE)
print(trainSVM)
predictSVM <- predict(trainSVM, testDataDF, type="class")
predictSVM
table(trainDataDF[1:12,]$destination,predictSVM)

trainSVM_UNData <- svm(Country~., data=migrantDataTotNoYr, kernel="linear", cost=.1, scale=FALSE)
predictSVM_UNData <- predict(trainSVM, migrantDataTotNoYr, type="class")



## ARM
#determine confidence
library(arules)
# confidence of .5, support of .25
rulesC5S25 <- arules::apriori(data=migrantDataTotNoYr,parameter = list(supp=.05, conf=.5, minlen=2), appearance = list(default="Country", rhs="pep=Afghanastan"),control=list(verbose=FALSE))
rulesC5S25 <- arules::apriori(data=migrantDataTotNoYr,parameter = list(supp=.05, conf=.5, minlen=10), appearance = list(default="Country", rhs="pep=Afghanastan"))
inspect(rulesC5S25)



## Clustering
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

'
#eudlidean
buildClust_UNData_eu <- dist(migrantDataTotNoYr, method="euclidean")
print(buildClust_UNData_eu)

clust_UNData_eu <- hclust(buildClust_UNData_eu,method="ward.D")
plot(buildClust_UNData_eu, cex=0.9, hang=-1)
rect.hclust(buildClust_UNData_eu, k=4)


#cosine
builCclust_UNData_cos <- dist(migrantDataTotNoYr, method="cosine")
print(builCclust_UNData_cos)

clust_UNData_cos <- hclust(builCclust_UNData_cos,method="ward.D")
plot(clust_UNData_cos, cex=0.9, hang=-1)
rect.hclust(clust_UNData_cos, k=4)


'

## Decision Trees
DT_UNData_noLabel <- migrantDataTotNoYr[,-1]
DT_UNData<- naive_bayes(Country~., data=migrantDataTotNoYr)
predDT_UNData<-predict(DT_UNData, DT_UNData_noLabel, type = c("class"))
head(predDT_UNData)
table(DT_UNData_noLabel, predDT_UNData)
#plot(NB_object, legend.box = FALSE)
#viz:
ggplot(DRTestDF, aes(x=NB_prediction)) + geom_freqpoly(binwidth=1, stat="count")


## Random Forest
library(randomForest)
'
rf_UNData = randomForest(Country ~ . , data = migrantDataTotNoYr)
print(rf_UNData)

predrf_UNData<-predict(rf_UNData, migrantDataTotNoYr) 
(table(predrf_UNData, migrantDataTotNoYr$Country))
'

## Naive Bayes
library(e1071)
library(naivebayes)

NB_UNData <- naiveBayes(Country~., data=migrantDataTotNoYr, laplace = 1, na.action = na.pass)
predNB_UNData <- predict(NB_UNData, newdata=migrantDataTotNoYr, type=c("class"))
table(migrantDataTotNoYr$Country, predNB_UNData)



