# Data Warehousing - Processing company acquisition data

## Table of contents
* [General info](#general-info)
* [Technologies used](#technologies-used)
* [Methods used](#methods-used)
* [Code example](ode-example-(ROLAP-in-SQL-SERVER))
* [Screenshots](#screenshots)
* [Contact](#contact)

## General info
> This project processes data from the aquisition of 1 company into another by consolidating data from 2 data warehouses into 1 and standardizing the way data is processed and labelled. The data analysis consists of evaluating business processes for both companies and outlining 5 processes that exist for both companies using a high-level dimensional modeling worksheet. A detailed-level dimensional modeling worksheet is then used to deep dive into 1 business process, more specifically to understand product popularity based on customer reviews. Finally, data consolidation is processed through a series of ETL implementations and BI is applied to produce final recommendations.
>* Company 1 'Fudgemart' is a fictitious online retailer, similar to Amazon.com or Walmart.com. The database consists of customers, products and vendors, and has familiar business processes you would find in any online retailer.\
>* Company 2 'Fudgeflix'  is a fictitious online DVD by mail and video on demand service, similar to HULU, Netflix, or Disney+. The database for Fudgeflix is called Fudgeflix_v3 and contains concepts such as accounts, subscriptions and video titles as well as other things associated with an online video streaming service.

## Technologies used
* SQL Server
* Visual Studios
* Microsoft Power BI

## Methods used
* SQL querying
* ROLAP (SQL SERVER)
* ROLAP (Visual Studios)
* ETL (Visual Studios)
* Data visualization

## Code example (ROLAP in SQL SERVER)
See file '4-ROLAP-FudgePopularity.sql'

## Screenshots
**Company 1:** Fudgelix streaming services schema\
![image](https://user-images.githubusercontent.com/75768214/117604587-a7ec4280-b10a-11eb-9b46-ad7eb846cb21.png)

**Company 2:** Fudgemart retailer schema\
![image](https://user-images.githubusercontent.com/75768214/117604647-c5b9a780-b10a-11eb-98b3-f097cba22524.png)

**Star schema (ROLAP):** Star schema consists of the consolidation of Fudgeflix into Fudgemart, looking at the product popularity based on customer reviews\
![image](https://user-images.githubusercontent.com/75768214/117604779-1af5b900-b10b-11eb-88c3-4e9f4fad7093.png)

**ETL Implementation:** See file '5-ETL-FudgePopularity.docx' for full process outlining building one data warehouse and extracting data from the 2 companies\
Control flow for Fudgemart data extraction:\
![image](https://user-images.githubusercontent.com/75768214/117605730-47123980-b10d-11eb-8bc1-229f9b5bbed3.png)

Control flow for Fudgemart data load:\
![image](https://user-images.githubusercontent.com/75768214/117605649-15996e00-b10d-11eb-9ef3-351924199f5d.png)

**MOLAP:**\
![image](https://user-images.githubusercontent.com/75768214/117606183-2f878080-b10e-11eb-994b-36b5b7a7b96e.png)

**BI:** Final output: most popular products & categories (incl. genres for TV shows & movies)\
![image](https://user-images.githubusercontent.com/75768214/117605935-aff9b180-b10d-11eb-9880-3afd59dbac19.png)\
\
![image](https://user-images.githubusercontent.com/75768214/117605941-b38d3880-b10d-11eb-97c3-28404b770a04.png)

## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
