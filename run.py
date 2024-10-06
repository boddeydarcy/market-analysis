# imports
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf
from mplfinance.original_flavor import candlestick_ohlc

stock = "TSLA"
# set ticker to a stock
ticker = yf.Ticker(stock)
plt.figure(figsize=(10, 6))  # change size of plot

# create dataframe and clean data
df = pd.DataFrame(ticker.history(period="3mo"))
df.dropna(inplace=True)  # remove null values
print(df)
date = df.index  # value of df.index is the date from the dataframe
close = df[["Close"]]  # close price
open = df[["Open"]]  # open price

# Add labels and title
font = {"family": "monospace", "size": 14}  # create font for axis labels
plt.title(f"{stock} Stock Analysis")
plt.ylabel("Close Price", fontdict=font)
plt.xlabel("Date", fontdict=font)

# line plots
plt.plot(date, open, color="blue")  # open chart
plt.plot(date, close, color="red")  # close chart

# candle plot
if df["Volume"][0] == 0:  # if it is a forex ticker the volume will be 0, the chart showing volume would be irrelevant
    mpf.plot(df, type="candle", show_nontrading=True)  # removes non trading days i.e weekends
else:
    mpf.plot(df, type="candle", volume=True, show_nontrading=True)  # removes non trading days i.e weekends


# show plots
plt.show()
mpf.show()

