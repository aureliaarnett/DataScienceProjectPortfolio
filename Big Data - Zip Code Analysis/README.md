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
**Data Structuring -- Extracting 4 zip codes in AR:**
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
.
.
.
# Consolidate 4 zip codes into 1 dataset
ARmetro = pd.DataFrame(HotSpringsMean)
ARmetro['Little Rock'] = LittleRockMean['Little Rock']
ARmetro['Fayetteville'] = ARFayettevilleMean['Fayetteville']
ARmetro['Searcy'] = SearcyMean['Searcy']
print('Initial Analysis: Dataset containing AR metro areas')
print(ARmetro)
#ARmetro.plot().set(title="Time Series for AR Metro Areas", xlabel="Year", ylabel="Mean Housing Value")
#pyplot.show()


## Screenshots
**Header** 

## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
