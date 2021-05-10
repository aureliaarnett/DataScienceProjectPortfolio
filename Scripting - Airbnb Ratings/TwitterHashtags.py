# Aurelia Arnett
# Purpose: To process a collection of Tweets from the Mongo DB server and return the top frequency hashtags to a csv file
# Note that Tweets have been collected using the run_twitter_simple_search_save.py and the TweetAuth.py programs
# This program also uses the create_database program to load data from the Mongo DB server
# Step 1: Connect to the mongod server in a separate command prompt
# Usage:  python uncoverHashtags.py <DBname> <DBcollection> <number> <filename>


import sys #import functions that will process hashtag data as inputed by the user to call the DB, DBcollection, quantity, and file name
from operator import itemgetter #import functions to fetch hashtag data from the DB collection
from create_database import load_from_DB #import & load data stored in the MongoDB server
import pandas as pd #create a pandas DF for csv output



# create a function that takes in a Tweet (as a Twitter JSON object) and returns the hashtags
def get_entities(tweet):
    if 'entities' in tweet.keys(): #check to ensure data is a Tweet
        hashtags = [hashtag['text'] for hashtag in tweet['entities']['hashtags']] #define the hashtags term
        return hashtags
    else: #return empty lists if no hashtags in Tweet
        return []

hashtagList=[] #Create an empty list that will later contain hashtags to export into a csv

# Obtain command line arguments (input by user)
if __name__ == '__main__':

    #make a list of command line arguments 
    args = sys.argv[1:] #omit the [0] element (the python file name)

    if not args or len(args) < 4: #user needs to input 4 names in addition to the python file name
        print('usage: python uncoverHashtags.py <DBname> <DBcollection> <number> <filepath>')
        sys.exit(1) #exit prompt

    # Define terms to align to user prompts
    DBname = args[0] #User will select the mongodb database
    DBcollection = args[1] #User will select the db collection from the mongodb database
    limit = int(args[2]) #User will select number of top hashtag terms
    outfile = args[3] #User will select the output csv file name

    # load all the tweets using functions stored in load_from_DB file
    tweet_results = load_from_DB(DBname, DBcollection)

    # Create a dictionary to store top hashtags & their frequencies
    hashtag_fd = {}

    # Create a function that will check for tweets in English and count hashtag frequencies
    for tweet in tweet_results:

        if tweet['lang'] == 'en': # check for hashtags in English only
        # Use the get_entities function to extract hashtags & count their frequencies
            
            hashtags = get_entities(tweet)
            for tag in hashtags:
               tag = tag.lower() # remove case sensitivity to tag terms such as #Airbnb with #airbnb with #AiRbNb
               if not tag in hashtag_fd: # if hashtag term comes up for the first time, count it once
                  hashtag_fd[tag] = 1
               else: # if term exists already, add 1 to the count that is already there
                  hashtag_fd[tag] += 1 

    # Create a sorted dictionary containing a list of pairs of hashtag terms and frequencies
    hashtags_sorted = sorted(hashtag_fd.items(), key=itemgetter(1), reverse=True)

    # print out the top number of hashtag terms with their frequencies
    print("Top", limit, "Frequency Hashtags")
    for (word, frequency) in hashtags_sorted[:limit]: #search for hashtags in the sorted dictionary
        hashtagdict = {} #create a blank hashtag dictionary
        hashtagdict['Word']=word #store the hashtag term in the new dictionary
        hashtagdict['Frequency']=frequency #pair the hashtag term frequency with the term in the new dictionary
        hashtagList.append((word, frequency)) #append the dictionary terms in the blank list that was created prior
        print (word, frequency) #print top hashtags and their frequencies


    # create a pandas df that can read to a csv file
    hashtagDF = pd.DataFrame(hashtagList, columns=['Hashtag', 'Frequency'])
    hashtagDF = hashtagDF.set_index('Hashtag')
#    print(hashtagDF) #check the pandas df to ensure it looks right
    hashtagDF.to_csv(outfile) #print pandas df, which contains hashtag terms and frequencies, to a csv output file





