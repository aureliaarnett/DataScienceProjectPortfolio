# Aurelia Arnett
# Final Project - Question 1
# Airbnb Dataset - Structured
# Purpose: To read in the Kaggle Dataset, process the data into dictionaries, and determine ratings by country
# Then find the countries that have the highest & lowest scores, and uncover what factors are associated with high vs low scores


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

# Initial Data Discovery
print('Data Discovery:')
print("Read in", len(airbnbList), "rows of Airbnb listings with credible information") # how many reviews total?

countSuperhosts = 0 # determine total superhosts in dataset
for airbnb in airbnbList:
   if airbnb['Superhost'] == 'TRUE':
      countSuperhosts += 1
print("Total superhosts in dataset:", countSuperhosts)
print()
entireHome = 0
sharedRoom = 0
privateRoom = 0

for airbnb in airbnbList:
   if airbnb['RoomType'] == 'Entire home/apt':
      entireHome += 1
   elif airbnb['RoomType'] == 'Shared room':
      sharedRoom += 1
   elif airbnb['RoomType'] == 'Private room':
      privateRoom += 1

# Average overall rating per room type (Entire home, shared room, private room)
entireHomeRate = 0
sharedRoomRate = 0
privateRoomRate = 0

for airbnb in airbnbList:
   if airbnb['RoomType'] == 'Entire home/apt':
      entireHomeRate += int(airbnb['OverallRating'])
   elif airbnb['RoomType'] == 'Shared room':
      sharedRoomRate += int(airbnb['OverallRating'])
   elif airbnb['RoomType'] == 'Private room':
      privateRoomRate += int(airbnb['OverallRating'])

print('There are', entireHome, 'listings of entire  homes with an average overall rating of ' + ("%.2f" %(entireHomeRate/entireHome)) + '%')
print('There are', privateRoom, 'listings of private rooms with an average overall rating of ' + ("%.2f" %(sharedRoomRate/sharedRoom)) + '%')
print('There are', sharedRoom, '  listings of shared  rooms with an average overall rating of ' + ("%.2f" %(privateRoomRate/privateRoom)) + '%')
print('**Conclusion: Listings that are entire homes have the highest overall rating, followed by shared rooms then private rooms')
print()


# Average number of bathrooms for overall reviews over 90%
count90 = 0
countBathrooms90 = 0
count90Accommodates = 0

countUnder50 = 0
countBathroomsUnder50 = 0
countAccommodatesUnder50 = 0

for airbnb in airbnbList:
   if int(airbnb['OverallRating']) >= 90:
      count90 += 1 # count reviews with an overall rating of 90% or above
      bathrooms = float(airbnb['Bathrooms'])
      countBathrooms90 += bathrooms # count bathrooms of listings with an overall rating of 90% or above
      accommodates = float(airbnb['Accommodates'])
      count90Accommodates += accommodates # count # listing accommodates of listings with an overall rating of 90% or above
   elif int(airbnb['OverallRating']) <= 50:
      countUnder50 += 1
      bathrooms = float(airbnb['Bathrooms'])
      countBathroomsUnder50 += bathrooms
      accommodates = float(airbnb['Accommodates'])
      countAccommodatesUnder50 += accommodates

print('Airbnbs with an overall rating over  90% have on average', ("%.2f" %(countBathrooms90/count90)), 'bathrooms and accommodate', (round(count90Accommodates/count90)), 'people')
print('Airbnbs with an overall rating under 50% have on average', ("%.2f" %(countBathroomsUnder50/countUnder50)), 'bathrooms and accommodate', (round(countAccommodatesUnder50/countUnder50)), 'people')
print('**Conclusion: bathrooms and bedrooms seem to be consistent and have no impact impact on rating')
#print('    Could test different degrees of ratings with these variables to confirm')
print()


# Average communication review for superhosts
superhostCommunication = 0
superhostOverall = 0

nonsuperhost = 0
nonsuperhostCommunication = 0
nonsuperhostOverall = 0

for airbnb in airbnbList:
   if airbnb['Superhost'] == 'TRUE':
      superhostCommunication += int(airbnb['CommunicationRating'])
      superhostOverall += int(airbnb['OverallRating'])
   elif airbnb['Superhost'] == 'FALSE':
      nonsuperhost += 1
      nonsuperhostCommunication += int(airbnb['CommunicationRating'])
      nonsuperhostOverall += int(airbnb['OverallRating'])

