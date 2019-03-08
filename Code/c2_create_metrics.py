#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals
import math
from sklearn.feature_extraction.text import TfidfVectorizer

from urllib.request import urlopen
from bs4 import BeautifulSoup
import collections, re
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pickle
import time


###
### Define functions here
###

# Used to create flag variables
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return(True) 
    return(False) 
def intersect_score(a, b):
    a_set = set(a)
    b_set = set(b)
    return(len(a_set.intersection(b_set)))

###
### Create bag of words here 
###

#Please excuse the vulgarity
curses = ["fuck", "fucking", "shit", "ass", "nigga", "niggas", "bitch", "bullshit", "pussy", "bastard", "dick", "niggaz", "cock", "asshole", "mothafucka", "titties", "tiddy", "tits", "motherfucker", "douche", "douchebag", "cunt", "twat"]
whiskey = ["whiskey","fireball","jack","daniels","daniel's","jim","beam","moonshine"]


###
### Read in data
###

song_db = pickle.load( open( "/Users/brettharder/Documents/VILLANOVA/Categorical Data/Brett_Billboard_Project/01_Data/pickled_final_db/final_db.p", "rb" ) )
song_db
song_db.lyrics[1]

### 
### Building corpus for TF-IDF
###

train = song_db[song_db.year != 2017]
train
# View Lyrics QC
train['lyrics'].iloc[0]

###Split by genre
country = train[train.genre == 'country']
hip_hop = train[train.genre == 'hip-hop']
pop = train[train.genre == 'pop']
rock = train[train.genre == 'rock']

###
### Get full list of all lyrics in each genre
###

# Country

#Start w empty list and append each songs lyrics w frequencies
lyrics_country = []
for i in range(0,len(country.lyrics)):
    lyrics_country.append(Counter(country['lyrics'].iloc[i]))
lyrics_country   

#iniilaize new dictionary to add values  
full_lyrics_country = lyrics_country[0]
#Adds up word values
for i in range(1,len(lyrics_country)):
    full_lyrics_country = full_lyrics_country + lyrics_country[i]
full_lyrics_country

# Creates full document
country_doc = ""
words = list(full_lyrics_country.keys())
times = list(full_lyrics_country.values())
for i in range(0,len(words)):
    country_doc = country_doc + (words[i] + ' ')*times[i]
    
country_doc


# Hip_hop
lyrics_hip_hop = []
for i in range(0,len(hip_hop.lyrics)):
    lyrics_hip_hop.append(Counter(hip_hop['lyrics'].iloc[i]))
lyrics_hip_hop   
  
full_lyrics_hip_hop = lyrics_hip_hop[0]

for i in range(1,len(lyrics_hip_hop)):
    full_lyrics_hip_hop = full_lyrics_hip_hop + lyrics_hip_hop[i]
full_lyrics_hip_hop

hip_hop_doc = ""
words = list(full_lyrics_hip_hop.keys())
times = list(full_lyrics_hip_hop.values())
for i in range(0,len(words)):
    hip_hop_doc = hip_hop_doc + (words[i] + ' ')*times[i]
    
hip_hop_doc
len(hip_hop_doc)


# Pop
lyrics_pop = []
for i in range(0,len(pop.lyrics)):
    lyrics_pop.append(Counter(pop['lyrics'].iloc[i]))
lyrics_pop   
  
full_lyrics_pop = lyrics_pop[0]

for i in range(1,len(lyrics_pop)):
    full_lyrics_pop = full_lyrics_pop + lyrics_pop[i]
full_lyrics_pop

pop_doc = ""
words = list(full_lyrics_pop.keys())
times = list(full_lyrics_pop.values())
for i in range(0,len(words)):
    pop_doc = pop_doc + (words[i] + ' ')*times[i]
    
pop_doc
len(pop_doc)

# Rock
lyrics_rock = []
for i in range(0,len(rock.lyrics)):
    lyrics_rock.append(Counter(rock['lyrics'].iloc[i]))
lyrics_rock   
  
full_lyrics_rock = lyrics_rock[0]

for i in range(1,len(lyrics_rock)):
    full_lyrics_rock = full_lyrics_rock + lyrics_rock[i]
