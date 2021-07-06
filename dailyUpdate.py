# Imports needed

from loadData import loadStocks
from StockAnalyst import generateTable, saveTable
from os import listdir
from os.path import isfile, join

# --------------------------------- #

# Edit dates as needed
dates = ["2021-5-9", "2021-5-10", "2021-5-11", "2021-5-12", "2021-5-13"]

# Edit stocks list as needed
loadStocks()

stocks_loaded = [f for f in listdir('stock_data') if isfile(join('stock_data', f))]

for stock in stocks_loaded:
    saveTable(stock, generateTable(stock, dates))
    print(stock, 'saved')