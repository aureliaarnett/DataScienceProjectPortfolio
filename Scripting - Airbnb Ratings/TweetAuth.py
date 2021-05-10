# Aurelia Arnett
# Purpose: Write a program that collects Tweets
# Create a new dbs in MongoDB and create the collection
# Extract Tweets from Twitter using the app
# Store Tweets into the collection

import pymongo
import json
import tweepy #enable API to authorize with Twitter


# Store special access keys from dev Twitter account
CONSUMER_KEY = 'WWeaaWM3yyfuYJFNw49iEJKZo'
CONSUMER_SECRET = 'X6oJmSYrSR7e5FRgRO88deH4viKQaKqIHSeLQYLbAbVzvcKGTZ'
OAUTH_TOKEN = '1067998645507678210-xJ3IYigYAEDOjcL2xHer45fPuWGPLV'
OAUTH_SECRET = 'HJExpDhXWimGVNnUvXsCX6pbqEvNNSG9rTe10MRCXoewt'

# Define a function that checks your authorization with twitter, validates the connection, and stores in the Tweepy package:
# ordinary rate limiting
def oauth_login():
  auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET) #validate permissions with Twitter
  auth.set_access_token(OAUTH_TOKEN,OAUTH_SECRET) #validate permissions with Twitter
  tweepy_api = tweepy.API(auth) #run the API from tweepy

  if (not tweepy_api): #check for errors
      print ("Problem Connecting to API with OAuth")

  # otherwise return API that allows access for the Tweepy enabled functions
  return tweepy_api


# extended rate limiting
def appauth_login():
  auth = tweepy.AppAuthHandler(CONSUMER_KEY,CONSUMER_SECRET) #validate permissions with Twitter, no OAUTH necessary
  tweepy_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

  if (not tweepy_api): #check for errors
      print ("Problem Connecting to API with AppAuth")

  # otherwise return API that allows access for the Tweepy enabled functions
  return tweepy_api


# check: successful connection?
if __name__ == '__main__':
  tweepy_api = oauth_login()
  print ("Twitter OAuthorization: ", tweepy_api)
  tweepy_api = appauth_login()
  print ("Twitter AppAuthorization: ", tweepy_api)


# Connect to mongo client & create a server host - to manually create a db from scratch / the program run_twitter_simple_search_save.py will also create dbs automatically
#client = pymongo.MongoClient('localhost', 27017)
#db = client.tweet_db # Create a database to store collection Tweets
#tweet_collection = db.tweet_collection # Define a pass within python
#tweet_collection.create_index([("id", pymongo.ASCENDING)], unique=True)