full_lyrics_rock

rock_doc = ""
words = list(full_lyrics_rock.keys())
times = list(full_lyrics_rock.values())
for i in range(0,len(words)):
    rock_doc = rock_doc + (words[i] + ' ')*times[i]
    
rock_doc
len(rock_doc)

###
### combine all genre documents into full list for TF-IDF
###

corpus = [country_doc,hip_hop_doc,pop_doc,rock_doc]

###
### TF-IDF CODE
tf = TfidfVectorizer(analyzer='word', ngram_range=(1,1), min_df = 0, stop_words = 'english')

tfidf_matrix =  tf.fit_transform(corpus)
feature_names = tf.get_feature_names()

len(feature_names)

tfidf_matrix

dense = tfidf_matrix.todense()
dense
len(dense[0].tolist()[0])


###
### Country analysis
###
country_matrix = dense[0].tolist()[0]
phrase_scores = [pair for pair in zip(range(0, len(country_matrix)), country_matrix) if pair[1] > 0]

# 1,490 compared to total words = 8,333
len(phrase_scores)

sorted(phrase_scores, key=lambda t: t[1] * -1)[:5]

# Country top phrases and scores
sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)

country_tfidf_bag = []
country_tfidf_score = []
for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:50]:
   print('{0: <20} {1}'.format(phrase, score))
   country_tfidf_bag.append(phrase)
   country_tfidf_score.append(score)
country_tfidf_bag

#Export 50 most important words and scores
country_tfidf_df = pd.DataFrame({'phrase':country_tfidf_bag,
                            'score':country_tfidf_score})                   
                         
country_tfidf_df.to_csv('/Users/brettharder/Documents/Categorical Data/Project/03_Reports/country_tfidf.csv',index=False)





###
### Hip-Hop analysis
###

hip_hop_matrix = dense[1].tolist()[0]
phrase_scores = [pair for pair in zip(range(0, len(hip_hop_matrix)), hip_hop_matrix) if pair[1] > 0]

# 5,065 compared to total words = 8,333
len(phrase_scores)

sorted(phrase_scores, key=lambda t: t[1] * -1)[:5]

# Hip-Hop top phrases and scores
hip_hop_tfidf_bag = []
hip_hop_tfidf_score = []
sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:50]:
   print('{0: <20} {1}'.format(phrase, score))
   hip_hop_tfidf_bag.append(phrase)
   hip_hop_tfidf_score.append(score)
hip_hop_tfidf_bag  

#Export 50 most important words and scores
hip_hop_tfidf_df = pd.DataFrame({'phrase':hip_hop_tfidf_bag,
                            'score':hip_hop_tfidf_score})                   
                         
hip_hop_tfidf_df.to_csv('/Users/brettharder/Documents/Categorical Data/Project/03_Reports/hip_hop_tfidf.csv',index=False)
 



###
### Pop analysis
###

pop_matrix = dense[2].tolist()[0]
phrase_scores = [pair for pair in zip(range(0, len(pop_matrix)), pop_matrix) if pair[1] > 0]

# 4,770 compared to total words = 8,333
len(phrase_scores)

sorted(phrase_scores, key=lambda t: t[1] * -1)[:5]

# Pop top phrases and scores
pop_tfidf_bag = []
pop_tfidf_score = []
sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:50]:
   print('{0: <20} {1}'.format(phrase, score))
   pop_tfidf_bag.append(phrase)
   pop_tfidf_score.append(score)
pop_tfidf_bag

#Export 50 most important words and scores
pop_tfidf_df = pd.DataFrame({'phrase':pop_tfidf_bag,
                            'score':pop_tfidf_score})                   
                         
pop_tfidf_df.to_csv('/Users/brettharder/Documents/Categorical Data/Project/03_Reports/pop_tfidf.csv',index=False)
 

###
### Rock analysis
###

rock_matrix = dense[3].tolist()[0]
phrase_scores = [pair for pair in zip(range(0, len(rock_matrix)), rock_matrix) if pair[1] > 0]

# 546 compared to total words = 8,333
len(phrase_scores)

sorted(phrase_scores, key=lambda t: t[1] * -1)[:5]