print('Superhosts have an average communication rating of ' + ("%.2f" %((superhostCommunication/countSuperhosts))) + '/10 and an average overall rating of ' + ("%.2f" %(superhostOverall/countSuperhosts)) + '%')
print('Non-superhosts have an average communication rating of ' + ("%.2f" %((nonsuperhostCommunication/nonsuperhost))) + '/10 and an average overall rating of ' + ("%.2f" %(nonsuperhostOverall/nonsuperhost)) + '%')
print('**Conclusion: Superhosts have a higher communication rating and overall rating on average than non-superhosts')
print()
print()


# Addressing Question 1: Do patterns exists for Airbnb’s with high ratings and with low ratings among regions?
print('Question 1: Do patterns exists for Airbnb’s with high ratings and with low ratings among regions?')
# Average location review per country (22 countries)
# Define the variables: one to count total airbnbs/country and one to calculate the total overall rating/country
countAustralia = 0
overallAustralia = 0
countAustria = 0
overallAustria = 0
countBelgium = 0
overallBelgium = 0
countCanada = 0
overallCanada = 0
countChina = 0
overallChina = 0
# No rating information for the UK -> this country can be excluded
countDenmark = 0
overallDenmark = 0
countFrance = 0
overallFrance = 0
countGermany = 0
overallGermany = 0
countGreece = 0
overallGreece = 0
countHK = 0 #Hong Kong
overallHK = 0
countIreland = 0
overallIreland = 0
countItaly = 0
overallItaly = 0
countMexico = 0
overallMexico = 0
countNetherlands = 0
overallNetherlands = 0
countSpain= 0
overallSpain = 0
countSwitzerland = 0
overallSwitzerland = 0
# No rating information for the UK -> this country can be excluded
countUS = 0 # United States
overallUS = 0
# No rating information for Vanuatu -> this country can be excluded
# No rating information for Vatican City -> this country can be excluded

# Determine Airbnb's by country and extract their overall rating
for airbnb in airbnbList:
   if airbnb['Country'] == 'Australia':
      countAustralia += 1
      overallAustralia += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Austria':
     countAustria += 1
     overallAustria += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Belgium':
     countBelgium += 1
     overallBelgium += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Canada':
     countCanada += 1
     overallCanada += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'China':
     countChina += 1
     overallChina += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Denmark':
     countDenmark += 1
     overallDenmark += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'France':
     countFrance += 1
     overallFrance += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Germany':
     countGermany += 1
     overallGermany += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Greece':
     countGreece += 1
     overallGreece += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Hong Kong':
     countHK += 1
     overallHK += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Ireland':
     countIreland += 1
     overallIreland += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Italy':
     countItaly += 1
     overallItaly += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Mexico':
     countMexico += 1
     overallMexico += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Netherlands':
     countNetherlands += 1
     overallNetherlands += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Spain':
     countSpain += 1
     overallSpain += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'Switzerland':
     countSwitzerland += 1
     overallSwitzerland += int(airbnb['OverallRating'])
   elif airbnb['Country'] == 'United States':
     countUS += 1
     overallUS += int(airbnb['OverallRating'])

