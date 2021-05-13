# Uncovering the authors of the Federalist papers - Hamilton, Madison, or Jay

## Table of contents
* [General info](#general-info)
* [Technologies used](#technologies-used)
* [Python methods used](#python-methods-used)
* [Code example](#code-example)
* [Screenshots from analysis](#screenshots-from-analysis)
* [Contact](#contact)

## General info
> This project evaluates 51 essays known to be written by Hamilton, 15 essays known to be written by Madison, 3 essays known to be written by both Hamilton and Madison, and 5 essays known to be written by Jay to predict the author of 11 mystery documents using clustering techniques and data mining in R.

## Technologies used
* R

## Python methods used
* Format the .csv data into a corpus (collection of written texts)
* Convert corpus text into a data term matrix in R
* Evaluate distance measures between 2 Hamilton docs and 2 Madison docs to uncover text similarities (Euclidean and Cosine similarity calculations)
* K-means clustering
* Expectation-maximization algorithm

## Code example


## Screenshots from analysis
**Load all essays into a corpus**: Hierarchical cluster diagram of a corpus with all essays included\
![image](https://user-images.githubusercontent.com/75768214/118076678-863bc700-b367-11eb-8f7a-40339954b94b.png)

Cluster visualization for k-means calculations associated with the Hamilton and Hamilton-Madison corpus\
![image](https://user-images.githubusercontent.com/75768214/118077045-34477100-b368-11eb-814b-790fa247764d.png)

Cluster visualization for k-means calculations associated with the Madison and Hamilton-Madison corpus
![image](https://user-images.githubusercontent.com/75768214/118077062-3dd0d900-b368-11eb-9724-05412c263523.png)


## Contact
Created by [@AureliaArnett](https://twitter.com/AureliaArnett) --> Let's connect!
