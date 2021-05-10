# Aurelia Arnett
# Purpose: To load Tweets from database collections stored in MongoDB server & initial data discovery
# The tweets that are loaded in are from two different user timeline collections: @airbnb and @vrbo

import pymongo

client = pymongo.MongoClient('localhost', 27017) # call the server

# Part 1: Read in JSON formatted data from two Mongo DB collections (@Airbnb and @Vrbo)
# Tweets have been collected using the run_twitter_simple_search_save.py and the TweetAuth.py programs
# This component returns Tweets with from user timeline query collected & stored in the MongoDB server

#Airbnb
db1 = client.airbnbtimeline #define a term for the @Airbnb db
dbcoll1 = db1.airbnbs #define a term for the @Airbnb db collection

#VRBO
db2 = client.vrbotimeline #define a term for the @Vrbo db
dbcoll2 = db2.vrbos #define a term for the @Vrbo db collection


# Find Tweets that are in English and convert them from JSON structures into a standard python list
#Airbnb
tweets_airbnb=dbcoll1.find() #search through  the @Airbnb db collection
for tweet in tweets_airbnb:
   if tweet['lang'] == 'en': # return Tweets in English only
      tweetlist_airbnb = [tweet for tweet in tweets_airbnb]
#VRBO
tweets_vrbo=dbcoll2.find() #define a term for the @Vrbo db collection
for tweet in tweets_vrbo:
   if tweet['lang'] == 'en':
      tweetlist_vrbo = [tweet for tweet in tweets_vrbo]

# Define a function that will print the 1st Tweet in a collection
def print_tweet_data(tweets):
   for tweet in tweets:
         print('User:', tweet['user']['name'])
         print('Message:', tweet['text'])
         print('Hashtags:', [hashtag['text'] for hashtag in tweet['entities']['hashtags']] )
         print('Number of retweets:', tweet['retweet_count'])
         if not tweet['place'] is None:
            print('Place:', tweet['place']['full_name'])

#print the first Tweet in each collection
print('Example tweet from the Airbnb Collection:')
print('Total Tweets in collection', len(tweetlist_airbnb))
print_tweet_data(tweetlist_airbnb[:1])
print()
print('Example tweet from the VRBO Collection:')
print('Total Tweets in collection', len(tweetlist_vrbo))
print_tweet_data(tweetlist_vrbo[:1])
print()



# Part 2: Count total number of retweets in each timeline collection
countretweetsAirbnb = 0
for tweet in tweetlist_airbnb: #sort through the @airbnb timeline collection to find retweet info
   if int(tweet['retweet_count']) > 1:
      countretweetsAirbnb += 1 #count total number of retweets
#print(countretweetsAirbnb)

countretweetsVrbo = 0
for tweet in tweetlist_vrbo: #sort through the @vrbo timeline collection to find retweet info
   if int(tweet['retweet_count']) > 1:
      countretweetsVrbo += 1 #count total number of retweets
#print(countretweetsVrbo)



# Part 3: Export retweet information to a csv file
import csv
outfile = "4-1compareRetweets.csv" #Name of output csv file
with open(outfile, 'w', newline='') as csvfileout:
   retweetWriter = csv.writer(csvfileout, delimiter=',', quoting=csv.QUOTE_MINIMAL) #define the row writer
   retweetWriter.writerow(['Timeline Collection', 'Total number of retweets'])
   retweetWriter.writerow(['@Airbnb', countretweetsAirbnb]) #information on Airbnb
   retweetWriter.writerow(['@Vrbo', countretweetsVrbo]) #information on Vrbo
   retweetWriter.writerow(['for a collection of 1999 Tweets from the @Airbnb timeline collection & 1999 Tweets from the @Vrbo timeline'])
csvfileout.close()

