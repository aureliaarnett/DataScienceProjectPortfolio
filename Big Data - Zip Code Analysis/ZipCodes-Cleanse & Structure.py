# Aurelia Arnett
# Objective: Demonstrate ability to develop models for forecasting average median housing value using zip codes.
# Case: Can we predict which three zip codes provide the best investment opportunity for the Syracuse Real Estate Investment Trust


##### PHASE 1: OBTAIN & SCRUB DATA, DATA DISCOVERY, & DATA PRE-PROCESSING #####
# Method 1 of reading dataset in:
# Import function to call in the Coaches dataset
import csv
# Function to process dataset into a pandas dictionary for data cleansing
import pandas as pd
import numpy as np

# Read in data & preprocess for calculations
zipcodes = 'Zip_Zhvi_SingleFamilyResidence.csv'

# convert data in csv to pandas dataframe that you can float variables to convert later
zipcodeList = [] # Create a list to store column variables

with open(zipcodes, mode='r') as csvfile: # open the csv file into the program
   zipcodeReader = csv.reader(csvfile, dialect='excel')

# Represent the data as a list dictionaries
   for line in zipcodeReader:
      if line[0].startswith('Region'): #skip first row containing column titles
         continue
      else:
         zipcode = {}
         zipcode['ZipCode'] = line[2] 
         zipcode['SizeRank'] = line[1] 
         zipcode['State'] = line[4] 
         zipcode['City'] = line[6] 
         zipcode['Metro'] = line[7] 
         zipcode['County'] = line[8]
         zipcodeList.append(zipcode)
csvfile.close()


# Convert list into pandas dataframe
zipcodeData1 = pd.DataFrame(zipcodeList)
#print('Table containing Zip Code data') # attempted to bin the data by year
#print(zipcodeData1[0:5])
#print()

# Method 2 of reading dataset in:
zipcodeData = pd.read_csv('Zip_Zhvi_SingleFamilyResidence.csv', header=0) # Convert entire dataset to pandas dataframe & use this as starting point
zipcodeData = zipcodeData.drop(['RegionID', 'SizeRank', 'RegionType', 'StateName'], axis=1) # Remove unwanted columns (not necessary for modeling)
#print(zipcodeData.columns)

# Review data to ensure it's properly called in:
#print('Table containing Zip Code data') #index data frame by zip code
print('Zip Code Data')
print(zipcodeData[0:5])
print('Len dataset:', len(zipcodeData)) # 30464 zip codes
print()




##### PHASE 2: Initial Analysis 
##### P2.a: Create a time series for AR metros
from matplotlib import pyplot

# Hot Springs, Little Rock, Fayetteville, Searcy:
# Create a dataset containing just Hot Springs data:
HotSprings = zipcodeData[zipcodeData.Metro == 'Hot Springs']
#print('Hot Springs Data:')
#print(HotSprings)
# Create a transposed dataset to build time a series model:
HotSpringsT = HotSprings.drop(['Metro','City', 'State','CountyName'], axis=1)
HotSpringsT = pd.DataFrame(HotSpringsT).set_index('RegionName').rename_axis('Date', axis=1)
HotSpringsT = HotSpringsT.transpose()
#print('Hot Springs Transpose:')
#print(HotSpringsT)
#print()
# Build dataset containing the mean housing value of the Hot Springs area:
HotSprings2 = pd.DataFrame(HotSpringsT)
rowHS = HotSprings2.loc[:,:]
HotSprings2["Hot Springs"] = rowHS.mean(axis=1)
#print('Hot Springs Data with mean:')
#print(HotSprings2)
#print()
HotSpringsMean = pd.DataFrame(HotSprings2["Hot Springs"])
#print('Hot Springs mean of area:')
#print(HotSpringsMean)

# Create a dataset containing just Little Rock data to ammend:
LittleRock = zipcodeData[zipcodeData.Metro == 'Little Rock-North Little Rock-Conway']
# Create a transposed dataset to build a time series model:
LittleRockT = LittleRock.drop(['Metro','City', 'State','CountyName'], axis=1)
LittleRockT = pd.DataFrame(LittleRockT).set_index('RegionName').rename_axis('Date', axis=1)
LittleRockT = LittleRockT.transpose()
LittleRock2 = pd.DataFrame(LittleRockT)
rowLR = LittleRock2.loc[:,:]
LittleRock2["Little Rock"] = rowLR.mean(axis=1)
LittleRockMean = pd.DataFrame(LittleRock2["Little Rock"])

# Create a dataset containing just Fayetteville data:
ARFayetteville = zipcodeData[zipcodeData.Metro == 'Fayetteville-Springdale-Rogers']
# Create a transposed dataset to build a time series model:
ARFayettevilleT = ARFayetteville.drop(['Metro','City', 'State','CountyName'], axis=1)
ARFayettevilleT = pd.DataFrame(ARFayettevilleT).set_index('RegionName').rename_axis('Date', axis=1)
ARFayettevilleT = ARFayettevilleT.transpose()
ARFayetteville2 = pd.DataFrame(ARFayettevilleT)
rowF = ARFayetteville2.loc[:,:]
ARFayetteville2["Fayetteville"] = rowF.mean(axis=1)
ARFayettevilleMean = pd.DataFrame(ARFayetteville2["Fayetteville"])

