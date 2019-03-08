#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:13:25 2018

@author: brettharder
"""

# -----------------------
# XgBoost on Lyrics Yo
# ----------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import xgboost as xgb
from sklearn.metrics import confusion_matrix
 
# Read in data
df = pd.read_csv('/Users/brettharder/Documents/GitHub/BB_Top100/Data/Modelling_db/billboard_processed_db.csv')

# Split into training and test
modelling_df = pd.DataFrame({'collaboration':song_db_metrics.collaboration,
                             'z_genre':song_db_metrics.genre,
                            'year':song_db_metrics.year,
                            'country_tfidf_score':song_db_metrics.country_tfidf_score,
                            'hip_hop_tfidf_score':song_db_metrics.hip_hop_tfidf_score,
                            'pop_tfidf_score':song_db_metrics.pop_tfidf_score,
                            'rock_tfidf_score':song_db_metrics.rock_tfidf_score,
                            'curse_flag':song_db_metrics.curse_flag,
                            'dirtiness_score':song_db_metrics.dirtiness_score,
                            'whiskey_flag':song_db_metrics.whiskey_flag,
                            'total_lyrics':total_lyrics,
                            'unique_words':unique_words}) 
modelling_df.shape

# Drop Year and split into train and test
X_train = modelling_df[modelling_df.year != 2017].iloc[:,0:10].values
X_test = modelling_df[modelling_df.year == 2017].iloc[:,0:10].values

y_train_str = modelling_df[modelling_df.year != 2017]["z_genre"]
y_test_str =  modelling_df[modelling_df.year == 2017]["z_genre"]

y_train = []

for i in range(0,y_train_str.shape[0]):
    if y_train_str.iloc[i] == "pop":
        y_train.append(0)
    elif y_train_str.iloc[i] == "hip-hop":
        y_train.append(1)
    elif y_train_str.iloc[i] == "country":
        y_train.append(2)
    else:
        y_train.append(3)

y_test = []
for i in range(0,y_test_str.shape[0]):
    if y_test_str.iloc[i] == "pop":
        y_test.append(0)
    elif y_test_str.iloc[i] == "hip-hop":
        y_test.append(1)
    elif y_test_str.iloc[i] == "country":
        y_test.append(2)
    else:
        y_test.append(3)

# Convert lists to numpy arrays
y_train = np.asarray(y_train)
y_test = np.asarray(y_test)

X_train = np.asarray(X_train)
X_test = np.asarray(X_test)

# Standardize features
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Convert to xgboost training and test sets
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# Set parameters
param = {
    'max_depth': 3,  # the maximum depth of each tree
    'eta': 0.3,  # the training step for each iteration
    'silent': 1,  # logging mode - quiet
    'objective': 'multi:softprob',  # error evaluation for multiclass training
    'num_class': 4}  # the number of classes that exist in this datset
num_round = 20  # the number of training iterations

# Train the model
bst = xgb.train(param, dtrain, num_round)

# Predict on test data
preds = bst.predict(dtest)

# pulling highest predicted class for y_predicted
y_pred = np.asarray([np.argmax(line) for line in preds])

# Model performance
from sklearn.metrics import precision_score
print(precision_score(y_test, y_pred, average='macro'))


# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
cm

# Split into training and test
comp = pd.DataFrame({'actual':y_test,'test':y_pred }) 

correct_y_n = []
for i in range(0,comp.shape[0]):
    if comp.actual[i] == comp.test[i]:
        correct_y_n.append(1)
    else:
        correct_y_n.append(0)
comp["correct_y_n"] = correct_y_n
comp.correct_y_n.mean()

# -------------
# ANN On lyrics 
# -------------

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_y_1 = LabelEncoder()
y_train = labelencoder_y_1.fit_transform(y_train)
y_test = labelencoder_y_1.fit_transform(y_test)

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 10))

# Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 4, kernel_initializer = 'uniform', activation = 'softmax'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 20)
y_pred = classifier.predict(X_test)

# pulling highest predicted class for y_predicted
y_pred = np.asarray([np.argmax(line) for line in preds])

# Model performance
from sklearn.metrics import precision_score
print(precision_score(y_test, y_pred, average='macro'))


# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
cm

# Split into training and test
comp = pd.DataFrame({'actual':y_test,'test':y_pred }) 
correct_y_n = []
for i in range(0,comp.shape[0]):
    if comp.actual[i] == comp.test[i]:
        correct_y_n.append(1)
    else:
        correct_y_n.append(0)
comp["correct_y_n"] = correct_y_n
comp.correct_y_n.mean()

# ------
# SVM YO
# -----

from sklearn.svm import SVC  
svclassifier = SVC(kernel='linear')  
svclassifier.fit(X_train, y_train)  

y_pred = svclassifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  

comp = pd.DataFrame({'actual':y_test,'test':y_pred }) 
correct_y_n = []
for i in range(0,comp.shape[0]):
    if comp.actual[i] == comp.test[i]:
        correct_y_n.append(1)
    else:
        correct_y_n.append(0)
comp["correct_y_n"] = correct_y_n
comp.correct_y_n.mean()