# Print the total number of Airbnb's by country and calculate the average overall rating of that country
print('There is no rating information for airbnbs in Cuba, the UK, Uruguay, Vanuatu, or Vatican City so those countries have been omitted')
print('There are', countAustralia, ' airbnbs in Australia   with an average overall rating of', ("%.2f" %(overallAustralia/countAustralia)) + '%')
print('There are', countAustria, '  airbnbs in Austria     with an average overall rating of', ("%.2f" %(overallAustria/countAustria)) + '%')
print('There are', countBelgium, '  airbnbs in Belgium     with an average overall rating of', ("%.2f" %(overallBelgium/countBelgium)) + '%')
print('There are', countCanada, ' airbnbs in Canada      with an average overall rating of', ("%.2f" %(overallCanada/countCanada)) + '%')
print('There are', countChina, '    airbnbs in China       with an average overall rating of', ("%.2f" %(overallChina/countChina)) + '%')
print('There are', countDenmark, '  airbnbs in Denmark     with an average overall rating of', ("%.2f" %(overallDenmark/countDenmark)) + '%')
print('There are', countFrance, ' airbnbs in France      with an average overall rating of', ("%.2f" %(overallFrance/countFrance)) + '%')
print('There are', countGermany, ' airbnbs in Germany     with an average overall rating of', ("%.2f" %(overallGermany/countGermany)) + '%')
print('There are', countGreece, '  airbnbs in Greece      with an average overall rating of', ("%.2f" %(overallGreece/countGreece)) + '%')
print('There are', countHK, '  airbnbs in Hong Kong   with an average overall rating of', ("%.2f" %(overallHK/countHK)) + '%')
print('There are', countIreland, '  airbnbs in Ireland     with an average overall rating of', ("%.2f" %(overallIreland/countIreland)) + '%')
print('There are', countItaly, ' airbnbs in Italy       with an average overall rating of', ("%.2f" %(overallItaly/countItaly)) + '%')
print('There are', countMexico, '     airbnbs in Mexico      with an average overall rating of', ("%.2f" %(overallMexico/countMexico)) + '%')
print('There are', countNetherlands, ' airbnbs in Netherlands with an average overall rating of', ("%.2f" %(overallNetherlands/countNetherlands)) + '%')
print('There are', countSpain, ' airbnbs in Spain       with an average overall rating of', ("%.2f" %(overallSpain/countSpain)) + '%')
print('There are', countSwitzerland, '  airbnbs in Switzerland with an average overall rating of', ("%.2f" %(overallSwitzerland/countSwitzerland)) + '%')
print('There are', countUS, 'airbnbs in the US      with an average overall rating of', ("%.2f" %(overallUS/countUS)) + '%')
#print('Rule out countries with very few airbnb listings: China, Mexico, Switzerland')
print()
print('Conclusion(s) on how to proceed:')
print('1. Evaluate the US on its own due to the +100,000 total listings')
#print('Countries with a total number of listings within the same range: Australia, Canada, France, Germany, Italy, Netherlands, and Spain')

# For the top 5 & bottom 5 ratings, create a term to keep track of average overall rating:
# Top 5
netherlandsOverall = ("%.2f" %(overallNetherlands/countNetherlands))
denmarkOverall = ("%.2f" %(overallDenmark/countDenmark))
greeceOverall = ("%.2f" %(overallGreece/countGreece))
australiaOverall = ("%.2f" %(overallAustralia/countAustralia))
canadaOverall = ("%.2f" %(overallCanada/countCanada))

# Bottom 5
hkOverall = ("%.2f" %(overallHK/countHK))
spainOverall = ("%.2f" %(overallSpain/countSpain))
switzerlandOverall = ("%.2f" %(overallSwitzerland/countSwitzerland))
italyOverall = ("%.2f" %(overallItaly/countItaly))
belgiumOverall = ("%.2f" %(overallBelgium/countBelgium))

print('2. Evaluate the 5 countries with the highest overall ratings:')
print('   Netherlands (' + netherlandsOverall + '%), Denmark (' + denmarkOverall + '%), Greece  (' + greeceOverall + '%), Canada (' + canadaOverall + '%), Australia (' + australiaOverall + '%)')
print('3. Evaluate the 5 countries with the lowest  overall ratings:')
print('   Hong Kong (' + hkOverall + '%), Spain (' + spainOverall + '%), Switzerland (' + switzerlandOverall + '%), Italy (' + italyOverall + '%), Belgium (' + belgiumOverall + '%)')
print()


# Evaluate influencing factors of listings by region, based on countries with the top and bottom ratings
# Demonstrate understanding of writing functions by creating multiple definitions that can be applied to each country ^

# Define a function that calculates the percentage of superhosts / country
def calcSuperhost(country):
   countCountry = 0
   countCountrySuperhosts = 0
   for airbnb in airbnbList:
      if airbnb['Country'] == country:
         countCountry += 1
         if airbnb['Superhost'] == 'TRUE':
            countCountrySuperhosts += 1
   return (round(100*(countCountrySuperhosts/countCountry)))
#print('% Airbnb hosts in the Netherlands that are superhosts: ' + calcSuperhost('Netherlands') + '%')


# Define a function that calculates the average communication rating for of superhosts by country
def calcCommunicationRatingS(country):
   countCountry = 0
   countCountryCommunicationS = 0
   for airbnb in airbnbList:
      if airbnb['Country'] == country:
         if airbnb['Superhost'] == 'TRUE':
            countCountry += 1
            countCountryCommunicationS += int(airbnb['CommunicationRating'])
   return ("%.2f" %(countCountryCommunicationS/countCountry))
