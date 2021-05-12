# Understanding factors that impact Airbnb ratings and predicting travel trends

## Table of contents
* [General info](#general-info)
* [Technologies used](#technologies-used)
* [Methods used](#methods-used)
* [Code example](code-example)
* [Screenshots](#screenshots)
* [Contact](#contact)

## General info
> This project analyses factors such as customer satisfaction, ammenities included, type of listing, size of Aribnb, price, location, trends found using Twitter hashtags, and time of year that impact Airbnb ratings, and predicts travel trends based on Twitter hashtags. Final recommendations and output are determined using a series of python programs:
> 1. ProcessStructuredData.py cleanses structured data & processes it into a dictionary data structure
> 2. ProcessUnstructuredData-foo.py files uncover trends in Aribnb amentities, which are found to be unstructured data types (Airbnb host manually enters in amenities included vs selecting from a list) by an using NLP approach
> 3. CollectTwitterHashtags.py collects a set of Twitter hashtags as semi-structured data (JSON) using run_twitter_simple_search_save.py, TweetAuth.py, and run_twitter_simple_search_save.py to authenticate with Twitter, search for the correct terms, and then collect the Twitter data  
> 4. Store-MongoDB.py builds a Mongo DB database to store Twitter data and readTweets.py reads and stores Twitter data in the database

## Technologies used
* Anaconda (Python)
* MongoDB
* Twitter Developer (Extract Tweet Collection in JSON form)

## Methods used
* Data cleansing for structured, unstructured, and semi-structured data
* Data formating: Pandas pd, data summaries, lists
* NLP: NLTK

## Code example
**NLP**: Evaluating Airbnb amenities included for listings with ratings under 50% (unstructured data)\
import nltk\
#Turn the message into tokens\
#NOTE: Used the code $ python -c "import nltk; nltk.download('punkt')" in a cmd prompt to install the nltk package\
\
#Under 50% score\
#Tokenize amenities for listings that have an overall rating under 50%\
#Create a list that contains the amenities/listing\
\
amenitylist50 = [airbnb['Amenities'].replace(" ", "") for airbnb in airbnbList if int(airbnb['OverallRating']) <= 50]\
print('Total number of listings with amenities:', len(amenitylist50))\
alltok_50 = [tok for amenity in amenitylist50 for tok in nltk.word_tokenize(amenity)]\
alltok_50_2 = [tok.lower() for tok in alltok_50]\
\
amenityFD = nltk.FreqDist(alltok_50_2)\
top_words = amenityFD.most_common(32)\
\
amenityFreqList = []\
#print('Amenity, Frequency, % Occurrence')\
for word, freq in top_words:\
   occ = round(100*(freq/len(amenitylist50)))\
   amenitydict = {}\
   amenitydict['Amenity'] = word\
   amenitydict['Frequency'] = freq\
   amenitydict['Occurrence'] = occ\\\
   amenityFreqList.append((word,freq,occ))\
#print(word, freq, occ)\
\
import pandas as pd\
amenityFreqDF = pd.DataFrame(amenityFreqList, columns=['Amenity', 'Frequency', '% Occurrence'])\
amenityFreqDF = amenityFreqDF.drop([0, 16])\
amenityFreqDF = amenityFreqDF.set_index('Amenity')\
print(amenityFreqDF)\
amenityFreqDF.to_csv('2-AmenitiesOver90.csv')\


## Screenshots
**Most common amenities output**:\
Summary results for top amenities: Airbnb’s ranked over 90% offer amenities on the left and Airbnb’s ranked under 50% offer amenities on the right
![image](https://user-images.githubusercontent.com/75768214/117924159-27fcde80-b2aa-11eb-9b6b-584e82de0506.png)

**Top Twitter hashtag results with a travel theme**\
Summarizy results for top hashtags, collection terms reading from left to right: #Airbnb, #Vrbo, #adventure, #travel, #wanderlust, and #destination
![image](https://user-images.githubusercontent.com/75768214/117924318-65616c00-b2aa-11eb-9f80-f2b3dda991b5.png)


## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
