# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:22:42 2017

@author: FloM
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

# Set the style
style.use=('ggplot')

# Set the time
start= dt.datetime(2000,1,1)
end= dt.datetime(2016,12,31)

# Read Apple data
df = web.DataReader('AAPL','yahoo',start,end)
#print(df.head())
#print(df.tail(3))
#df.to_csv('Apple.csv')

#Need to set the date as the index
df =pd.read_csv('C:/Users/FloM/Desktop/Persönlich/Programmieren/Python/Tutorials/Finance/Apple.csv',parse_dates=True,index_col=0)
print(df.head())

#df.plot()
#plt.show()

# Plot open close
#df[['Open','Close']].plot()
#df['Open'].plot()

# Set min to 0 -> for first observations uses all availabe info to calculate MA
df['50ma'] = df['Adj Close'].rolling(window=50,min_periods=0).mean()
# Remove all NAs where MA could not be calculated
#df.dropna(inplace=True)
print(df.head())

# Plot with matplotlib - define subplots
# Sharex -> takes same axis
ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1) #6 rows, 1 col - span 5 rows
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1) #6 rows, 1 col - spans 1 row

# Plot the data
#ax1.plot(df.index,df['Adj Close'])
#ax1.plot(df.index,df['50ma'])
#ax2.plot(df.index,df['Adj Close'])
#plt.show()


# Convert to 2-week data
# Open high low close of the 2 weeks
df_ohlc = df['Adj Close'].resample('14D').ohlc()
df_volume = df['Volume'].resample('14D').sum()

# Rest the index for plotting - convert to mplot date - need that for the plot
df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
ax1.xaxis_date()

candlestick_ohlc(ax1,df_ohlc.values,width=2,colorup='g')
# For ax2 - fill between date and values (x is the date-index, y is the volume)
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)
plt.show()




