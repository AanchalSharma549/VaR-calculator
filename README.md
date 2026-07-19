# VaR Calculator - Value at Risk Analysis

## What is VaR?

VaR- Value at Risk tells you the expected loss one can expect during a period of time at a particular level of confidence
Example- "VaR at 95% is 1000$" means 95% of the time our loss will be less then 1000$ but 5% of the time, it can exceed the amount.

## What Does This Project Do?

This project lets you calculate the VaR in 3 different ways called Historical, Parametric, Monte Carlo. The sample data used here is 20 years of stock data downloaded from kaggle.It let you compare all the different methods and figure out which will work best for you.


## The 3 Methods Explained

### 1. Historical Simulation
It works with the past data and assumes loss on that basis. In case of uncertainities, it is not the best.


### 2. Parametric (Variance-Covariance)
It uses a math formula which assumes that your investment follows normal distribution (bell curve), the only catch isthat the real market is not always this perfect as it assumes.


### 3. Monte Carlo Simulation
It creates as many fake scenarios as required matching the real data's pattern and then work on that fake data to find out the worst of the 5%, it takes time and is heavier on computer but works better in complex situations.

## Key Takeaway

One can try different methods and can decide which work the best on which data. You get different answers thus it is important to know what to use and when. 

## Files Included

- `var_calculator.py` - Main code
- `stockdata.csv` - Historical stock price data
- `README.md` - This file

## Author

Aanchal Sharma
Date: 18th July, 2026