# Create a dataset containing just Searcy data:
Searcy = zipcodeData[zipcodeData.Metro == 'Searcy']
# Create a transposed dataset to build a time series model:
SearcyT = Searcy.drop(['Metro','City', 'State','CountyName'], axis=1)
SearcyT = pd.DataFrame(SearcyT).set_index('RegionName').rename_axis('Date', axis=1)
SearcyT = SearcyT.transpose()
Searcy2 = pd.DataFrame(SearcyT)
rowS = Searcy2.loc[:,:]
Searcy2["Searcy"] = rowS.mean(axis=1)
SearcyMean = pd.DataFrame(Searcy2["Searcy"])

ARmetro = pd.DataFrame(HotSpringsMean)
ARmetro['Little Rock'] = LittleRockMean['Little Rock']
ARmetro['Fayetteville'] = ARFayettevilleMean['Fayetteville']
ARmetro['Searcy'] = SearcyMean['Searcy']
print('Initial Analysis: Dataset containing AR metro areas')
print(ARmetro)
#ARmetro.plot().set(title="Time Series for AR Metro Areas", xlabel="Year", ylabel="Mean Housing Value")
#pyplot.show()



##### PHASE 3: PROPHET MODELING
import warnings
import numpy
from fbprophet import Prophet
import matplotlib.pyplot as plt

### TRANSPOSE ZIP CODES DATA ### > This dataset will be the 'final' dataset to collect information for
# Note: to perform the sliding window method, must change the size of the train and test set after testing (train on past 5, 10, 2, years)
import datetime
zipcodeDataT = zipcodeData.drop(['Metro','City', 'State','CountyName'], axis=1) 
zipcodeDataT = pd.DataFrame(zipcodeDataT).set_index('RegionName').rename_axis('Date', axis=1)
zipcodeDataT = zipcodeDataT.transpose()
zipcodeDataT.index = pd.to_datetime(zipcodeDataT.index)
#print('Zip Code Data (transposed)')
#print(zipcodeDataT)
#print()


#### P3.1: Test that the code works - build a subset model for testing
# FIRST: Let's use the AR metros dataset
arMetroEnumerate = []
zipNames = []

for i, zip in enumerate(ARmetro.columns):
    arMetroEnumerate.append(ARmetro.loc[ARmetro.loc[:,zip].first_valid_index():,zip]) # add only from first valid index
    arMetroEnumerate[i] = arMetroEnumerate[i].to_frame()
    arMetroEnumerate[i].name = zip
    zipcode = {}
    zipcode['Zip Code'] = zip
    zipNames.append(zipcode)
    arMetroEnumerate[i]['ds'] = arMetroEnumerate[i].index
    arMetroEnumerate[i].rename(columns={zip: 'y'}, inplace=True)
#    print(zip) #check to see if zip code names are saved

zipNamesDF = pd.DataFrame(zipNames)
#print(zipNamesDF)

#print(arMetroEnumerate[0].name) #data returns properly
#print(arMetroEnumerate) # View dataset of datasets

# SCRUB - BUILD TRAIN & TEST SETS:
arMetroTrain = []
arMetroTest  = []

for df in arMetroEnumerate:
   arMetroTrain.append(df[217:-13]) # represents housing value from Feb '14 - Feb '19 (5 years prior)
   arMetroTest.append(df[-13:])  # represents housing value from the last 13 months (Mar '19 - Mar '20)

#print('Train Set for AR Metros:')
#print(arMetroTrain[0])
#print('Test Set for AR Metros')
#print(arMetroTest[0][['y']])


# CREATE PREDICTION DF
#currentDT = datetime.datetime.now()
#print(currentDT.strftime("%Y-%m-%d %H:%M:%S"))
warnings.filterwarnings('ignore')

predsAR = []
yhatAR = []
errormetricAR = [] #difference in the range
rmseAR = []
yactAR = []


def rmse(predictions, targets):
    differences = predictions - targets                       #the DIFFERENCEs.
    differences_squared = differences ** 2                    #the SQUAREs of ^
    mean_of_differences_squared = differences_squared.mean()  #the MEAN of ^
    rmse_val = np.sqrt(mean_of_differences_squared)           #ROOT of ^
    return rmse_val   


j = 0
#for i, df in enumerate(arMetroTrain):
#    # bring in test set to compare y actual:
#    yactual = pd.DataFrame(arMetroTest[j])
#    yactAR.append(yactual['y'].tolist())
#    yactARDF = pd.DataFrame(yactAR)
#    yactARDF = yactARDF.transpose()

