# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:42:33 2017
@author: FloM
"""

"""
sentdex Tutorial - Programming for finance 8
"""


import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot') 


df =pd.read_csv('C:/Users/FloM/Desktop/Persönlich/Programmieren/Python/Tutorials/Finance/sp500_joined_closes.csv')

df['AET'].plot()

# create a correlation table
df_corr = df.corr()
print(df_corr.head())
data = df_corr.values # gives us the data as a numpy array

# create a heatmap
fig=plt.figure()
ax=fig.add_subplot(1,1,1)


heatmap=ax.pcolor(data,cmap=plt.cm.RdYlGn)
fig.colorbar(heatmap)
ax.set_xticks(np.arange(data.shape[0])+0.5,minor=False)
ax.set_yticks(np.arange(data.shape[1])+0.5,minor=False)
ax.invert_yaxis()
ax.xaxis.tick_top()

column_labels = df_corr.columns
row_labels =df_corr.index

ax.set_xticklabels(column_labels)
ax.set_yticklabels(row_labels)
plt.xticks(rotation=90)
heatmap.set_clim(-1,1) # limit of colors
plt.show()






