# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 17:43:29 2017

@author: FloM
"""

"""
Basic pandas: Select cols
"""

import pandas as pd

orders = pd.read_table('http://bit.ly/chiporders') #assumes tab separation,header row
orders.head()


#list for header
user_cols =['id','age','gender','job','zip']
# now pipe as seperator, first row no header
users = pd.read_table('http://bit.ly/movieusers',sep='|', header= None,names=user_cols) 
users.head()


# Entweder ufo = pd.read_table('http://bit.ly/uforeports',sep=',') 
# Oder
ufo = pd.read_csv('http://bit.ly/uforeports')  # here "," is the default
ufo.head

#Get city col
ufo['City']
type(ufo['City']) # is a Series (= a col)
# OR
ufo.City # the name of a col is an attribute of the df

# if space - no dot notation
ufo['Colors Reported'] 

# Concat
ufo.City + ',' + ufo.State

# New Col
ufo['Location'] = ufo.City + ',' + ufo.State
ufo.head()


