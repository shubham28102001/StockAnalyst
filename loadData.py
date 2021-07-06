# Imports needed
import time
import numpy as np
import pandas as pd
import investpy
from os import listdir
from os.path import isfile, join
import warnings

warnings.filterwarnings("ignore")

# Loads historical data of stock
def loadHistoricalData(stock):
    df = investpy.get_stock_historical_data(stock=stock,
                                        country='India',
                                        from_date='01/01/2010',
                                        to_date='28/06/2021')

    df = df.drop('Currency', axis=1)
    df.to_csv('stock_data/%s.csv'%(stock))

# loads for multiple stocks
def loadStocks(specific_stocks=[], max_stocks=20):
    stocks = investpy.stocks.get_stocks_list(country='India')
    stocks = [i for i in stocks if not i in specific_stocks]
    stocks = stocks[:(max_stocks-len(specific_stocks))]
    stocks_req = stocks+specific_stocks

    for stock in stocks_req:
        loadHistoricalData(stock)
        print(stock, ' loaded')


# checks if stock is loaded, if it isnt (and exists), then loads it
def loadStock(stock):
    stocks = investpy.stocks.get_stocks_list(country='India')
    stocks_loaded = [f for f in listdir('stock_data') if isfile(join('stock_data', f))]
    stocks_loaded = [f.replace('.csv', '') for f in stocks_loaded]

    if not stock in stocks:
        return 0
    elif stock in stocks_loaded:
        return 1
    else:
        loadHistoricalData(stock)
        print(stock, ' loaded')
        return 2