# Rock top phrases and scores
rock_tfidf_bag = []
rock_tfidf_score = []
sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:50]:
   print('{0: <20} {1}'.format(phrase, score))
   rock_tfidf_bag.append(phrase)
   rock_tfidf_score.append(score)
rock_tfidf_bag

#Export 50 most important words and scores
rock_tfidf_df = pd.DataFrame({'phrase':rock_tfidf_bag,
                            'score':rock_tfidf_score})                   
                         
rock_tfidf_df.to_csv('/Users/brettharder/Documents/Categorical Data/Project/03_Reports/rock_tfidf.csv',index=False)
 

###
### End of TF-IDF
###

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

###
### Create metrics
###

# TF-IDF METRICS
country_tfidf_bag
hip_hop_tfidf_bag
pop_tfidf_bag
rock_tfidf_bag

# initialize song genre tfidf scores
country_tfidf_score = []
hip_hop_tfidf_score = []
pop_tfidf_score = []
rock_tfidf_score = []

for i in range(0,len(song_db)):
    country_tfidf_score.append(intersect_score(list(song_db.lyrics[i].keys()),country_tfidf_bag)/len(country_tfidf_bag))
    hip_hop_tfidf_score.append(intersect_score(list(song_db.lyrics[i].keys()),hip_hop_tfidf_bag)/len(hip_hop_tfidf_bag))
    pop_tfidf_score.append(intersect_score(list(song_db.lyrics[i].keys()),pop_tfidf_bag)/len(pop_tfidf_bag))
    rock_tfidf_score.append(intersect_score(list(song_db.lyrics[i].keys()),rock_tfidf_bag)/len(rock_tfidf_bag))
  

      
# TF-IDF METRICS!!! 
country_tfidf_score
hip_hop_tfidf_score
pop_tfidf_score   
rock_tfidf_score

# Curse word indicator variable
curses


curse_flag = []
dirtiness_score = []
whiskey_flag = []
total_lyrics = []
unique_words = []

for i in range(0,len(song_db)):
    total_lyrics.append(sum(song_db.lyrics[i].values()))
    unique_words.append(len(song_db.lyrics[i].keys()))
    dirtiness_score.append(intersect_score(list(song_db.lyrics[i].keys()),curses))
    if common_member(list(song_db.lyrics[i].keys()),curses) == True:
        curse_flag.append(1)
    else:
        curse_flag.append(0)
    if common_member(list(song_db.lyrics[i].keys()),whiskey) == True:
        whiskey_flag.append(1)
    else:
        whiskey_flag.append(0)
      

curse_flag
dirtiness_score
whiskey_flag
total_lyrics
unique_words

###
### Merge all metrics back to database to create final db
###

song_db_metrics = pd.DataFrame({'song':song_db.song,
                          'artist':song_db.artist,
                          'lyrics':song_db.lyrics,
                          'genre':song_db.genre,
                          'collaboration':song_db.collaboration,
                          'year':song_db.year,
                          'country_tfidf_score':country_tfidf_score,
                          'hip_hop_tfidf_score':hip_hop_tfidf_score,
                          'pop_tfidf_score':pop_tfidf_score,
                          'rock_tfidf_score':rock_tfidf_score,
                          'curse_flag':curse_flag,
                          'dirtiness_score':dirtiness_score,
                          'whiskey_flag':whiskey_flag,
                          'total_lyrics':total_lyrics,
                          'unique_words':unique_words})                   
                         
song_db_metrics

# Pickle dat boiii

pickle.dump( song_db_metrics, open( "/Users/brettharder/Documents/GitHub/BB_Top100/Data/Modelling_db/final_db_metrics.p", "wb" ) )



###
### Drop lyrics and export csv!!!
###

songs_to_csv = pd.DataFrame({'song':song_db_metrics.song,
                            'artist':song_db_metrics.artist,
                            'genre':song_db_metrics.genre,
                            'collaboration':song_db_metrics.collaboration,
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
                         
songs_to_csv

songs_to_csv.to_csv('/Users/brettharder/Documents/GitHub/BB_Top100/Data/Modelling_db/billboard_processed_db.csv',index=False)
















