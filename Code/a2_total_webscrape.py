# ----------------------------
# Scrape and Pickle ALL Songs
# ----------------------------

# -----------------
# CURRENT PROGRESS
#
# Scraped 
#
# 2006: 1-90
# 2007: 
# 2008:
# 2009:
# 2010:
# 2011:
# 2012:
# 2013:
# 2014:
# 2015:
# 2016:
# 2017:
# 2018:
# -----------------


# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import collections, re
import numpy as np

import pandas as pd
import pickle
import time

import sys
sys.path

import os
os.getcwd()

# Import scraping functionality
sys.path.append("/Users/brettharder/Documents/GitHub/BB_Top100/Code/src")
print(sys.path)
from scraping import song_scrape


# Read in songdb csv
song_db = pd.read_csv('/Users/brettharder/Documents/GitHub/BB_Top100/Data/Published/cleaned_song_db_final.csv')
# View records
song_db.head()
# Get types of variables
song_db.dtypes
# Get variable names
song_db.columns
# Get dimensions of dataframe 599 records, 8 variables
song_db.shape

# Select only top 10 records to practice scrape

#start and end parameters
start = 0
end = 10

# Create sample df
sample = song_db[start:end]

# Scrape song lyrics and genre
scraped_song_lyrics, lyric_bag, genre = song_scrape(song_db,start,end,5)

# Examine scraped fields
scraped_song_lyrics
lyric_bag
genre

len(genre)
len(lyric_bag)
len(scraped_song_lyrics)

        
# Get most used lyrics
for i in range(0,len(genre)):
    print(sample.song[i]+ " Most used lyric is " + max(lyric_bag[i], key=lyric_bag[i].get)+" -- Genre is "+genre[i])

# ---------------------------------------------
# Create dataframe of sampled lyrics and genres
# ---------------------------------------------

sample.song[0:10]
sample.collaboration
lyric_bag
genre
scraped_song_lyrics
sample.year
sample.artist

sample_df = pd.DataFrame({'song':sample.song[0:10],
                          'artist':sample.artist[0:10],
                          'lyrics':scraped_song_lyrics[0:10],
                          'lyrics_dict':lyric_bag[0:10],
                          'genre':genre[0:10],
                          'collaboration':sample.collaboration[0:10],
                          'year':sample.year[0:10]})
sample_df
len(sample_df)


pickle.dump( sample_df, open( "/Users/brettharder/Documents/GitHub/BB_Top100/Data/Pickled_Songs/songs_81_90.p", "wb" ) )

new_df = pickle.load(open( "/Users/brettharder/Documents/GitHub/BB_Top100/Data/Pickled_Songs/songs_1_10.p", "rb" ) )

new_df.lyrics

new_df

# Get most used lyrics
for i in range(0,len(new_df.genre)):
    print(new_df.song[i]+ " Most used lyric is " + max(new_df.lyrics_dict[i], key=new_df.lyrics_dict[i].get))

