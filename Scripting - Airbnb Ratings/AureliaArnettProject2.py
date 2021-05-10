# Aurelia Arnett
# Final Project - Question 2, part 1
# Airbnb Dataset - Untructured
# Purpose: To read in the Kaggle Dataset, process the data into dictionaries, and determine amenities included wtih high ratings


# Load in the data
import csv

# Read in the data
airbnbData = 'airbnbRatings.csv'

airbnbList = [] # create a list of Airbnbs

# convert spreadsheet to readable file
with open(airbnbData, 'r', encoding='cp1252', errors='ignore') as csvfile:
   airbnbReader = csv.reader(csvfile, dialect='excel')

# Data Processing
# Create a dictionary containing Airbnb data & clean out blanks, NAs, or typos
   for line in airbnbReader:
      if line[0] =='' or line[0].startswith('Listing'):
         continue
      else:
         airbnb = {}
         airbnb['ID'] = line[0]
         airbnb['Name'] = line[1]
         airbnb['HostID'] = line[2]
         airbnb['HostName'] = line[3]

         if line[4] =='' or line[4].startswith('N'): # remove row if the host response rate is blank or NA
            continue
         else: 
            airbnb['HostResponseRate'] = line[4]

         airbnb['Superhost'] = line[5]
         airbnb['HostTotalListings'] = line[6]
         airbnb['Street'] = line[7]
         airbnb['City'] = line[8]
         airbnb['Neighborhood'] = line[9]
         airbnb['State'] = line[10]

         if line[11] == '':
            continue
         else:
            airbnb['Country'] = line[11]

         airbnb['latitude'] = line[12]
         airbnb['longitude'] = line[13]
         airbnb['PropertyType'] = line[14]
         airbnb['RoomType'] = line[15]
         airbnb['Accommodates'] = line[16]

         # remove blank bathrooms & bedrooms (little data = little value)
         if line[17] == '':
            continue
         else:
            airbnb['Bathrooms'] = line[17]

         if line[18] == '':
            continue
         else:
            airbnb['Bedrooms'] = line[18]

         airbnb['Amenities'] = line[19]

         if line[20] == '': # Airbnb's that don't list a price may not be valuable 
            continue
         else:
            airbnb['Price'] = line[20]

         airbnb['MinStay'] = line[21]
         airbnb['MaxStay'] = line[22]
         airbnb['Availability'] = line[23]
         airbnb['LastScraped'] = line[24]
         airbnb['NumberOfReviews'] = line[25]

	 # remove all rows that do not have ratings
         if line[26] == '':
            continue
         else:
            airbnb['LastReviewDate'] = line[26]

         if line[27] == '':
            continue
         else:
            airbnb['OverallRating'] = line[27]

         if line[28] == '':
            continue
         else:
            airbnb['AccuracyRating'] = line[28]

         if line[29] == '':
            continue
         else:
            airbnb['CleanlinessRating'] = line[29]

         if line[30] == '':
            continue
         else:
            airbnb['CheckinRating'] = line[30]

         if line[31] == '':
            continue
         else:
            airbnb['CommunicationRating'] = line[31]

         if line[32] == '':
            continue
         else:
            airbnb['LocationRating'] = line[32]

         if line[33] == '':
            continue
         else:
            airbnb['ValueRating'] = line[33]

         if line[34] == '':
            continue
         else:
            airbnb['ReviewsPerMonth'] = line[34]

         airbnbList.append(airbnb)

csvfile.close()


# Addressing Question 2: What types of amenities are included for listings with overall ratings over 90%?
print('Question 2: What types of amenities are included for listings with overall ratings over 90%?')

import nltk
# Turn the message into tokens
# NOTE: Used the code $ python -c "import nltk; nltk.download('punkt')" in a cmd prompt to install the nltk package

# Over 90% score
# Tokenize amenities for listings that have an overall rating over 90%
# Create a list that contains the amenities/listing

amenitylist90 = [airbnb['Amenities'].replace(" ", "") for airbnb in airbnbList if int(airbnb['OverallRating']) >= 90]
print('Total number of listings with amenities:', len(amenitylist90))
alltok_90 = [tok for amenity in amenitylist90 for tok in nltk.word_tokenize(amenity)]
alltok_90_2 = [tok.lower() for tok in alltok_90]

amenityFD = nltk.FreqDist(alltok_90_2)
top_words = amenityFD.most_common(32)

amenityFreqList = []
#print('Amenity, Frequency, % Occurrence')
for word, freq in top_words:
   occ = round(100*(freq/len(amenitylist90)))
   amenitydict = {}
   amenitydict['Amenity'] = word
   amenitydict['Frequency'] = freq
   amenitydict['Occurrence'] = occ
   amenityFreqList.append((word,freq,occ))
#   print(word, freq, occ)


import pandas as pd
amenityFreqDF = pd.DataFrame(amenityFreqList, columns=['Amenity', 'Frequency', '% Occurrence'])
amenityFreqDF = amenityFreqDF.drop([0, 16])
amenityFreqDF = amenityFreqDF.set_index('Amenity')
print(amenityFreqDF)
amenityFreqDF.to_csv('2-AmenitiesOver90.csv')