#print('Average communication rating of superhosts in the Netherlands: ' + calcCommunicationRatingS('Netherlands') + '/10')


# Define a function that calculates the average communication rating for of non-superhosts by country
def calcCommunicationRatingN(country):
   countCountry = 0
   countCountryCommunicationN = 0
   for airbnb in airbnbList:
      if airbnb['Country'] == country:
         if airbnb['Superhost'] == 'FALSE':
            countCountry += 1
            countCountryCommunicationN += int(airbnb['CommunicationRating'])
   return ("%.2f" %(countCountryCommunicationN/countCountry))
#print('Average communication rating of non-superhosts in the Netherlands: ' + calcCommunicationRatingN('Netherlands') + '/10')


# Define a function that calculates the average communication rating by country
def calcCommunicationRating(country):
   countCountry = 0
   countCountryCommunication = 0
   for airbnb in airbnbList:
      if airbnb['Country'] == country:
         countCountry += 1
         countCountryCommunication += int(airbnb['CommunicationRating'])
   return ("%.2f" %(countCountryCommunication/countCountry))
#print('Average communication rating of non-superhosts in the Netherlands: ' + calcCommunicationRatingN('Netherlands') + '/10')


# Define a function that calculates the % of listings that are 'Entire home' by country
def calcEntHome(country):
   countCountry = 0
   countEntHome = 0
   for airbnb in airbnbList:
      if airbnb['Country'] == country:
         countCountry += 1
         if airbnb['RoomType'] == 'Entire home/apt':
            countEntHome += 1
   return (round(100*(countEntHome/countCountry)))
#print("Total listings as  Entire Home in The Netherlands:", calcEntHome('Netherlands'))


# Define a function that calculates the % of listings that are 'Private room' by country
def calcPrivRoom(country):
   countCountry = 0
   countPrivRoom = 0
   for airbnb in airbnbList:
      if airbnb['Country'] == country:
         countCountry += 1
         if airbnb['RoomType'] == 'Private room':
            countPrivRoom += 1
   return (round(100*(countPrivRoom/countCountry)))
#print("Total listings as Private Room in The Netherlands:", calcPrivRoom('Netherlands'))


# Define a function that calculates the % of listings that are 'Shared room' by country
def calcShareRoom(country):
   countCountry = 0
   countShareRoom = 0
   for airbnb in airbnbList:
      if airbnb['Country'] == country:
         countCountry += 1
         if airbnb['RoomType'] == 'Shared room':
            countShareRoom += 1
   return (round(100*(countShareRoom/countCountry)))
#print("Total listings as Shared Room  in The Netherlands:", calcShareRoom('Netherlands'))


# Define a function that calculates the average number of bathrooms for listings by country
def calcBathrooms(country):
   countCountry = 0
   countBathrooms = 0
   for airbnb in airbnbList:
      bathrooms = float(airbnb['Bathrooms'])
      if airbnb['Country'] == country:
         countCountry += 1.0
         countBathrooms += int(bathrooms)
   return ("%.2f" %(countBathrooms/countCountry))
#print("The average number of bathrooms:", calcBathrooms('Netherlands'))


# Define a function that calculates the average number of bedrooms for listings by country
def calcBedrooms(country):
   countCountry = 0
   countBedrooms = 0
   for airbnb in airbnbList:
      bedrooms = float(airbnb['Bedrooms'])
      if airbnb['Country'] == country:
         countCountry += 1.0
         countBedrooms += int(bedrooms)
   return (round(countBedrooms/countCountry))
#print("The average number of bedrooms of listings in The Netherlands:", calcBedrooms('Netherlands'))


# Define a function that calculates the average number of accommodations for listings by country
def calcAcc(country):
   countCountry = 0
   countAcc = 0
   for airbnb in airbnbList:
      acc = float(airbnb['Accommodates'])
      if airbnb['Country'] == country:
         countCountry += 1.0
         countAcc += int(acc)
   return (round(countAcc/countCountry))
#print("The average number of accommodations for listings in The Netherlands accommodates:", calcAcc('Netherlands'))


# Define a function that calculates the average price for listings by country
def calcPrice(country):
   countCountry = 0
   countPrice = 0
   for airbnb in airbnbList:
      acc = float(airbnb['Price'])
      if airbnb['Country'] == country:
         countCountry += 1.0
         countPrice += int(acc)
   return ("%.2f" %(countPrice/countCountry))
#print("The average price/night for listings in The Netherlands: $" + calcPrice('Netherlands'))


