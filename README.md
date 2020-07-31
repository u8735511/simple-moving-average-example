# simple-moving-average-example
**counting simple moving average by using yfinance**


## ***Features***

- main-stock_max.py:Use yahoo finance daily data to count 5MA, 10MA, 20MA, 60MA, 120MA, 240MA, you can change period by yourself.
- main-stock_week.py:Use yahoo finance weekly data to count 4MA, 8MA, you can change period by yourself.

## ***Requirements***

- Python 3
- Python `pip`
- Python module `yfinance`
- Python module `pandas_datareader`

## ***Module Installation***

	pip install -r requirements.txt
	
## ***Usage***

***counting Moving average and save data to csv file***

    python main-stock_max(en).py
	python main-stock_week(en).py
	
### ***Folder***

1. stock_list:put you stock symbol here
2. stock_data:csv file output

### ***Output Files***
1. do_moving_stock.txt:This is a sample compared output for daily data
2. do_moving_stock_week.txt:This is a sample compared output for weekly data