# Optimizing Service Ticket Resolution Time - ServiceNow

## Table of contents
* [General info](#general-info)
* [Technologies used](#technologies-used)
* [Methods used](#methods-used)
* [File names](#file-names-&-their-meanings)
* [Setup](#setup)
* [Code example](#code-example)
* [Screenshots from analysis](#screenshots-from-analysis)
* [Contact](#contact)

## General info
> This project explores ServiceNow ticket data from 2 different companies, company A and company J, to better understand the environment for each company (number of technicians, skillsets, average ticket intakes), evaluate trends (such as average amount of time a ticket is open, different categories of ticket types, amount of staff available, qualified to work ticket), evaluate variable significance, and offer recomendations per company to help increase service efficiencies and minimizr expenses.

## Technologies used

## Methods used

## File names & their meanings

## Setup

## Code example
Note: The code below introduces the data cleansing step and occurs after importing the necessary packages (ex: pandas as pd; numpy as np; seaborn as sns)

a_data = pd.read_csv('/content/gdrive/Shared drives/IST 718 Project/a_complete.csv',encoding='ISO-8859-1')\
a_data\
a_data['closed_at'] = pd.to_datetime(a_data.closed_at)\
a_data['Date'] = a_data['closed_at'].dt.strftime('%Y-%m-%d')\
a_data = a_data.sort_values('Date', ascending=True)\
a_data[a_data['Date']=='2020-01-01']\
a_1 = a_data[8090:92000]\
a_1ac = a_1[a_1['u_actual_category']=='access-issue/request']\
a_1['business_duration'].mean()\
#drop blank columns\
a_data = a_data.dropna(how='all', axis=1)\
a_data #dropped 11 columns.. now we have 81 columns\
#drop any columns that have na values in 100 rows\
#first split into tasks and incidents so no useful columns are removed\
a_data_inc = a_data[:107215]\
a_data_tas = a_data[107215:]\
#remove columns with NaN in at least 100000 and 10000 rows\
a_data_inc = a_data_inc.dropna(thresh=len(a_data_inc) - 100000, axis=1) #due to inc size this one is larger\
a_data_tas = a_data_tas.dropna(thresh=len(a_data_tas) - 10000, axis=1)\
print(a_data_inc.info()) #reduce to 55 columns\
print(a_data_tas.info()) #reduce to 37 columns\
...

## Screenshots from analysis
Note: the screenshots below represent only a piece of this project, and for company A only

Data Exploration:

A visual representation of the number of tickets opened for company A between December 2019 and December 2020, by category of ticket and prioritiy type
Where P4 is least important and P1 is most important
![image](https://user-images.githubusercontent.com/75768214/117555973-e6a1d000-b018-11eb-8dcf-bdd1c9c6a21c.png)

Data Modeling: Forecasting (prophet model)\
Predicting the average time a ticket is open
![image](https://user-images.githubusercontent.com/75768214/117556119-5bc1d500-b01a-11eb-8956-d90c4395be29.png)

Predicting the number of tickets that will be open
![image](https://user-images.githubusercontent.com/75768214/117556130-75631c80-b01a-11eb-955a-06ee48b30c08.png)

Predicting the cost to service a ticket (measured by technician time & pay)
![image](https://user-images.githubusercontent.com/75768214/117556151-96c40880-b01a-11eb-984a-3d0c32c57d68.png)

Data Modeling: Timeseries\
Predicting the count of tickets from the category 'software' that will be opened in the next year
![image](https://user-images.githubusercontent.com/75768214/117556185-e6a2cf80-b01a-11eb-8dc2-48b805cf93f7.png)


## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
