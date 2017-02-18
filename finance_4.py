# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:42:33 2017
@author: FloM
"""

"""
sentdex Tutorial - Programming for finance 9-12
"""

from collections import Counter
import pandas as pd
import numpy as np
from sklearn import svm,cross_validation,neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier



def process_data_for_labels(ticker):
    hm_days=7 #days to the future
    df = pd.read_csv('sp500_joined_closes.csv',index_col=0)
    tickers=df.columns.values.tolist()
    df.fillna(0,inplace=True)
    
    
    for i in range(1,hm_days+1):
        print(i)
        # custom col xom(tickername)_2d(when i =2) // {} is placeholder for the format function!
        df['{}_{}d'.format(ticker,i)] =(df[ticker].shift(-i) - df[ticker]) / df[ticker]
    
    
    df.fillna(0,inplace=True)
    return tickers,df


# with as many parameters as we want - define the y (target)
def buy_sell_hold(*args): 
    cols = [c for c in args]
    requirement = 0.02 #if stock price changes by 2 percent in 7 days -> act
    for col in cols:
        if col > requirement:
            return 1 # buy
        if col <-requirement:
            return -1 # sell
    return 0 # hold

def extract_featuresets(ticker):
    tickers,df=process_data_for_labels(ticker)
    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                     df['{}_1d'.format(ticker)],      
                                     df['{}_2d'.format(ticker)],
                                     df['{}_3d'.format(ticker)],
                                     df['{}_4d'.format(ticker)],
                                     df['{}_5d'.format(ticker)],
                                     df['{}_6d'.format(ticker)],
                                     df['{}_7d'.format(ticker)] 
                                     )) 
    vals=df['{}_target'.format(ticker)].values.tolist()
    str_vals=[str(i) for i in vals]
    print('Data spread:',Counter(str_vals))
    df.fillna(0,inplace=True)
    
    df = df.replace([np.inf,-np.inf], np.nan)
    df.dropna(inplace=True)
    
    #daily percentage change
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df.replace([np.inf,-np.inf], 0)
    df_vals.fillna(0,inplace=True)

    X = df_vals.values
    y=df['{}_target'.format(ticker)].values
    
    return X,y,df


def do_ml(ticker):
    X,y,df=extract_featuresets(ticker)
    X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.25)
    
    #clf = neighbors.KNeighborsClassifier()
    clf = VotingClassifier([('lsvc',svm.LinearSVC()),
                            ('knn',neighbors.KNeighborsClassifier()),
                            ('rfor',RandomForestClassifier()),
                            
                            
    
    ])
    
    clf.fit(X_train,y_train)
    confidence =clf.score(X_test,y_test)
    
    predictions = clf.predict(X_test)
    
    print('predicted spread:', Counter(predictions))
    
    return confidence
    
   


do_ml('MMM')
    
    
    
    
    
    
    
    
    
    




    
    
    