#    # model data based on the train dataset
#    model = Prophet(interval_width=0.95, weekly_seasonality=True, daily_seasonality=True)
#    model.fit(df)
#    pred_value = model.make_future_dataframe(periods=13, freq='MS') # Future predictions
#    forecast = model.predict(pred_value)
#    forecast2 = pd.DataFrame((forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-13:]))
#    forecast2['error'] = forecast2['yhat_upper']-forecast2['yhat_lower']
#    forecast2['y_actual'] = yactARDF[j].values
#    forecast2['y_pred'] = forecast2['yhat']
#    forecast2['rmse'] = rmse(forecast2['yhat'],forecast2['y_actual'])
#    forecast2.name = zipNamesDF.loc[i:i].values # name the df the zip code
#    print(arMetroTest[j]) # Verify y actual is correct
#    print(forecast2)
#    j += 1

    # save values: error metric, RMSE, y pred
#    errormetricAR.append(forecast2['error'].tolist()) # store the error term   
#    rmseAR.append(forecast2['rmse'].tolist())
#    yhatAR.append(forecast2['yhat'].tolist()) # store yhat (pred value) & compare to arMetroTest

#    model.plot(forecast2,uncertainty=True)
#    pyplot.show()
#    print(pred_value)
#    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-13:])
#    print(forecast[-13:])
#    print(type(forecast)) #type pd df
#    predsAR.append(forecast2)

#print()
#print('RMSE:')
#rmseDF = pd.DataFrame(rmseAR)
#print(rmseDF[0])
#rmseDF = rmseDF.rename(columns = lambda x: 'x')
#rmseDFT = pd.DataFrame(rmseDF.transpose())
#rmseDFT = rmseDFT.rename(columns = lambda x: 'y')
#for i in rmseDFT:
#   rmseDF.rename(index = lambda x: zipNamesDF.loc[i:i].values) 
#    rmseDFT[i].rename(columns={'y': zipNamesDF.loc[i:i].values}, inplace=True)

#print()
#print('Error in model:')
#print(errormetricAR)
#errorDF = pd.DataFrame(errormetricAR)
#if len(errorDF) == len(zipNames):
#   errorDF.index = zipNames
#errorDF = errorDF.transpose()
#print(errorDF)
#errorDF.plot().set(title="Error in model", xlabel="Month", ylabel="Error")
#pyplot.show()
# SAVE DATA IN CSV FILE:
#errorDF.to_csv('ARError.csv')

#print()
#print('y actual')
#yactARDF = pd.DataFrame(yactAR)
#yactARDF = yactARDF.transpose()
#yactARDF.columns = ["Hot Springs","Little Rock","Fayetteville","Searcy"]
#print(yactARDF)

#print()
#yhatDF = pd.DataFrame(yhatAR)
#yhatDF = yhatDF.transpose()
#yhatDF.columns = ["Hot Springs pred","Little Rock pred","Fayetteville pred","Searcy pred"]
#print('y predicted:')
#print(yhatDF)





#### P3.2: Build Prophet models based on location - Seattle
#### Build the dataset(s)
print()
SeattleZips = zipcodeData[zipcodeData.CountyName == 'King County']
#print('Zip Codes based in King County (WA)')
#print('Number of zip codes in King County:', len(SeattleZips)) # 78
SeattleZips = SeattleZips.drop(['State', 'City', 'Metro', 'CountyName'], axis=1)
#print(SeattleZips)
SeattleZips = SeattleZips.drop([26793])

SeattleZipsLowError = pd.DataFrame(SeattleZips.loc[12639,:])
SeattleZipsLowError.columns = ['98047']
SeattleZipsLowError['98002'] = SeattleZips.loc[2525,:]
SeattleZipsLowError['98092'] = SeattleZips.loc[1581,:]
SeattleZipsLowError['98188'] = SeattleZips.loc[4906,:]
SeattleZipsLowError['98003'] = SeattleZips.loc[957,:]
#print(SeattleZipsLowError)


#SeattleZips = pd.DataFrame(SeattleZips).set_index('RegionName').rename_axis('Date', axis=1)
#SeattleZips = SeattleZips.transpose()
#SeattleZips.index = pd.to_datetime(SeattleZips.index)
#print(SeattleZips)

#### Build train/test set
seattleEnumerate = []
seattlezipNames = []

for i, zip in enumerate(SeattleZips.columns):
    seattleEnumerate.append(SeattleZips.loc[SeattleZips.loc[:,zip].first_valid_index():,zip]) # add only from first valid index
    seattleEnumerate[i] = seattleEnumerate[i].to_frame()
    seattleEnumerate[i].name = zip
    zipcode = {}
    zipcode['Zip Code'] = zip
    seattlezipNames.append(zipcode)
    seattleEnumerate[i]['ds'] = seattleEnumerate[i].index
    seattleEnumerate[i].rename(columns={zip: 'y'}, inplace=True)

seattlezipNamesDF = pd.DataFrame(seattlezipNames)
#print(zipNamesDF)

