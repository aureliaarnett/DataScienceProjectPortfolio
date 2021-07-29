# Forecasting housing values by US zip code

## Table of contents
* [General info](#general-info)
* [Technologies used](#technologies-used)
* [Methods used](#methods-used)
* [Code example](#code-example)
* [Screenshots](#screenshots)
* [Contact](#contact)

## General info
> This project 

## Technologies used
* Anaconda (python)

## Methods used
* Python
* Pyplot
* Prophet modeling
* Timeseries analysis

## Code example
**Data Structuring** -- Extracting 4 zip codes in AR:\
#Create a dataset containing just Hot Springs data:\
HotSprings = zipcodeData[zipcodeData.Metro == 'Hot Springs']\
#print('Hot Springs Data:')\
#print(HotSprings)\
#Create a transposed dataset to build time a series model:\
HotSpringsT = HotSprings.drop(['Metro','City', 'State','CountyName'], axis=1)\
HotSpringsT = pd.DataFrame(HotSpringsT).set_index('RegionName').rename_axis('Date', axis=1)\
HotSpringsT = HotSpringsT.transpose()\
#print('Hot Springs Transpose:')\
#print(HotSpringsT)\
#Build dataset containing the mean housing value of the Hot Springs area:\
HotSprings2 = pd.DataFrame(HotSpringsT)\
rowHS = HotSprings2.loc[:,:]\
HotSprings2["Hot Springs"] = rowHS.mean(axis=1)\
#print('Hot Springs Data with mean:')\
#print(HotSprings2)\
#print()\
HotSpringsMean = pd.DataFrame(HotSprings2["Hot Springs"])\
#print('Hot Springs mean of area:')\
#print(HotSpringsMean)\
.\
.\
.\
#Consolidate 4 zip codes into 1 dataset\
ARmetro = pd.DataFrame(HotSpringsMean)\
ARmetro['Little Rock'] = LittleRockMean['Little Rock']\
ARmetro['Fayetteville'] = ARFayettevilleMean['Fayetteville']\
ARmetro['Searcy'] = SearcyMean['Searcy']\
print('Initial Analysis: Dataset containing AR metro areas')\
print(ARmetro)\
#ARmetro.plot().set(title="Time Series for AR Metro Areas", xlabel="Year", ylabel="Mean Housing Value")\
#pyplot.show()\
\
**Prophet modemling & time series analysis for zip codes in AR**\
**Note:** This was repeated for all zip codes in Seattle, WA and then on the dataset of all 15K zip codes\
import warnings\
import numpy\
from fbprophet import Prophet\
import matplotlib.pyplot as plt\
\
#TRANSPOSE ZIP CODES DATA> This dataset will be the 'final' dataset to collect information for\
#Note: to perform the sliding window method, must change the size of the train and test set after testing (train on past 5, 10, 2, years)\
import datetime\
zipcodeDataT = zipcodeData.drop(['Metro','City', 'State','CountyName'], axis=1) \
zipcodeDataT = pd.DataFrame(zipcodeDataT).set_index('RegionName').rename_axis('Date', axis=1)\
zipcodeDataT = zipcodeDataT.transpose()\
zipcodeDataT.index = pd.to_datetime(zipcodeDataT.index)\
#print('Zip Code Data (transposed)')\
#print(zipcodeDataT)\
#print()\
\
#Test that the code works - build a subset model for testing\
#FIRST: Let's use the AR metros dataset\
arMetroEnumerate = []\
zipNames = []\
\
for i, zip in enumerate(ARmetro.columns):\
    arMetroEnumerate.append(ARmetro.loc[ARmetro.loc[:,zip].first_valid_index():,zip]) # add only from first valid index\
    arMetroEnumerate[i] = arMetroEnumerate[i].to_frame()\
    arMetroEnumerate[i].name = zip\
    zipcode = {}\
    zipcode['Zip Code'] = zip\
    zipNames.append(zipcode)\
    arMetroEnumerate[i]['ds'] = arMetroEnumerate[i].index\
    arMetroEnumerate[i].rename(columns={zip: 'y'}, inplace=True)\
#print(zip) #check to see if zip code names are saved\
\
zipNamesDF = pd.DataFrame(zipNames)\
#print(zipNamesDF)\
\
#print(arMetroEnumerate[0].name) #data returns properly\
#print(arMetroEnumerate) # View dataset of datasets\
\
#SCRUB - BUILD TRAIN & TEST SETS:\
arMetroTrain = []\
arMetroTest  = []\
\
for df in arMetroEnumerate:\
   arMetroTrain.append(df[217:-13]) # represents housing value from Feb '14 - Feb '19 (5 years prior)\
   arMetroTest.append(df[-13:])  # represents housing value from the last 13 months (Mar '19 - Mar '20)\
\
#print('Train Set for AR Metros:')\
#print(arMetroTrain[0])\
#print('Test Set for AR Metros')\
#print(arMetroTest[0][['y']])\
\
#CREATE PREDICTION DF\
#currentDT = datetime.datetime.now()\
#print(currentDT.strftime("%Y-%m-%d %H:%M:%S"))\
warnings.filterwarnings('ignore')\
\
predsAR = []\
yhatAR = []\
errormetricAR = [] #difference in the range\
rmseAR = []\
yactAR = []\
\
def rmse(predictions, targets):\
    differences = predictions - targets                       #the DIFFERENCEs.\
    differences_squared = differences ** 2                    #the SQUAREs of ^\
    mean_of_differences_squared = differences_squared.mean()  #the MEAN of ^\
    rmse_val = np.sqrt(mean_of_differences_squared)           #ROOT of ^\
    return rmse_val   \
\
j = 0\
#for i, df in enumerate(arMetroTrain):\
#bring in test set to compare y actual:\
#yactual = pd.DataFrame(arMetroTest[j])\
#yactAR.append(yactual['y'].tolist())\
#yactARDF = pd.DataFrame(yactAR)\
#yactARDF = yactARDF.transpose()\
\
#model data based on the train dataset\
#model = Prophet(interval_width=0.95, weekly_seasonality=True, daily_seasonality=True)\
#model.fit(df)\
#pred_value = model.make_future_dataframe(periods=13, freq='MS') # Future predictions\
#forecast = model.predict(pred_value)\
#forecast2 = pd.DataFrame((forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-13:]))\
#forecast2['error'] = forecast2['yhat_upper']-forecast2['yhat_lower']\
#forecast2['y_actual'] = yactARDF[j].values\
#forecast2['y_pred'] = forecast2['yhat']\
#forecast2['rmse'] = rmse(forecast2['yhat'],forecast2['y_actual'])\
#forecast2.name = zipNamesDF.loc[i:i].values # name the df the zip code\
#print(arMetroTest[j]) # Verify y actual is correct\
#print(forecast2)\
#j += 1\
\
#save values: error metric, RMSE, y pred\
#errormetricAR.append(forecast2['error'].tolist()) # store the error term   \
#rmseAR.append(forecast2['rmse'].tolist())\
#yhatAR.append(forecast2['yhat'].tolist()) # store yhat (pred value) & compare to arMetroTest\
\
#model.plot(forecast2,uncertainty=True)\
#pyplot.show()\
#print(pred_value)\
#print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-13:])\
#print(forecast[-13:])\
#print(type(forecast)) #type pd df\
#predsAR.append(forecast2)\
\
#print()\
#print('RMSE:')\
#rmseDF = pd.DataFrame(rmseAR)\
#print(rmseDF[0])\
#rmseDF = rmseDF.rename(columns = lambda x: 'x')\
#rmseDFT = pd.DataFrame(rmseDF.transpose())\
#rmseDFT = rmseDFT.rename(columns = lambda x: 'y')\
#for i in rmseDFT:\
#rmseDF.rename(index = lambda x: zipNamesDF.loc[i:i].values) \
#rmseDFT[i].rename(columns={'y': zipNamesDF.loc[i:i].values}, inplace=True)\
\
#print()\
#print('Error in model:')\
#print(errormetricAR)\
#errorDF = pd.DataFrame(errormetricAR)\
#if len(errorDF) == len(zipNames):\
#errorDF.index = zipNames\
#errorDF = errorDF.transpose()\
#print(errorDF)\
#errorDF.plot().set(title="Error in model", xlabel="Month", ylabel="Error")\
#pyplot.show()\
#SAVE DATA IN CSV FILE:\
#errorDF.to_csv('ARError.csv')\
\
#print()\
#print('y actual')\
#yactARDF = pd.DataFrame(yactAR)\
#yactARDF = yactARDF.transpose()\
#yactARDF.columns = ["Hot Springs","Little Rock","Fayetteville","Searcy"]\
#print(yactARDF)\
\
#print()\
#yhatDF = pd.DataFrame(yhatAR)\
#yhatDF = yhatDF.transpose()\
#yhatDF.columns = ["Hot Springs pred","Little Rock pred","Fayetteville pred","Searcy pred"]\
#print('y predicted:')\
#print(yhatDF)\


## Screenshots
**Visualizations aligned to zip codes in AR only as example:**\
**Initial Analysis**\
A time series analysis for 4 metro areas in Arkansas\
![image](https://user-images.githubusercontent.com/75768214/127574066-a0503786-eaae-45cf-b525-50630ff8e080.png)
\
\
Error prediction model of Arkansas zip codes over the next 1 year
![image](https://user-images.githubusercontent.com/75768214/127574077-8b2fb3ed-b7bd-4d80-9164-24c25c378e0a.png)

## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
