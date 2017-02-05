# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 16:03:46 2017

@author: FloM
"""

"""
Basic scikit:  Model tuning, grid search, randomized grid search
"""




from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


iris = load_iris()
# feature matrix x
X = iris.data
# response vector y
y= iris.target

k_range = range(1,31)
scores = []

# key = parameter name (=n_neighbors for us), value = value to be searche for the parameter
param_grid= dict(n_neighbors=k_range)
print(param_grid)

knn = KNeighborsClassifier(n_neighbors=5) # this can 'do' knn estimations

# instantate the grid - not estimate yet. Will repeat the 10 fold CV process 30 times (range 1:31)
# every time, n_neighbors will get a different value from the list
grid = GridSearchCV(knn,param_grid,cv=10,scoring='accuracy')
#with n_jobs = -1 --> runs on multiple CPUs, parallel processing then!

grid.fit(X,y)
grid.cv_results_

print(grid.best_params_)
print(grid.best_score_)

# extract mean scores
means = grid.cv_results_['mean_test_score']
plt.plot(k_range,means)


"""
Optimize multiple parameters at once
"""

# Values that will be searched
k_range = range(1,31)
weight_options =['uniform','distance']


param_grid= dict(n_neighbors=k_range,weights=weight_options)
print(param_grid)

# every combination of nneighbors and weights -> 60 times  10*30(neighbors)*2 (weights)
grid = GridSearchCV(knn,param_grid,cv=10,scoring='accuracy')
grid.fit(X,y)
grid.cv_results_
means = grid.cv_results_['mean_test_score']
print(grid.best_params_)
print(grid.best_score_)

# Predict with best model
n_data = [1,2,1,8]
grid.predict([1,2,1,8])



"""
Reduce computational complexity
"""

from sklearn.grid_search import RandomizedSearchCV

# specify a parameter distribution (same as here a discrete distibution)
param_dist= dict(n_neighbors=k_range,weights=weight_options)
# Attention -> specify a distribution for continuous values! NO List!

# n_iter -> number of combination searched
rand =RandomizedSearchCV(knn,param_dist,cv=10,scoring ='accuracy',n_iter = 10)
rand.fit(X,y)

rand.best_score_
rand.best_params_