#print(seattleEnumerate[0].name) #data returns properly
#print(seattleEnumerate) # View dataset of datasets

# SCRUB - BUILD TRAIN & TEST SETS:
seattleTrain10 = []
seattleTrain5 = []
seattleTest  = []

for df in seattleEnumerate:
   seattleTrain10.append(df[157:-13]) # represents housing value from Feb '09 - Feb '19 (10 years data)
   seattleTrain5.append(df[217:-13])  # represents housing value from Feb '14 - Feb '19 (5 years data)
   seattleTest.append(df[-13:])       # represents housing value from the last 13 months (Mar '19 - Mar '20)

#print('Train Set for King County (10 yrs):')
#print(seattleTrain10[0])
#print()
#print('Train Set for King County (5 yrs):')
#print(seattleTrain5[0])
#print()
#print('Test Set for King Count')
#print(seattleTest[0])


#### CREATE PREDICTION DF
predsSEA = []
yhatSEA = []
errormetricSEA = [] #difference in the range
rmseSEA = []
yactSEA = []

#for i, df in enumerate(seattleTrain10):
    # bring in test set to compare y actual:
#    yactual = pd.DataFrame(seattleTest[j])
#    yactSEA.append(yactual['y'].tolist())
#    yactSEADF = pd.DataFrame(yactSEA)
#    yactSEADF = yactSEADF.transpose()

    # model data based on the train dataset
#    model = Prophet(interval_width=0.95, weekly_seasonality=True, daily_seasonality=True)
#    model.fit(df)
#    pred_value = model.make_future_dataframe(periods=65, freq='MS') # Future predictions (13 mo for 1 yr & 65 mo for 5 yr)
#    forecast = model.predict(pred_value)
#    forecast2 = pd.DataFrame((forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-65:]))
#    forecast2['error'] = forecast2['yhat_upper']-forecast2['yhat_lower']
#    forecast2['y_actual'] = yactSEADF[j].values
#    forecast2['y_pred'] = forecast2['yhat']
#    forecast2['rmse'] = rmse(forecast2['yhat'],forecast2['y_actual'])
#    print(seattleTest[j]) # Verify y actual is correct
#    print(forecast2)
#    j += 1

    # save values: error metric, RMSE, y pred
#    errormetricSEA.append(forecast2['error'].tolist()) # store the error term   
#    rmseSEA.append(forecast2['rmse'].tolist())
#    yhatSEA.append(forecast2['yhat'].tolist()) # store yhat (pred value) & compare to seattleTest

#    model.plot(forecast2,uncertainty=True)
#    pyplot.show()
#    predsSEA.append(forecast2)

SEAindex = seattlezipNames

#print()
#print('RMSE for King County:')
#rmseDF = pd.DataFrame(rmseSEA)
#if len(rmseDF) == len(SEAindex):
#   rmse.index = SEAindex
#print(rmseDF)
# SAVE DATA IN CSV FILE:
#rmseDF.to_csv('KingCountyRMSE5Yr.csv')


#print()
#print('Error in model:')
#errorDF = pd.DataFrame(errormetricSEA)
#if len(errorDF) == len(SEAindex):
#   errorDF.index = SEAindex
#row = errorDF.loc[:,:]
#errorDF['MeanError'] = row.mean(axis=1)
#errorDF = errorDF.nsmallest(5, 'MeanError')
#errorDF = errorDF.transpose()
#print(errorDF)
# SAVE DATA IN CSV FILE:
#errorDF.to_csv('KingCountyError5Yr.csv')

# Plot error over time for King County Zips with the lowest average error:
#riskToGrowthDF = pd.DataFrame(errorDF.transpose())
#riskToGrowthDF = riskToGrowthDF.drop(['MeanError'], axis=1)
#riskToGrowthDF = riskToGrowthDF.transpose()
#riskToGrowthDF.plot().set(title="Error in model for zip codes in King County where the model had the lowest error", xlabel="Month", ylabel="Error")
#pyplot.show()

#print()
#print('y predicted:')
yhatDF = pd.DataFrame(yhatSEA)
if len(yhatDF) == len(SEAindex):
   yhatDF.index = SEAindex
#yhatDF = yhatDF.transpose()
#print(yhatDF)
# SAVE DATA IN CSV FILE:
#yhatDF.to_csv('KingCountyYHat5Yr.csv')

#print()
#print('y actual')
#yactSEADF = pd.DataFrame(yactSEA)
#yactSEADF = yactSEADF.transpose()
#print(yactSEADF)



### BUILD PREDICTION MODEL GRAPHIC FOR ZIPS WITH LOWEST ERROR (1 yr forecast):
#print(SeattleZipsLowError)
#### Build train/test set
seattleEnumerate2 = []
seattlezipNames2 = []

