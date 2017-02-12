# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:22:42 2017

@author: FloM
"""
import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

# Get S&P 500 table from wiki
def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup=bs.BeautifulSoup(resp.text,'lxml')
    table= soup.find('table',{'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]: # for each row in table
        ticker = row.findAll('td')[0].text #1st column
        tickers.append(ticker)
        
    with open('sp500tickers.pickle','wb') as f:
        pickle.dump(tickers,f) # dump the tickers to file f
        
        print(tickers)
    return tickers
#save_sp500_tickers() # call function


# Get data from yahoo
def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500: #if true
        tickers= save_sp500_tickers()
    else: #false - as now
         with open('sp500tickers.pickle','rb') as f:
             tickers=pickle.load(f)
    if not os.path.exists('stock_df'):
        os.makedirs('stock_dfs')
        
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2016,12,31)
    
    for ticker in tickers[:10]: 
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)): #checks wheter the csv exists already (with name of the company)
            df = web.DataReader(ticker,'yahoo',start,end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('already have {}'.format(ticker))     
get_data_from_yahoo()


# convert the data (csv file) in one df
def compile_data():
    with open("sp500tickers.pickle","rb") as f:
        tickers = pickle.load(f)[:10] # only 10, as have loaded only 10
        
    main_df = pd.DataFrame()
    
    for count,ticker in enumerate(tickers):
        df=pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date',inplace=True)
        
        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open','High','Low','Close','Volume'],1, inplace=True)
        
        if main_df.empty:
            main_df=df
        else:
            main_df = main_df.join(df,how='outer')
            
        # print after 10th count
        if count % 10 == 0:
            print(count)
    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')

compile_data()
    
    





















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    