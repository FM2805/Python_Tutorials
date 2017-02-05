# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 21:45:06 2017

@author: FloM
"""

"""
Basic pandas: Filter data-frame
"""

import pandas as pd


#list for header
user_cols =['id','age','gender','job','zip']
# now pipe as seperator, first row no header
users = pd.read_table('http://bit.ly/movieusers',sep='|', header= None,names=user_cols) 

users.shape
users.columns


# filter a DF
is_old = users.age > 40
users[is_old] # or
users[users.age > 40]

# filter with multiple criteria
users[(users.age > 40) & (users.job=='educator')]