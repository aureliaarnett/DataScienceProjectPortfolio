# Aurelia Arnett
# Purpose: To load Tweets from database collections stored in MongoDB server & initial data discovery

import pymongo

client = pymongo.MongoClient('localhost', 27017) # call the server

# Part 1: Read JSON formatted data from a Mongo DB collection
# Tweets have been collected using the run_twitter_simple_search_save.py and the TweetAuth.py programs
# This component reads in Tweets from hashtags collections

#Airbnb
db1 = client.airbnb
dbcoll1 = db1.airbnbs

#VRBO
db2 = client.vrbo
dbcoll2 = db2.vrbos

#travel
db3 = client.travel
dbcoll3 = db3.travels

#adventure
db4 = client.adventure
dbcoll4 = db4.adventures

#waderlust
db5 = client.wander
dbcoll5 = db5.wanderlust



# Find Tweets that are in English and convert them from JSON structures into a standard python list
# Airbnb
tweets_airbnb=dbcoll1.find()
for tweet in tweets_airbnb:
   if tweet['lang'] == 'en': # return Tweets in English only
      tweetlist_airbnb = [tweet for tweet in tweets_airbnb]

#VRBO
tweets_vrbo=dbcoll2.find()
for tweet in tweets_vrbo:
   if tweet['lang'] == 'en':
      tweetlist_vrbo = [tweet for tweet in tweets_vrbo]

#travel
tweets_travel=dbcoll3.find()
for tweet in tweets_travel:
   if tweet['lang'] == 'en':
      tweetlist_travel = [tweet for tweet in tweets_travel]

#adventure
tweets_adventure=dbcoll4.find()
for tweet in tweets_adventure:
   if tweet['lang'] == 'en':
      tweetlist_adventure = [tweet for tweet in tweets_adventure]

#wanderlust
tweets_wanderlust=dbcoll5.find()
for tweet in tweets_wanderlust:
   if tweet['lang'] == 'en':
      tweetlist_wanderlust = [tweet for tweet in tweets_wanderlust]


# Print one Tweet unprocessed from the original db for data discovery
#print(tweetlist_airbnb[:1]) 

# Format Tweet in readable form
def print_tweet_data(tweets):
   for tweet in tweets:
         print('Date:', tweet['created_at'])
         print('User:', tweet['user']['name'])
         print('User Location:', tweet['user']['location'])
         print('Message:', tweet['text'])
         print('Hashtags:', tweet['entities']['hashtags'] )
         print('Number of retweets:', tweet['retweet_count'])
         print('Number of favorites:', tweet['favorite_count'])
         if not tweet['place'] is None:
            print('Place:', tweet['place']['full_name'])

#print first Tweet
print('Airbnb Collection with collection length', len(tweetlist_airbnb))
print_tweet_data(tweetlist_airbnb[:1])
print()

print('VRBO Collection with collection length', len(tweetlist_vrbo))
print_tweet_data(tweetlist_vrbo[:1])
print()

print('Travel Collection with collection length', len(tweetlist_travel))
print_tweet_data(tweetlist_travel[:1])
print()

print('Adventure Collection with collection length', len(tweetlist_adventure))
print_tweet_data(tweetlist_adventure[:1])
print()

print('Wanderlust Collection with collection length', len(tweetlist_wanderlust))
print_tweet_data(tweetlist_adventure[:1])
print()


# Discovery: it appears 'travel' and 'adventure' come up in many hashtags
# We also see there are a few pieces of information:
#   date & time in form as 'created_at'
#   Tweet message in form as 'text'
#   unable to return hashtags or location
#   username can be generated from 'user': 'name'
#   hashtag information is 'entities': 'hashtags'




