# Aurelia Arnett
# create a database to JSON / semi-structured data

import pymongo
import json
from bson.json_util import dumps


# This function either starts or adds to an existing database and collection in Mongo
# Parameters:  
#   DBname - the name of the database, either new or existing
#   DBcollection - the name of the collection, either new or existing

def save_to_DB (DBname, DBcollection, data):
    client = pymongo.MongoClient('localhost', 27017) # connect to database server
    # save the results in a database collection
    DBname = DBname.lower() # remove case sensitivity by changing names to lowercase
    DBname = DBname.replace('#', '') # remove special characters
    DBname = DBname.replace(' ', '') # remove special characters
    DBcollection = DBcollection.lower()
    DBcollection = DBcollection.replace('#', '')
    DBcollection = DBcollection.replace(' ', '')

    # use the DBname and collection, which will create if not existing
    db = client[DBname]
    collection = db[DBcollection]   
        
    # add the data to the database
    collection.insert_many(data)
    print("Saved", len(data), "documents to DB collection", DBname, DBcollection)

# Extract data from an existing DB and collection
# Parameters:  
#   DBname and DBcollection- the name of the database and collection, either new or existing
# Result:
#   data - returns all the data in the collection as a list of JSON objects

def load_from_DB (DBname, DBcollection):
    # connect to database server and just let connection errors fail the program
    client = pymongo.MongoClient('localhost', 27017)
    # use the DBname and collection, which will create if not existing
    db = client[DBname]
    collection = db[DBcollection]    
        
    # get all the data from the collection as a cursor
    docs = collection.find()
    #  convert the cursor to a list
    docs_bson = list(docs)
    docs_json_str = [dumps(doc) for doc in docs_bson]
    docs_json = [json.loads(doc) for doc in docs_json_str]
    return docs_json