for i, zip in enumerate(SeattleZipsLowError.columns):
    seattleEnumerate2.append(SeattleZipsLowError.loc[SeattleZipsLowError.loc[:,zip].first_valid_index():,zip]) # add only from first valid index
    seattleEnumerate2[i] = seattleEnumerate2[i].to_frame()
    seattleEnumerate2[i].name = zip
    zipcode = {}
    zipcode['Zip Code'] = zip
    seattlezipNames2.append(zipcode)
    seattleEnumerate2[i]['ds'] = seattleEnumerate2[i].index
    seattleEnumerate2[i].rename(columns={zip: 'y'}, inplace=True)

seattlezipNamesDF2 = pd.DataFrame(seattlezipNames2)
#print(zipNamesDF)

#print(seattleEnumerate2[0].name) #data returns properly
#print(seattleEnumerate2) # View dataset of datasets

# SCRUB - BUILD TRAIN & TEST SETS:
seattleTrain10 = []
seattleTrain5 = []
seattleTest  = []

for df in seattleEnumerate2:
   seattleTrain10.append(df[157:-13]) # represents housing value from Feb '09 - Feb '19 (10 years data)
   seattleTrain5.append(df[217:-13])  # represents housing value from Feb '14 - Feb '19 (5 years data)
   seattleTest.append(df[-13:])       # represents housing value from the last 13 months (Mar '19 - Mar '20)

#### CREATE PREDICTION DF
predsSEA2 = []
yhatSEA2 = []
errormetricSEA2 = [] #difference in the range
rmseSEA2 = []
yactSEA2 = []

#for i, df in enumerate(seattleTrain10):
#    # bring in test set to compare y actual:
#    yactual = pd.DataFrame(seattleTest[j])
#    yactSEA2.append(yactual['y'].tolist())
#    yactSEADF2 = pd.DataFrame(yactSEA2)
#    yactSEADF2 = yactSEADF2.transpose()

    # model data based on the train dataset
#    model = Prophet(interval_width=0.95, weekly_seasonality=True, daily_seasonality=True)
#    model.fit(df)
#    pred_value = model.make_future_dataframe(periods=13, freq='MS') # Future predictions
#    forecast = model.predict(pred_value)
#    forecast2 = pd.DataFrame((forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-13:]))
#    forecast2['error'] = forecast2['yhat_upper']-forecast2['yhat_lower']
#    forecast2['y_actual'] = yactSEADF2[j].values
#    forecast2['y_pred'] = forecast2['yhat']
#    forecast2['rmse'] = rmse(forecast2['yhat'],forecast2['y_actual'])
#    print(seattleTest[j]) # Verify y actual is correct
#    print(forecast2)
#    j += 1

    # save values: error metric, RMSE, y pred
#    errormetricSEA.append(forecast2['error'].tolist()) # store the error term   
#    rmseSEA2.append(forecast2['rmse'].tolist())
#    yhatSEA2.append(forecast2['yhat'].tolist()) # store yhat (pred value) & compare to seattleTest

#    model.plot(forecast2,uncertainty=True)
#    pyplot.show()
#    predsSEA.append(forecast2)

#print()
#print('RMSE for King County:')
#rmseDF = pd.DataFrame(rmseSEA2)
#print(rmseDF)

#print()
#print('y predicted:')
#yhatDF = pd.DataFrame(yhatSEA2)
#yhatDF = yhatDF.transpose()
#yhatDF.columns = ["98047","98002","98092","98188","98003"]
#print(yhatDF)
#yhatDF.plot().set(title="Forecast for zip codes in King County where the model had the lowest error", xlabel="Month", ylabel="Forecast")
#pyplot.show()







### BUILD PREDICTION MODEL GRAPHIC FOR ZIPS WITH LOWEST ERROR (5 yr forecast):
#index: 28, 16, 55, 31, 70
#print(SeattleZips)
SeattleZipsLowError2 = pd.DataFrame(SeattleZips.loc[2583,:])
SeattleZipsLowError2.columns = ['98031']
SeattleZipsLowError2['98092'] = SeattleZips.loc[1581,:]
SeattleZipsLowError2['98022'] = SeattleZips.loc[5305,:]
SeattleZipsLowError2['98188'] = SeattleZips.loc[4906,:]
SeattleZipsLowError2['98047'] = SeattleZips.loc[12639,:]
#print(SeattleZipsLowError2)


#### Build train/test set
seattleEnumerate3 = []
seattlezipNames3 = []

for i, zip in enumerate(SeattleZipsLowError2.columns):
    seattleEnumerate3.append(SeattleZipsLowError2.loc[SeattleZipsLowError2.loc[:,zip].first_valid_index():,zip]) # add only from first valid index
    seattleEnumerate3[i] = seattleEnumerate3[i].to_frame()
    seattleEnumerate3[i].name = zip
    zipcode = {}
    zipcode['Zip Code'] = zip
    seattlezipNames3.append(zipcode)
    seattleEnumerate3[i]['ds'] = seattleEnumerate3[i].index
    seattleEnumerate3[i].rename(columns={zip: 'y'}, inplace=True)

