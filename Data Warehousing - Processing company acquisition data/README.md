# Data Warehousing - Processing company acquisition data

## Table of contents
* [General info](#general-info)
* [Technologies used](#technologies-used)
* [Methods used](#methods-used)
* [Code example](ode-example-(ROLAP-in-SQL-SERVER))
* [Screenshots](#screenshots)
* [Contact](#contact)

## General info
> General

## Technologies used
* SQL Server
* Visual Studios
* PowerBI

## Methods used
* SQL Querying
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

**ETL:** See file '5-ETL-FudgePopularity.docx' for full process outlining building one data warehouse and extracting data from the 2 companies\
Control flow for Fudgemart data extraction:\
![image](https://user-images.githubusercontent.com/75768214/117605730-47123980-b10d-11eb-8bc1-229f9b5bbed3.png)

Control flow for Fudgemart data load:\
![image](https://user-images.githubusercontent.com/75768214/117605649-15996e00-b10d-11eb-9ef3-351924199f5d.png)

**MOLAP:**
![image](https://user-images.githubusercontent.com/75768214/117606036-e6373100-b10d-11eb-9477-9174563cfdf4.png)

**BI:** Final output: most popular products & categories (incl. genres for TV shows & movies)\
![image](https://user-images.githubusercontent.com/75768214/117605935-aff9b180-b10d-11eb-9880-3afd59dbac19.png)
![image](https://user-images.githubusercontent.com/75768214/117605941-b38d3880-b10d-11eb-97c3-28404b770a04.png)

## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
