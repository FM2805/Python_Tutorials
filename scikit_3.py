# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 12:52:15 2017

@author: FloM
"""

"""
Basic scikit: Cross Validation
"""

from sklearn.datasets import load_iris
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
x=iris.data
y=iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.4,random_state=4)


# k-fold cross-validation
from sklearn.model_selection import KFold
kf= KFold(n_splits=2,shuffle=False) # into 2 folds
kf.get_n_splits(range(1,25))

X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
print(X)

# Returns an index!!!
for train_index, test_index in kf.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]



# Parameter tuning - 10 fold cross-validation
from sklearn.model_selection import cross_val_score #CV score
knn =KNeighborsClassifier(n_neighbors=4)
scores = cross_val_score(knn,x,y,cv=10,scoring="accuracy")
print(scores.mean())


k_range = range(1,31)
k_scores=[]

for k in k_range:
    knn =KNeighborsClassifier(n_neighbors=k)
    scores=cross_val_score(knn,x,y,cv=10,scoring="accuracy")
    k_scores.append(scores.mean())

print(k_scores)
plt.plot(k_range,k_scores)
    