seattlezipNamesDF3 = pd.DataFrame(seattlezipNames3)
#print(zipNamesDF)

#print(seattleEnumerate3[0].name) #data returns properly
#print(seattleEnumerate3) # View dataset of datasets

# SCRUB - BUILD TRAIN & TEST SETS:
seattleTrain10 = []
seattleTest  = []

for df in seattleEnumerate3:
   seattleTrain10.append(df[157:-13]) # represents housing value from Feb '09 - Feb '19 (10 years data)
   seattleTest.append(df[-13:])       # represents housing value from the last 13 months (Mar '19 - Mar '20)

#### CREATE PREDICTION DF
predsSEA3 = []
yhatSEA3 = []
errormetricSEA3 = [] #difference in the range
rmseSEA3 = []
yactSEA3 = []

#for i, df in enumerate(seattleTrain10):
    # bring in test set to compare y actual:
#    yactual = pd.DataFrame(seattleTest[j])
#    yactSEA3.append(yactual['y'].tolist())
#    yactSEADF3 = pd.DataFrame(yactSEA3)
#    yactSEADF3 = yactSEADF3.transpose()

    # model data based on the train dataset
#    model = Prophet(interval_width=0.95, weekly_seasonality=True, daily_seasonality=True)
#    model.fit(df)
#    pred_value = model.make_future_dataframe(periods=65, freq='MS') # Future predictions
#    forecast = model.predict(pred_value)
#    forecast2 = pd.DataFrame((forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-65:]))
#    forecast2['error'] = forecast2['yhat_upper']-forecast2['yhat_lower']
#    forecast2['y_actual'] = yactSEADF3[j].values
#    forecast2['y_pred'] = forecast2['yhat']
#    forecast2['rmse'] = rmse(forecast2['yhat'],forecast2['y_actual'])
#    print(seattleTest[j]) # Verify y actual is correct
#    print(forecast2)
#    j += 1

    # save values: error metric, RMSE, y pred
#    errormetricSEA3.append(forecast2['error'].tolist()) # store the error term   
#    rmseSEA3.append(forecast2['rmse'].tolist())
#    yhatSEA3.append(forecast2['yhat'].tolist()) # store yhat (pred value) & compare to seattleTest

#    model.plot(forecast2,uncertainty=True)
#    pyplot.show()
#    predsSEA.append(forecast2)

#print()
#print('Error in model:')
#errorDF = pd.DataFrame(errormetricSEA3)
#errorDF = errorDF.transpose()
#errorDF.columns = ["98031","98092","98022","98188","98047"]
#errorDF = errorDF.transpose()
#print(errorDF)

# Plot error over time for King County Zips with the lowest average error:
#errorDF.plot().set(title="Error in model for zip codes in King County where the model had the lowest error (5 yrs)", xlabel="Month", ylabel="Error")
#pyplot.show()

#print()
#print('y predicted:')
#yhatDF = pd.DataFrame(yhatSEA3)
#yhatDF = yhatDF.transpose()
#yhatDF.columns = ["98031","98092","98022","98188","98047"]
#yhatDF = yhatDF.transpose()
#print(yhatDF)
#yhatDF.plot().set(title="Forecast for zip codes in King County where the model had the lowest error (5 yrs)", xlabel="Month", ylabel="Forecast")
#pyplot.show()



#### SET UP TO RUN for all 30,000 zips ####
zipcodeData = pd.read_csv('zipsDel.csv', header=0) # Remove zips that have no data in Mar 2010
zipcodeData = zipcodeData.drop(['Metro','City', 'State', 'StateName', 'CountyName','RegionID', 'SizeRank', 'RegionType'], axis=1)
zipcodeDataT = pd.DataFrame(zipcodeData).set_index('RegionName').rename_axis('Date', axis=1)
zipcodeDataT = zipcodeDataT.transpose()
zipcodeDataT.index = pd.to_datetime(zipcodeDataT.index)
#print(zipcodeDataT)
zipcodeDataT = zipcodeDataT.transpose()
zipcodeDataT1 = (zipcodeDataT.iloc[0:5000]).transpose()
zipcodeDataT2 = (zipcodeDataT.iloc[5001:10001]).transpose()
zipcodeDataT3 = (zipcodeDataT.iloc[10002:15002]).transpose()
zipcodeDataT4 = (zipcodeDataT.iloc[20003:25003]).transpose()
zipcodeDataT5 = (zipcodeDataT.iloc[25004:26665]).transpose()

#   seattleTrain10.append(df[157:-13]) # represents housing value from Feb '09 - Feb '19 (10 years data)

#### Build train/test set
zipEnumerate = []
zipNames = []

