# -*- coding: utf-8 -*-
"""baseline_results.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cPl5n-rFZ2_Oe_jLFZuOpyZRgrbLcvuM
"""

!pip install surprise
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from surprise import Reader, SVD, Dataset, accuracy
import os
from sklearn.model_selection import train_test_split
from surprise.model_selection import GridSearchCV

import random
random.seed(415)

original_ratings = pd.read_csv('/content/drive/My Drive/iw_data/ratings.csv')
original_ratings.reset_index(drop=True, inplace=True)

# only include movies with at least n ratings
n = 20
movies = original_ratings.movieId.value_counts()
movies = movies[movies>=n].index.tolist()
ratings = original_ratings.query('movieId in @movies')

# only include users with at least n ratings
users = ratings.userId.value_counts()
users = users[users>=n].index.tolist()

# take random sample of 10% of users to use as dataset
users = np.random.choice(users, size= (int)(len(users) * 0.1))
ratings = ratings.loc[ratings['userId'].isin(users)]
print(ratings.shape)

# split data into training testing sets
train_data, test_data = train_test_split(ratings, test_size = 0.5)
print("Training size:", train_data.shape)
print("Testing size:", test_data.shape)

# read training, testing sets into data frames
reader = Reader(rating_scale = (1, 5))
data_train_raw = Dataset.load_from_df(train_data[['userId', 'movieId', 'rating']], reader)
data_test_raw = Dataset.load_from_df(test_data[['userId', 'movieId', 'rating']], reader)

# create both training and testing data using "train set" format
data_train = data_train_raw.build_full_trainset()
data_test = data_test_raw.build_full_trainset()

# create both training and testing data using "test set" format
data_trainset = data_train.build_testset()
data_testset = data_test.build_testset()

train_data.to_csv("data_train_set.csv")
test_data.to_csv("data_test_set.csv")

# Create SVD
algo = SVD(n_factors = 50, n_epochs = 20, lr_all = 0.005, reg_all = 0.02)

# Create NMF 
# algo = NMF(n_factors = 15, n_epochs = 50)

# Train the algorithm on the trainset
algo.fit(data_train)

# make predictions on the testset
test_results = algo.test(data_testset)
print(accuracy.rmse(test_results))
test_results = pd.DataFrame(test_results)
test_results.drop("details", inplace=True, axis=1)
test_results.columns = ['userId', 'movieId', 'actual', 'cf_predictions']
test_results.head()

test_results.to_csv('test_results.csv')