###
### Clean Song genres and make workable Database
###

from urllib.request import urlopen
from bs4 import BeautifulSoup
import collections, re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pickle
import time


song_db = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_final_db/final_db.p", "rb" ) )
song_db

#Dimensions of dataframe
song_db.shape
song_db[song_db.year == 2017].shape
song_db[song_db.year != 2017].shape

# 83% of data in training dataset (2017)
song_db[song_db.year != 2017].shape[0] / song_db.shape[0]

#Freq of genres - 5 different - country, hip-hop, pop, rock
song_db.groupby('genre').count()

#Genres by year
song_db.groupby(['year','genre']).count()

#Averge collab per year
song_db.groupby(['year']).mean()