# Define a function that calculates the average value rating for listings by country
def calcValueRating(country):
   countCountry = 0
   countCountryValue = 0
   for airbnb in airbnbList:
      if airbnb['Country'] == country:
         countCountry += 1
         countCountryValue += int(airbnb['ValueRating'])
   return ("%.2f" %(countCountryValue/countCountry))
#print("Average value rating of Airbnb's in The Netherlands: " + calcValueRating('Netherlands') + "/10")

def countCountry(country):
   countCountry = 0
   for airbnb in airbnbList:
      if airbnb['Country'] == country:
         countCountry += 1
   return (countCountry)


def calcOverallRating(country):
   countCountry = 0
   countCountryRating = 0
   for airbnb in airbnbList:
      if airbnb['Country'] == country:
         countCountry += 1
         countCountryRating += int(airbnb['OverallRating'])
   return ("%.2f" %(countCountryRating/countCountry))



def createDict(country):
   countryList = []
   countryInfo = {}
   countryInfo['Country'] = country
#   countryInfo['TotalListings'] = countCountry(country)
   countryInfo['AvOverallRating'] = calcOverallRating(country)
   countryInfo['%Superhosts'] = calcSuperhost(country)
#   countryInfo['AvCommRatingSuperhosts'] = calcCommunicationRatingS(country)
#   countryInfo['AvCommRatingNonsuperhosts'] = calcCommunicationRatingN(country)
   countryInfo['AvCommRating'] = calcCommunicationRating(country)
   countryInfo['%EntireHome'] = calcEntHome(country)
   countryInfo['%PrivateRoom'] = calcPrivRoom(country)
   countryInfo['%SharedRoom'] = calcShareRoom(country)
   countryInfo['AvNumBathrooms'] = calcBathrooms(country)
   countryInfo['AvNumBedrooms'] = calcBedrooms(country)
   countryInfo['AvNumAccommodations'] = calcAcc(country)
   countryInfo['AvPrice'] = calcPrice(country)
   countryInfo['AvValueRating'] = calcValueRating(country)
   countryList.append(countryInfo)
   return countryList

# US
US = createDict('United States')

# Top 5 Countries
Netherlands = createDict('Netherlands') #type = list
Denmark = createDict('Denmark')
Greece = createDict('Greece')
Canada = createDict('Canada')
Australia = createDict('Australia')

# Bottom 5 Countries
HongKong = createDict('Hong Kong')
Spain = createDict('Spain')
Switzerland = createDict('Switzerland')
Italy = createDict('Italy')
Belgium = createDict('Belgium')


# Create pandas dataframes to compare overall ratings per country
import pandas as pd

# Create a dataframe to show information regarding the top 5 countries
print('US Factors')
USdf = pd.DataFrame(US)
USdf = USdf.set_index('Country')
print(USdf)
print()
USdf.to_csv('1-US-Factors.csv')

# Create a dataframe to show information regarding the top 5 countries
print('Top 5 Countries')
topFiveDF = pd.DataFrame(Netherlands)
# columns=['Country', 'Total Listings', 'Average Overall Rating', 'Number of Superhosts', 'Average Superhost Communication Rating', 'Average Non-superhost Communication Rating', 'Number of Entire Homes', 'Number of Private Rooms', 'Number of Shared Rooms', 'Average Number of Bathrooms', 'Average Number of Bedrooms', 'Average Number of Accommodations', 'Average Price', 'Average Value Rating']
topFiveDF = topFiveDF.append(Denmark)
topFiveDF = topFiveDF.append(Greece)
topFiveDF = topFiveDF.append(Canada)
topFiveDF = topFiveDF.append(Australia)
topFiveDF = topFiveDF.set_index('Country')
print(topFiveDF)
print()
topFiveDF.to_csv('1-topFiveCountries.csv')

# Create a dataframe to show information regarding the bottom 5 countries
print('Bottom 5 Countries')
bottomFiveDF = pd.DataFrame(HongKong)
bottomFiveDF = bottomFiveDF.append(Spain)
bottomFiveDF = bottomFiveDF.append(Switzerland)
bottomFiveDF = bottomFiveDF.append(Italy)
bottomFiveDF = bottomFiveDF.append(Belgium)
bottomFiveDF = bottomFiveDF.set_index('Country')
print(bottomFiveDF)
bottomFiveDF.to_csv('1-bottomFiveCountries.csv')

