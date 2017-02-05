# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 10:47:09 2017

@author: FloM
"""

"""
Basic scikit: Prediction
"""


from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression


iris= load_iris()
type(iris)

print(iris.data)

print(iris.target_names)

# feature matrix x
x = iris.data
x.shape

# response vector y
y= iris.target
y.shape


# Create an instance of the estimator (knn) - to be precise the knn class
knn = KNeighborsClassifier(n_neighbors=1) # this can 'do' knn estimations
print(knn)

# fit model
knn.fit(x,y)

#predict new observation
knn.predict([3,4,5,2])

# predict 2 new observations
X_new= [[3,4,2,1],[4,6,1,9]]
knn.predict(X_new)



# Create an instance of the estimator 
log_reg = LogisticRegression() 
print(log_reg)

# fit model
log_reg.fit(x,y)

#predict new observation
log_reg.predict([3,4,5,2])

# predict 2 new observations
X_new= [[3,4,2,1],[4,6,1,9]]
log_reg.predict(X_new)



