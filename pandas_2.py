# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 21:24:06 2017

@author: FloM
"""

"""
Basic pandas: Rename, Drop cols
"""



import pandas as pd


#list for header
user_cols =['id','age','gender','job','zip']
# now pipe as seperator, first row no header
users = pd.read_table('http://bit.ly/movieusers',sep='|', header= None,names=user_cols) 

# attributes - wie ohne ()
users.shape
# methods - action oriented with ()
users.describe()

# get cols
users.columns
#rename
users.rename(columns={'zip':'zip_code','job':'job_desc'},inplace=True) # with dictionary

# or pass a list if rename all
users_cols =['ID','AGE','GENDER','JOB','ZIP']
users.columns = users_cols


# Remove Cols - also works with a list
users.drop('GENDER',axis=1,inplace=True)  # axes = 0: Row // axes =1: Columns
# get cols
users.columns

# Sort a series
users['AGE'].sort_values(ascending=False)

# Sort a DF (by AGE)
users.sort_values('AGE')