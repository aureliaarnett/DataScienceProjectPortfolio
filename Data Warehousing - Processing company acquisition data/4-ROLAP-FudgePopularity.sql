/****** Object:  Database ist722_hhkhan_ob3_dw    Script Date: 3/13/2021 4:01:56 PM ******/
/*
Kimball Group, The Microsoft Data Warehouse Toolkit
Generate a database from the datamodel worksheet, version: 4

You can use this Excel workbook as a data modeling tool during the logical design phase of your project.
As discussed in the book, it is in some ways preferable to a real data modeling tool during the inital design.
We expect you to move away from this spreadsheet and into a real modeling tool during the physical design phase.
The authors provide this macro so that the spreadsheet isn't a dead-end. You can 'import' into your
data modeling tool by generating a database using this script, then reverse-engineering that database into
your tool.

Uncomment the next lines if you want to drop and create the database
*/
/*
DROP DATABASE ist722_hhkhan_ob3_dw
GO
CREATE DATABASE ist722_hhkhan_ob3_dw
GO
ALTER DATABASE ist722_hhkhan_ob3_dw
SET RECOVERY SIMPLE
GO
*/
USE ist722_hhkhan_ob3_dw
;
IF EXISTS (SELECT Name from sys.extended_properties where Name = 'Description')
    EXEC sys.sp_dropextendedproperty @name = 'Description'
EXEC sys.sp_addextendedproperty @name = 'Description', @value = 'Default description - you should change this.'
;


-- Create a schema to hold user views (set schema name on home page of workbook).
-- It would be good to do this only if the schema doesn't exist already.
GO
CREATE SCHEMA fudge
GO


/* Drop table fudge.DimDate */
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'fudge.DimDate') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE fudge.DimDate
;

/* Create table fudge.DimDate */
CREATE TABLE fudge.DimDate (
   [DateKey]  int   NOT NULL
,  [Date]  datetime   NULL
,  [FullDateUSA]  nchar(11)   NOT NULL
,  [DayOfWeek]  tinyint   NOT NULL
,  [DayName]  nchar(10)   NOT NULL
,  [DayOfMonth]  tinyint   NOT NULL
,  [DayOfYear]  int   NOT NULL
,  [WeekOfYear]  tinyint   NOT NULL
,  [MonthName]  nchar(10)   NOT NULL
,  [MonthOfYear]  tinyint   NOT NULL
,  [Quarter]  tinyint   NOT NULL
,  [QuarterName]  nchar(10)   NOT NULL
,  [Year]  int   NOT NULL
,  [IsWeekday]  varchar(1)  DEFAULT 0 NOT NULL
, CONSTRAINT [PK_fudge.DimDate] PRIMARY KEY CLUSTERED 
( [DateKey] )
) ON [PRIMARY]
;


INSERT INTO fudge.dimdate (DateKey, Date, FullDateUSA, DayOfWeek, DayName, DayOfMonth, DayOfYear, WeekOfYear, MonthName, MonthOfYear, Quarter, QuarterName, Year, IsWeekday)
VALUES (-1, '', 'Unk date', 0, 'Unk date', 0, 0, 0, 'Unk month', 0, 0, 'Unk qtr', 0, 0)
;





/* Drop table fudge.DimProduct */
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'fudge.DimProduct') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE fudge.DimProduct 
;


/* Create table fudge.DimProduct */
CREATE TABLE fudge.DimProduct (
   [ProductKey]  int IDENTITY  NOT NULL
,  [product_id]  varchar(20)   NOT NULL
,  [product_name]  varchar(200)   NOT NULL
,  [product_type]  varchar(221)   NOT NULL
,  [RowIsCurrent]  bit  DEFAULT 1 NOT NULL
,  [RowStartDate]  datetime  DEFAULT '12/31/1899' NOT NULL
,  [RowEndDate]  datetime  DEFAULT '12/31/9999' NOT NULL
,  [RowChangeReason]  nvarchar(200)   NULL
, CONSTRAINT [PK_fudge.DimProduct] PRIMARY KEY CLUSTERED 
( [ProductKey] )
) ON [PRIMARY]
;


SET IDENTITY_INSERT fudge.DimProduct ON
;
INSERT INTO fudge.DimProduct (ProductKey, product_id, product_name, product_type, RowIsCurrent, RowStartDate, RowEndDate, RowChangeReason)
VALUES (-1, '0', 'None', 'None', 1, '12/31/1899', '12/31/9999', 'N/A')
;
SET IDENTITY_INSERT fudge.DimProduct OFF
;



/* Drop table fudge.DimCustomer */
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'fudge.DimCustomer') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE fudge.DimCustomer 
;

/* Create table fudge.DimCustomer */
CREATE TABLE fudge.DimCustomer (
   [CustomerKey]  int IDENTITY  NOT NULL
,  [CustomerID]  int  NOT NULL
,  [customer_email]  varchar(200)   NOT NULL
,  [customer_firstname]  varchar(50)   NOT NULL
,  [customer_lastname]  varchar(50)   NOT NULL
,  [customer_zipcode]  varchar(20)   NOT NULL
,  [RowIsCurrent]  bit  DEFAULT 1 NOT NULL
,  [RowStartDate]  datetime  DEFAULT '12/31/1899' NOT NULL
,  [RowEndDate]  datetime  DEFAULT '12/31/9999' NOT NULL
,  [RowChangeReason]  nvarchar(200)    NULL
, CONSTRAINT [PK_fudge.DimCustomer] PRIMARY KEY CLUSTERED 
( [CustomerKey] )
) ON [PRIMARY]
;


SET IDENTITY_INSERT fudge.DimCustomer ON
;
INSERT INTO fudge.DimCustomer (CustomerKey, CustomerID, customer_email, customer_firstname, customer_lastname,customer_zipcode, RowIsCurrent, RowStartDate, RowEndDate, RowChangeReason)
VALUES (-1, -1, 'None', 'None', 'None', 'None', 1, '12/31/1899', '12/31/9999', 'N/A')
;
SET IDENTITY_INSERT fudge.DimCustomer OFF
;



/* Drop table fudge.FactPopularity */
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'fudge.FactPopularity') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE fudge.FactPopularity 
;

/* Create table fudge.FactPopularity */
CREATE TABLE fudge.FactPopularity (
   [ProductKey]  int   NOT NULL
,  [CustomerKey]  int   NOT NULL
,  [ReviewDateKey]  int   NOT NULL
,  [product_name]  varchar(200)   NOT NULL
,  [customer_rating]  int   NULL
,  [product_type]  varchar(221) NOT NULL
,  [origin_database] nvarchar(20) NOT NULL
, CONSTRAINT [PK_fudge.FactPopularity] PRIMARY KEY NONCLUSTERED 
([ProductKey], [CustomerKey], [ReviewDateKey], [product_type] )
) ON [PRIMARY]
;

 
ALTER TABLE fudge.FactPopularity ADD CONSTRAINT
   FK_fudge_FactPopularity_CustomerKey FOREIGN KEY
   (
   CustomerKey
   ) REFERENCES fudge.DimCustomer
   ( CustomerKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;
 
ALTER TABLE fudge.FactPopularity ADD CONSTRAINT
   FK_fudge_FactPopularity_ProductKey FOREIGN KEY
   (
   ProductKey
   ) REFERENCES fudge.DimProduct
   ( ProductKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;
 
ALTER TABLE fudge.FactPopularity ADD CONSTRAINT
   FK_fudge_FactPopularity_OrderDateKey FOREIGN KEY
   (
   ReviewDateKey
   ) REFERENCES fudge.DimDate
   ( DateKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;

