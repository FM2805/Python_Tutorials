# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 12:10:30 2017

@author: FloM
"""

"""
Basic scikit: Test and train a model
"""

from sklearn.datasets import load_iris
iris = load_iris()
x=iris.data
y=iris.target

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(x,y)
logreg.predict(x)
y_pred = logreg.predict(x)
len(y_pred)

# Get classification accuracy
from sklearn import metrics
metrics.accuracy_score(y,y_pred)
#training accuracy


from sklearn.neighbors import KNeighborsClassifier
knn =KNeighborsClassifier(n_neighbors=4)
knn.fit(x,y)
y_pred = knn.predict(x)

# Test and train model
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.4,random_state=4)

print(x_train)
print(x_test)

x_train.shape
y_train.shape

# Estimate based on training data
logreg = LogisticRegression()
logreg.fit(x_train,y_train)
# Predict on test
y_pred = logreg.predict(x_test)
#true values in y_test
print(metrics.accuracy_score(y_test,y_pred))

# Estimate based on training data
knn =KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)
print(metrics.accuracy_score(y_test,y_pred))
# much better

# automatic testing

import matplotlib.pyplot as plt

k_range = range(1,20)
scores = []

for k in k_range:
    print(k)
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    y_pred = knn.predict(x_test)
    scores.append(metrics.accuracy_score(y_test,y_pred))   
    

plt.plot(k_range,scores)