#for i, zip in enumerate(zipcodeDataT5.columns):
#    zipEnumerate.append(zipcodeDataT5.loc[zipcodeDataT5.loc[:,zip].first_valid_index():,zip]) # add only from first valid index
#    # Note that this code will be reused each time and the training data frame will be updated for each run
#    zipEnumerate[i] = zipEnumerate[i].to_frame()
#    zipEnumerate[i].name = zip
#    zipcode = {}
#    zipcode['Zip Code'] = zip
#    zipNames.append(zipcode)
#    zipEnumerate[i]['ds'] = zipEnumerate[i].index
#    zipEnumerate[i].rename(columns={zip: 'y'}, inplace=True)

#zipNamesDF = pd.DataFrame(zipNames)
#print(zipNamesDF)

#print(zipEnumerate[0].name) #data returns properly
#print(zipEnumerate) # View dataset of datasets

# SCRUB - BUILD TRAIN & TEST SETS:
zipTrain10 = []
zipTest  = []

#for df in zipEnumerate:
#   zipTrain10.append(df[-121:]) # represents housing value from Mar '10 - Mar '20 (10 years data)
#   zipTest.append(df[-13:])       # represents housing value from the last 13 months (Mar '19 - Mar '20)

#print('Train Set (10 yr back):')
#print(zipTrain10[0])
#print()
#print('Test Set')
#print(zipTest[0])


#### CREATE PREDICTION DF
yhat = []
errormetric = [] #difference in the range

#for i, df in enumerate(zipTrain10):
#    # model data based on the train dataset
#    model = Prophet(interval_width=0.95, weekly_seasonality=True, daily_seasonality=True)
#    model.fit(df)
#    pred_value = model.make_future_dataframe(periods=120, freq='MS') # Future predictions (120 mo for 10 yr)
#    forecast = model.predict(pred_value)
#    forecast2 = pd.DataFrame((forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]))
#    forecast2['error'] = forecast2['yhat_upper']-forecast2['yhat_lower']
#    forecast2['y_pred'] = forecast2['yhat']
#    print(forecast2)

    # save values: error metric, RMSE, y pred
#    errormetric.append(forecast2['error'].tolist()) # store the error term   
#    yhat.append(forecast2['yhat'].tolist()) # store yhat (pred value) & compare to seattleTest

#    model.plot(forecast2,uncertainty=True)
#    pyplot.show()

#zipindex = zipNames

#print()
#print('Error in model:')
#errorDF = pd.DataFrame(errormetric)
#if len(errorDF) == len(zipindex):
#   errorDF.index = zipindex
#row = errorDF.loc[:,:]
#errorDF['MeanError'] = row.mean(axis=1)
#print(errorDF)
# SAVE DATA IN CSV FILE:
#errorDF.to_csv('ErrorZips5.csv')

#print()
#print('y predicted:')
#yhatDF = pd.DataFrame(yhat)
#if len(yhatDF) == len(zipindex):
#   yhatDF.index = zipindex
#print(yhatDF)
# SAVE DATA IN CSV FILE:
#yhatDF.to_csv('yPred5.csv')





### CALL IN NEW DATA ###
# APPEND THE ERROR DATA FRAMES #
errorzips1 = pd.read_csv('ErrorZips1.csv', header=0)
errorzips1 = errorzips1.drop(['MeanError'], axis=1)
errorzips1 = errorzips1.drop(errorzips1.iloc[:,1:122], axis=1)

errorzips2 = pd.read_csv('ErrorZips2.csv', header=0)
errorzips2 = errorzips2.drop(['MeanError'], axis=1)
errorzips2 = errorzips2.drop(errorzips2.iloc[:,1:122], axis=1)

errorzips3 = pd.read_csv('ErrorZips3.csv', header=0)
errorzips3 = errorzips3.drop(['MeanError'], axis=1)
errorzips3 = errorzips3.drop(errorzips3.iloc[:,1:122], axis=1)

errorzips4 = pd.read_csv('ErrorZips4.csv', header=0)
errorzips4 = errorzips4.drop(['MeanError'], axis=1)
errorzips4 = errorzips4.drop(errorzips4.iloc[:,1:122], axis=1)

errorzips5 = pd.read_csv('ErrorZips5.csv', header=0)
errorzips5 = errorzips5.drop(['MeanError'], axis=1)
errorzips5 = errorzips5.drop(errorzips5.iloc[:,1:122], axis=1)

errorzips = errorzips1.append(errorzips2)
errorzips = errorzips.append(errorzips3)
errorzips = errorzips.append(errorzips4)
errorzips = errorzips.append(errorzips5)
row = errorzips.loc[:,:]
errorzips['MeanError'] = row.mean(axis=1)
print('Dataset showing the error with time for a 10 year forecast for all zip codes:')
print(errorzips)
print()
smallesterrorzips = errorzips.nsmallest(5, columns="MeanError")
print('Zip codes with the smallest mean error over a 10 year forecast:')
print(smallesterrorzips)


# APPEND THE FORECAST DATA FRAMES #
forecastzips1 = pd.read_csv('yPred1.csv', header=0)
forecastzips1 = forecastzips1.drop(forecastzips1.iloc[:,1:122], axis=1) # Drop years (columns) associated with the prediction columns on training years

