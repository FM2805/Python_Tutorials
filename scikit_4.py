# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 14:37:49 2017

@author: FloM
"""
"""
Basic scikit:  More cross validation - regression example
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score #CV score




data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv',index_col=0)

help(pd.read_csv)

# List of col names
feature_cols =['TV', 'Radio', 'Newspaper']
X = data[feature_cols]
y= data.Sales

# 10 fold CV with all features
lm = LinearRegression()
scores = cross_val_score(lm,X,y,cv=10,scoring="mean_squared_error")
print(scores) # negative, need to change the sign (mse is a loss function! - smaller better)


mse_scores = -scores
#root mean squared error
rmse = np.sqrt(mse_scores)
# average
print(rmse.mean())


#estimate with only 2 cols
feature_cols =['TV', 'Radio']
X = data[feature_cols]
y= data.Sales
scores = np.sqrt(-cross_val_score(lm,X,y,cv=10,scoring="mean_squared_error"))
print(scores.mean())


