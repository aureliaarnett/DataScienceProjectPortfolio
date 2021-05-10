# Aurelia Arnett
# Purpose: To collect Tweets from the Twitter.com developer server and store them as JSON structured data in a MongoDB server
# Note that the program calls to the TweetAuth program for user authentication 
# Usage:  python run_twitter_simple_search_save.py <query> <number> <DBname> <DBcollection> 
# This program also uses the create_database program to load data from the Mongo DB server and the save_to_DB program to store data


import tweepy #import tweepy function and collect data
import json #returns data as JSNO formatted tweets
import sys #import functions that will process hashtag data as inputed by the user to call the DB, DBcollection, quantity, and file name
from TweetAuth import oauth_login #check for user authentication
from TweetAuth import appauth_login #confirm user authentication
from create_database import save_to_DB #save data to a file


# using the Tweepy function, search for the requested query as inputed by the user and return tweets as JSON structures
def simple_search(api, query, max_results=20):
  search_results = [status for status in tweepy.Cursor(api.search, q=query).items(max_results)] # search for tweets in the Twitter.com server
  tweets = [tweet._json for tweet in search_results] # represent tweets as JSON
  return tweets

# process user input
if __name__ == '__main__':
    
    #make a list of command line arguments 
    args = sys.argv[1:] #omit the [0] element (the python file name)

    #check to ensure right input data
    if not args or len(args) < 4:
        print('usage: python twitter_simple_search.py <query> <num tweets> <DB name> <collection name>')
        sys.exit(1)

    query = args[0] #User will select the mongodb database
    num_tweets = int(args[1]) #User will select the db collection from the mongodb database
    DBname = args[2] #User will select number of top hashtag terms
    DBcollection = args[3] #User will select the output csv file name

    api = appauth_login() #ensure authorization 
    print ("Twitter Authorization: ", api)
    
    result_tweets = simple_search(api, query, max_results=num_tweets) #search for tweets in desired collection
    print ('Number of result tweets: ', len(result_tweets))

    # save the results in a database collection
    DBname = DBname.lower() # remove case sensitivity to tag terms such as #Airbnb with #airbnb with #AiRbNb
    DBname = DBname.replace('#', '') # remove special characters like hashtags and spaces (other special characters may also be forbidden)
    DBname = DBname.replace(' ', '')
    DBcollection = DBcollection.lower() # remove case sensitivity to tag terms such as #Airbnb with #airbnb with #AiRbNb
    DBcollection = DBcollection.replace('#', '') # remove special characters like hashtags and spaces (other special characters may also be forbidden)
    DBcollection = DBcollection.replace(' ', '')
    
    # save tweet collection to MongoDB server
    save_to_DB(DBname, DBcollection, result_tweets)
  