forecastzips2 = pd.read_csv('yPred2.csv', header=0)
forecastzips2 = forecastzips2.drop(forecastzips2.iloc[:,1:122], axis=1)

forecastzips3 = pd.read_csv('yPred3.csv', header=0)
forecastzips3 = forecastzips3.drop(forecastzips3.iloc[:,1:122], axis=1)

forecastzips4 = pd.read_csv('yPred4.csv', header=0)
forecastzips4 = forecastzips4.drop(forecastzips4.iloc[:,1:122], axis=1)

forecastzips5 = pd.read_csv('yPred5.csv', header=0)
forecastzips5 = forecastzips5.drop(forecastzips5.iloc[:,1:122], axis=1)

forecastzips = forecastzips1.append(forecastzips2)
forecastzips = forecastzips.append(forecastzips3)
forecastzips = forecastzips.append(forecastzips4)
forecastzips = forecastzips.append(forecastzips5)
print('Dataset showing the forecast over time for a 10 year forecast for all zip codes:')
print(forecastzips)
print()


# PLOT ERROR FOR LOWEST ERROR ZIPS #
smallesterrorzips = smallesterrorzips.drop(['MeanError'], axis=1)
smallesterrorzips = pd.DataFrame(smallesterrorzips.transpose())
smallesterrorzips.columns=['17976', '24726', '73438', '42032', '24606']
smallesterrorzips = pd.DataFrame(smallesterrorzips.transpose())
smallesterrorzips = smallesterrorzips.drop(smallesterrorzips.iloc[:,0:1], axis=1)
smallesterrorzips = pd.DataFrame(smallesterrorzips.transpose())
print('Zip codes with the lowest error:')
print(smallesterrorzips)
#smallesterrorzips.plot().set(title="5 zip codes with the lowest error for a 10 year forecast", xlabel="Month", ylabel="Error")
#pyplot.show()


#forecastsmallesterrorzips = pd.DataFrame(forecastzips)
#forecastsmallesterrorzips.to_csv('forecastsmallesterrorzips.csv') # find index

forecastsmallesterrorzips = pd.DataFrame(forecastzips.iloc[11283,:])
forecastsmallesterrorzips.columns = ['17976']
forecastsmallesterrorzips['24726'] = forecastzips.iloc[18502,:]
forecastsmallesterrorzips['73438'] = forecastzips.iloc[14642,:]
forecastsmallesterrorzips['42032'] = forecastzips.iloc[20363,:]
forecastsmallesterrorzips['24606'] = forecastzips.iloc[20012,:]

forecastsmallesterrorzips = forecastsmallesterrorzips.transpose()
forecastsmallesterrorzips = forecastsmallesterrorzips.drop(forecastsmallesterrorzips.iloc[:,0:1], axis=1)
forecastsmallesterrorzips = pd.DataFrame(forecastsmallesterrorzips.transpose())
print('Forecast of zips with the lowest error:')
print(forecastsmallesterrorzips)
#forecastsmallesterrorzips.plot().set(title="Forecast of zips with the lowest error", xlabel="Month", ylabel="Forecast")
#pyplot.show()




### Recommended zip codes ###
recommendZips = pd.DataFrame(smallesterrorzips).rename_axis('Zip Code', axis=1)
recommendZips = recommendZips.transpose()
row = recommendZips.loc[:,:]
recommendZips['MeanError'] = row.mean(axis=1)
recommendZips = recommendZips.drop(recommendZips.iloc[:,0:120], axis=1)


forecastsmallesterrorzips = forecastsmallesterrorzips.transpose()
forecastsmallesterrorzips['PredictedGrowthIn5Yrs'] = forecastsmallesterrorzips.iloc[:,59] - forecastsmallesterrorzips.iloc[:,0] #find the forecasted growth in 5 yrs
forecastsmallesterrorzips['PredictedGrowthIn10Yrs'] = forecastsmallesterrorzips.iloc[:,119] - forecastsmallesterrorzips.iloc[:,0] #find the forecasted growth in 10 yrs


recommendZips['PredictedGrowthIn5Yrs'] = forecastsmallesterrorzips['PredictedGrowthIn5Yrs']
recommendZips['PredictedGrowthIn10Yrs'] = forecastsmallesterrorzips['PredictedGrowthIn10Yrs']
recommendZips  = recommendZips.nsmallest(5, columns="MeanError")
print('Zip Codes Summary:')
print(recommendZips)













##### ARCHIVE CODE #####
import urllib.request
import json
import pymongo

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.zipsdb
collZips = db.zips

#errorDictAR = dict(errorDF.to_dict("records"))
#print(type(errorDictAR))
#collZips.insert_many({"index":"ARZips","data":errorDictAR})
#print()
#print('errorDict loaded into Mongo DB')
#print('Load errorDict to df:')
#dataFromDB = collZips.find({"index":"ARZips"})
#outputDF = pd.DataFrame(dataFromDB)
#print(outputDF)
