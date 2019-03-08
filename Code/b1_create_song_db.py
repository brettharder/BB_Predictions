###
### Stacking and fixing data
###

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import collections, re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pickle
import time


#Load Pickled songs dataframes

songs_1_10 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_1_10.p", "rb" ) )
songs_1_10

year = [2017]*10
year

artist = ["Ed Sheeran", "Luis Fonsi & Daddy Yankee Featuring Justin Bieber", "Bruno Mars", "Kendrick Lamar", "The Chainsmokers & Coldplay", "Migos Featuring Lil Uzi Vert", "The Chainsmokers Featuring Halsey", "Sam Hunt", "Imagine Dragons","Post Malone Featuring Quavo"]

# Append year and artist to this and 11-20
song_1_10 = pd.DataFrame({'song':songs_1_10.song,
                          'artist':artist,
                          'lyrics':songs_1_10.lyrics,
                          'genre':songs_1_10.genre,
                          'collaboration':songs_1_10.collaboration,
                          'year':year})
song_1_10

song_1_10


songs_11_20 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_11_20.p", "rb" ) )
songs_11_20

artist = ["James Arthur", "DJ Khaled Featuring Justin Bieber, Quavo, Chance The Rapper & Lil Wayne", "Lil Uzi Vert", "Future", "French Montana Featuring Swae Lee", "Bruno Mars", "Zedd & Alessia Cara", "DJ Khaled Featuring Rihanna & Bryson Tiller", "Rae Sremmurd Featuring Gucci Mane", "The Weeknd Featuring Daft Punk"]
song_11_20 = pd.DataFrame({'song':songs_11_20.song,
                          'artist':artist,
                          'lyrics':songs_11_20.lyrics,
                          'genre':songs_11_20.genre,
                          'collaboration':songs_11_20.collaboration,
                          'year':year})
song_11_20


songs_21_30 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_21_30.p", "rb" ) )
songs_21_30

song_21_30 = pd.DataFrame({'song':songs_21_30.song,
                          'artist':songs_21_30.artist,
                          'lyrics':songs_21_30.lyrics,
                          'genre':songs_21_30.genre,
                          'collaboration':songs_21_30.collaboration,
                          'year':songs_21_30.year})
song_21_30


songs_31_40 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_31_40.p", "rb" ) )
songs_31_40

song_31_40 = pd.DataFrame({'song':songs_31_40.song,
                          'artist':songs_31_40.artist,
                          'lyrics':songs_31_40.lyrics,
                          'genre':songs_31_40.genre,
                          'collaboration':songs_31_40.collaboration,
                          'year':songs_31_40.year})
song_31_40



songs_41_50 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_41_50.p", "rb" ) )
songs_41_50

song_41_50 = pd.DataFrame({'song':songs_41_50.song,
                          'artist':songs_41_50.artist,
                          'lyrics':songs_41_50.lyrics,
                          'genre':songs_41_50.genre,
                          'collaboration':songs_41_50.collaboration,
                          'year':songs_41_50.year})
song_41_50


songs_51_60 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_51_60.p", "rb" ) )
songs_51_60
song_51_60 = pd.DataFrame({'song':songs_51_60.song,
                          'artist':songs_51_60.artist,
                          'lyrics':songs_51_60.lyrics,
                          'genre':songs_51_60.genre,
                          'collaboration':songs_51_60.collaboration,
                          'year':songs_51_60.year})
song_51_60


songs_61_66 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_61_66.p", "rb" ) )
songs_61_66

song_61_66 = pd.DataFrame({'song':songs_61_66.song,
                          'artist':songs_61_66.artist,
                          'lyrics':songs_61_66.lyrics,
                          'genre':songs_61_66.genre,
                          'collaboration':songs_61_66.collaboration,
                          'year':songs_61_66.year})
song_61_66


songs_67_70 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_67_70.p", "rb" ) )
songs_67_70
song_67_70 = pd.DataFrame({'song':songs_67_70.song,
                          'artist':songs_67_70.artist,
                          'lyrics':songs_67_70.lyrics,
                          'genre':songs_67_70.genre,
                          'collaboration':songs_67_70.collaboration,
                          'year':songs_67_70.year})
song_67_70

songs_71_78 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_71_78.p", "rb" ) )
songs_71_78
song_71_78 = pd.DataFrame({'song':songs_71_78.song,
                          'artist':songs_71_78.artist,
                          'lyrics':songs_71_78.lyrics,
                          'genre':songs_71_78.genre,
                          'collaboration':songs_71_78.collaboration,
                          'year':songs_71_78.year})
song_71_78


songs_79_80 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_79_80.p", "rb" ) )
songs_79_80
song_79_80 = pd.DataFrame({'song':songs_79_80.song,
                          'artist':songs_79_80.artist,
                          'lyrics':songs_79_80.lyrics,
                          'genre':songs_79_80.genre,
                          'collaboration':songs_79_80.collaboration,
                          'year':songs_79_80.year})
song_79_80


songs_81_83 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_81_83.p", "rb" ) )
songs_81_83
song_81_83 = pd.DataFrame({'song':songs_81_83.song,
                          'artist':songs_81_83.artist,
                          'lyrics':songs_81_83.lyrics,
                          'genre':songs_81_83.genre,
                          'collaboration':songs_81_83.collaboration,
                          'year':songs_81_83.year})
song_81_83


songs_84_90 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_84_90.p", "rb" ) )
songs_84_90
song_84_90 = pd.DataFrame({'song':songs_84_90.song,
                          'artist':songs_84_90.artist,
                          'lyrics':songs_84_90.lyrics,
                          'genre':songs_84_90.genre,
                          'collaboration':songs_84_90.collaboration,
                          'year':songs_84_90.year})
song_84_90



songs_91_98 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_91_98.p", "rb" ) )
songs_91_98
song_91_98 = pd.DataFrame({'song':songs_91_98.song,
                          'artist':songs_91_98.artist,
                          'lyrics':songs_91_98.lyrics,
                          'genre':songs_91_98.genre,
                          'collaboration':songs_91_98.collaboration,
                          'year':songs_91_98.year})
song_91_98


songs_99_100 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_99_100.p", "rb" ) )
songs_99_100
song_99_100 = pd.DataFrame({'song':songs_99_100.song,
                          'artist':songs_99_100.artist,
                          'lyrics':songs_99_100.lyrics,
                          'genre':songs_99_100.genre,
                          'collaboration':songs_99_100.collaboration,
                          'year':songs_99_100.year})
song_99_100

# Stack dataframes
songs = [song_1_10,song_11_20,songs_21_30,songs_31_40,songs_41_50,songs_51_60,songs_61_66,songs_67_70,songs_71_78,songs_79_80,songs_81_83,songs_84_90,songs_91_98,songs_99_100]
songs


db_2017 = pd.concat(songs)
db_2017.lyrics

### Dump df
pickle.dump( db_2017, open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2017.p", "wb" ) )


songs_2017 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2017.p", "rb" ) )

songs_2017
songs_2017.genre


#######################################
#######################################   2016
#######################################


### Create 2016 df

#101-117
songs_101_117 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_100_117.p", "rb" ) )
songs_101_117
song_101_117 = pd.DataFrame({'song':songs_101_117.song,
                          'artist':songs_101_117.artist,
                          'lyrics':songs_101_117.lyrics,
                          'genre':songs_101_117.genre,
                          'collaboration':songs_101_117.collaboration,
                          'year':songs_101_117.year})
song_101_117

#118-121
songs_118_121 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_118_121.p", "rb" ) )
songs_118_121
song_118_121 = pd.DataFrame({'song':songs_118_121.song,
                          'artist':songs_118_121.artist,
                          'lyrics':songs_118_121.lyrics,
                          'genre':songs_118_121.genre,
                          'collaboration':songs_118_121.collaboration,
                          'year':songs_118_121.year})
song_118_121

# 122_130
songs_122_130 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_122_130.p", "rb" ) )
songs_122_130
song_122_130 = pd.DataFrame({'song':songs_122_130.song,
                          'artist':songs_122_130.artist,
                          'lyrics':songs_122_130.lyrics,
                          'genre':songs_122_130.genre,
                          'collaboration':songs_122_130.collaboration,
                          'year':songs_122_130.year})
song_122_130

# 131_140
songs_131_140 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_131_140.p", "rb" ) )
songs_131_140
song_131_140 = pd.DataFrame({'song':songs_131_140.song,
                          'artist':songs_131_140.artist,
                          'lyrics':songs_131_140.lyrics,
                          'genre':songs_131_140.genre,
                          'collaboration':songs_131_140.collaboration,
                          'year':songs_131_140.year})
song_131_140

# 141_146
songs_141_146 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_141_146.p", "rb" ) )
songs_141_146
song_141_146 = pd.DataFrame({'song':songs_141_146.song,
                          'artist':songs_141_146.artist,
                          'lyrics':songs_141_146.lyrics,
                          'genre':songs_141_146.genre,
                          'collaboration':songs_141_146.collaboration,
                          'year':songs_141_146.year})
song_141_146

# 147_150
songs_147_150 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_147_150.p", "rb" ) )
songs_147_150
song_147_150 = pd.DataFrame({'song':songs_147_150.song,
                          'artist':songs_147_150.artist,
                          'lyrics':songs_147_150.lyrics,
                          'genre':songs_147_150.genre,
                          'collaboration':songs_147_150.collaboration,
                          'year':songs_147_150.year})
song_147_150

# 151_160
songs_151_160 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_151_160.p", "rb" ) )
songs_151_160
song_151_160 = pd.DataFrame({'song':songs_151_160.song,
                          'artist':songs_151_160.artist,
                          'lyrics':songs_151_160.lyrics,
                          'genre':songs_151_160.genre,
                          'collaboration':songs_151_160.collaboration,
                          'year':songs_151_160.year})
song_151_160

# 161_170
songs_161_170 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_161_170.p", "rb" ) )
songs_161_170
song_161_170 = pd.DataFrame({'song':songs_161_170.song,
                          'artist':songs_161_170.artist,
                          'lyrics':songs_161_170.lyrics,
                          'genre':songs_161_170.genre,
                          'collaboration':songs_161_170.collaboration,
                          'year':songs_161_170.year})
song_161_170

# 171_180
songs_171_180 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_171_180.p", "rb" ) )
songs_171_180
song_171_180 = pd.DataFrame({'song':songs_171_180.song,
                          'artist':songs_171_180.artist,
                          'lyrics':songs_171_180.lyrics,
                          'genre':songs_171_180.genre,
                          'collaboration':songs_171_180.collaboration,
                          'year':songs_171_180.year})
song_171_180

# 181_190
songs_181_190 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_181_190.p", "rb" ) )
songs_181_190
song_181_190 = pd.DataFrame({'song':songs_181_190.song,
                          'artist':songs_181_190.artist,
                          'lyrics':songs_181_190.lyrics,
                          'genre':songs_181_190.genre,
                          'collaboration':songs_181_190.collaboration,
                          'year':songs_181_190.year})
song_181_190

# 191_200
songs_191_200 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_191_200.p", "rb" ) )
songs_191_200
song_191_200 = pd.DataFrame({'song':songs_191_200.song,
                          'artist':songs_191_200.artist,
                          'lyrics':songs_191_200.lyrics,
                          'genre':songs_191_200.genre,
                          'collaboration':songs_191_200.collaboration,
                          'year':songs_191_200.year})
song_191_200


# Stack dataframes
songs = [song_101_117,song_118_121,song_122_130,song_131_140,song_141_146,song_147_150,song_151_160,song_161_170,song_171_180,song_181_190,song_191_200]
songs


db_2016 = pd.concat(songs)
db_2016.genre

### Dump df
pickle.dump( db_2016, open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2016.p", "wb" ) )

songs_2016 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2016.p", "rb" ) )

songs_2016
songs_2017.genre



##################################################################
##################################################################     2015
##################################################################



# 201_210
songs_201_210 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_201_210.p", "rb" ) )
songs_201_210
song_201_210 = pd.DataFrame({'song':songs_201_210.song,
                          'artist':songs_201_210.artist,
                          'lyrics':songs_201_210.lyrics,
                          'genre':songs_201_210.genre,
                          'collaboration':songs_201_210.collaboration,
                          'year':songs_201_210.year})
song_201_210

# 211_220
songs_211_220 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_211_220.p", "rb" ) )
songs_211_220
song_211_220 = pd.DataFrame({'song':songs_211_220.song,
                          'artist':songs_211_220.artist,
                          'lyrics':songs_211_220.lyrics,
                          'genre':songs_211_220.genre,
                          'collaboration':songs_211_220.collaboration,
                          'year':songs_211_220.year})
song_211_220

# 221_230
songs_221_230 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_221_230.p", "rb" ) )
songs_221_230
song_221_230 = pd.DataFrame({'song':songs_221_230.song,
                          'artist':songs_221_230.artist,
                          'lyrics':songs_221_230.lyrics,
                          'genre':songs_221_230.genre,
                          'collaboration':songs_221_230.collaboration,
                          'year':songs_221_230.year})
song_221_230

# 231_240
songs_231_240 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_231_240.p", "rb" ) )
songs_231_240
song_231_240 = pd.DataFrame({'song':songs_231_240.song,
                          'artist':songs_231_240.artist,
                          'lyrics':songs_231_240.lyrics,
                          'genre':songs_231_240.genre,
                          'collaboration':songs_231_240.collaboration,
                          'year':songs_231_240.year})
song_231_240

# 241_250
songs_241_250 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_241_250.p", "rb" ) )
songs_241_250
song_241_250 = pd.DataFrame({'song':songs_241_250.song,
                          'artist':songs_241_250.artist,
                          'lyrics':songs_241_250.lyrics,
                          'genre':songs_241_250.genre,
                          'collaboration':songs_241_250.collaboration,
                          'year':songs_241_250.year})
song_241_250

# 251_260
songs_251_260 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_251_260.p", "rb" ) )
songs_251_260
song_251_260 = pd.DataFrame({'song':songs_251_260.song,
                          'artist':songs_251_260.artist,
                          'lyrics':songs_251_260.lyrics,
                          'genre':songs_251_260.genre,
                          'collaboration':songs_251_260.collaboration,
                          'year':songs_251_260.year})
song_251_260

# 261_270
songs_261_270 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_261_270.p", "rb" ) )
songs_261_270
song_261_270 = pd.DataFrame({'song':songs_261_270.song,
                          'artist':songs_261_270.artist,
                          'lyrics':songs_261_270.lyrics,
                          'genre':songs_261_270.genre,
                          'collaboration':songs_261_270.collaboration,
                          'year':songs_261_270.year})
song_261_270

# 271_280
songs_271_280 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_271_280.p", "rb" ) )
songs_271_280
song_271_280 = pd.DataFrame({'song':songs_271_280.song,
                          'artist':songs_271_280.artist,
                          'lyrics':songs_271_280.lyrics,
                          'genre':songs_271_280.genre,
                          'collaboration':songs_271_280.collaboration,
                          'year':songs_271_280.year})
song_271_280

# 281_290
songs_281_290 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_281_290.p", "rb" ) )
songs_281_290
song_281_290 = pd.DataFrame({'song':songs_281_290.song,
                          'artist':songs_281_290.artist,
                          'lyrics':songs_281_290.lyrics,
                          'genre':songs_281_290.genre,
                          'collaboration':songs_281_290.collaboration,
                          'year':songs_281_290.year})
song_281_290

# 291_300
songs_291_300 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_291_300.p", "rb" ) )
songs_291_300
song_291_300 = pd.DataFrame({'song':songs_291_300.song,
                          'artist':songs_291_300.artist,
                          'lyrics':songs_291_300.lyrics,
                          'genre':songs_291_300.genre,
                          'collaboration':songs_291_300.collaboration,
                          'year':songs_291_300.year})
song_291_300


# Stack dataframes
songs = [song_201_210,song_211_220,song_221_230,song_231_240,song_241_250,song_251_260,song_261_270,song_271_280,song_281_290,song_291_300]
songs


db_2015 = pd.concat(songs)
db_2015
db_2015.genre

### Dump df
pickle.dump( db_2015, open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2015.p", "wb" ) )

songs_2015 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2015.p", "rb" ) )

songs_2015
songs_2015.song



##################################################################
##################################################################     2014
##################################################################



# 301_310
songs_301_310 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_301_310.p", "rb" ) )
songs_301_310
song_301_310 = pd.DataFrame({'song':songs_301_310.song,
                          'artist':songs_301_310.artist,
                          'lyrics':songs_301_310.lyrics,
                          'genre':songs_301_310.genre,
                          'collaboration':songs_301_310.collaboration,
                          'year':songs_301_310.year})
song_301_310

# 311_320
songs_311_320 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_311_320.p", "rb" ) )
songs_311_320
song_311_320 = pd.DataFrame({'song':songs_311_320.song,
                          'artist':songs_311_320.artist,
                          'lyrics':songs_311_320.lyrics,
                          'genre':songs_311_320.genre,
                          'collaboration':songs_311_320.collaboration,
                          'year':songs_311_320.year})
song_311_320

# 321_330
songs_321_330 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_321_330.p", "rb" ) )
songs_321_330
song_321_330 = pd.DataFrame({'song':songs_321_330.song,
                          'artist':songs_321_330.artist,
                          'lyrics':songs_321_330.lyrics,
                          'genre':songs_321_330.genre,
                          'collaboration':songs_321_330.collaboration,
                          'year':songs_321_330.year})
song_321_330

# 331_340
songs_331_340 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_331_340.p", "rb" ) )
songs_331_340
song_331_340 = pd.DataFrame({'song':songs_331_340.song,
                          'artist':songs_331_340.artist,
                          'lyrics':songs_331_340.lyrics,
                          'genre':songs_331_340.genre,
                          'collaboration':songs_331_340.collaboration,
                          'year':songs_331_340.year})
song_331_340

# 341_350
songs_341_350 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_341_350.p", "rb" ) )
songs_341_350
song_341_350 = pd.DataFrame({'song':songs_341_350.song,
                          'artist':songs_341_350.artist,
                          'lyrics':songs_341_350.lyrics,
                          'genre':songs_341_350.genre,
                          'collaboration':songs_341_350.collaboration,
                          'year':songs_341_350.year})
song_341_350

# 351_360
songs_351_360 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_351_360.p", "rb" ) )
songs_351_360
song_351_360 = pd.DataFrame({'song':songs_351_360.song,
                          'artist':songs_351_360.artist,
                          'lyrics':songs_351_360.lyrics,
                          'genre':songs_351_360.genre,
                          'collaboration':songs_351_360.collaboration,
                          'year':songs_351_360.year})
song_351_360

# 361_370
songs_361_370 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_361_370.p", "rb" ) )
songs_361_370
song_361_370 = pd.DataFrame({'song':songs_361_370.song,
                          'artist':songs_361_370.artist,
                          'lyrics':songs_361_370.lyrics,
                          'genre':songs_361_370.genre,
                          'collaboration':songs_361_370.collaboration,
                          'year':songs_361_370.year})
song_361_370

# 371_380
songs_371_380 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_371_380.p", "rb" ) )
songs_371_380
song_371_380 = pd.DataFrame({'song':songs_371_380.song,
                          'artist':songs_371_380.artist,
                          'lyrics':songs_371_380.lyrics,
                          'genre':songs_371_380.genre,
                          'collaboration':songs_371_380.collaboration,
                          'year':songs_371_380.year})
song_371_380

# 381_390
songs_381_390 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_381_390.p", "rb" ) )
songs_381_390
song_381_390 = pd.DataFrame({'song':songs_381_390.song,
                          'artist':songs_381_390.artist,
                          'lyrics':songs_381_390.lyrics,
                          'genre':songs_381_390.genre,
                          'collaboration':songs_381_390.collaboration,
                          'year':songs_381_390.year})
song_381_390

# 391_400
songs_391_400 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_391_400.p", "rb" ) )
songs_391_400
song_391_400 = pd.DataFrame({'song':songs_391_400.song,
                          'artist':songs_391_400.artist,
                          'lyrics':songs_391_400.lyrics,
                          'genre':songs_391_400.genre,
                          'collaboration':songs_391_400.collaboration,
                          'year':songs_391_400.year})
song_391_400


# Stack dataframes
songs = [song_301_310,song_311_320,song_321_330,song_331_340,song_341_350,song_351_360,song_361_370,song_371_380,song_381_390,song_391_400]
songs


db_2014 = pd.concat(songs)
db_2014
db_2014.genre

### Dump df
pickle.dump( db_2014, open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2014.p", "wb" ) )

songs_2014 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2014.p", "rb" ) )

songs_2014
songs_2014.song



##################################################################
##################################################################     2013
##################################################################

# 401_410
songs_401_410 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_401_410.p", "rb" ) )
songs_401_410
song_401_410 = pd.DataFrame({'song':songs_401_410.song,
                          'artist':songs_401_410.artist,
                          'lyrics':songs_401_410.lyrics,
                          'genre':songs_401_410.genre,
                          'collaboration':songs_401_410.collaboration,
                          'year':songs_401_410.year})
song_401_410

# 411_420
songs_411_420 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_411_420.p", "rb" ) )
songs_411_420
song_411_420 = pd.DataFrame({'song':songs_411_420.song,
                          'artist':songs_411_420.artist,
                          'lyrics':songs_411_420.lyrics,
                          'genre':songs_411_420.genre,
                          'collaboration':songs_411_420.collaboration,
                          'year':songs_411_420.year})
song_411_420

# 421_430
songs_421_430 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_421_430.p", "rb" ) )
songs_421_430
song_421_430 = pd.DataFrame({'song':songs_421_430.song,
                          'artist':songs_421_430.artist,
                          'lyrics':songs_421_430.lyrics,
                          'genre':songs_421_430.genre,
                          'collaboration':songs_421_430.collaboration,
                          'year':songs_421_430.year})
song_421_430

# 431_440
songs_431_440 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_431_440.p", "rb" ) )
songs_431_440
song_431_440 = pd.DataFrame({'song':songs_431_440.song,
                          'artist':songs_431_440.artist,
                          'lyrics':songs_431_440.lyrics,
                          'genre':songs_431_440.genre,
                          'collaboration':songs_431_440.collaboration,
                          'year':songs_431_440.year})
song_431_440

# 441_450
songs_441_450 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_441_450.p", "rb" ) )
songs_441_450
song_441_450 = pd.DataFrame({'song':songs_441_450.song,
                          'artist':songs_441_450.artist,
                          'lyrics':songs_441_450.lyrics,
                          'genre':songs_441_450.genre,
                          'collaboration':songs_441_450.collaboration,
                          'year':songs_441_450.year})
song_441_450

# 451_460
songs_451_460 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_451_460.p", "rb" ) )
songs_451_460
song_451_460 = pd.DataFrame({'song':songs_451_460.song,
                          'artist':songs_451_460.artist,
                          'lyrics':songs_451_460.lyrics,
                          'genre':songs_451_460.genre,
                          'collaboration':songs_451_460.collaboration,
                          'year':songs_451_460.year})
song_451_460

# 461_470
songs_461_470 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_461_470.p", "rb" ) )
songs_461_470
song_461_470 = pd.DataFrame({'song':songs_461_470.song,
                          'artist':songs_461_470.artist,
                          'lyrics':songs_461_470.lyrics,
                          'genre':songs_461_470.genre,
                          'collaboration':songs_461_470.collaboration,
                          'year':songs_461_470.year})
song_461_470

# 471_480
songs_471_480 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_471_480.p", "rb" ) )
songs_471_480
song_471_480 = pd.DataFrame({'song':songs_471_480.song,
                          'artist':songs_471_480.artist,
                          'lyrics':songs_471_480.lyrics,
                          'genre':songs_471_480.genre,
                          'collaboration':songs_471_480.collaboration,
                          'year':songs_471_480.year})
song_471_480

# 481_490
songs_481_490 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_481_490.p", "rb" ) )
songs_481_490
song_481_490 = pd.DataFrame({'song':songs_481_490.song,
                          'artist':songs_481_490.artist,
                          'lyrics':songs_481_490.lyrics,
                          'genre':songs_481_490.genre,
                          'collaboration':songs_481_490.collaboration,
                          'year':songs_481_490.year})
song_481_490

# 491_500
songs_491_500 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_491_500.p", "rb" ) )
songs_491_500
song_491_500 = pd.DataFrame({'song':songs_491_500.song,
                          'artist':songs_491_500.artist,
                          'lyrics':songs_491_500.lyrics,
                          'genre':songs_491_500.genre,
                          'collaboration':songs_491_500.collaboration,
                          'year':songs_491_500.year})
song_491_500

# Stack dataframes
songs = [song_401_410,song_411_420,song_421_430,song_431_440,song_441_450,song_451_460,song_461_470,song_471_480,song_481_490,song_491_500]
songs


db_2013 = pd.concat(songs)
db_2013
db_2013.genre

### Dump df
pickle.dump( db_2013, open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2013.p", "wb" ) )

songs_2013 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2013.p", "rb" ) )

songs_2013
songs_2013.song

##################################################################
##################################################################     2012
##################################################################

# 501_510
songs_501_510 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_501_510.p", "rb" ) )
songs_501_510
song_501_510 = pd.DataFrame({'song':songs_501_510.song,
                          'artist':songs_501_510.artist,
                          'lyrics':songs_501_510.lyrics,
                          'genre':songs_501_510.genre,
                          'collaboration':songs_501_510.collaboration,
                          'year':songs_501_510.year})
song_501_510

# 511_520
songs_511_520 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_511_520.p", "rb" ) )
songs_511_520
song_511_520 = pd.DataFrame({'song':songs_511_520.song,
                          'artist':songs_511_520.artist,
                          'lyrics':songs_511_520.lyrics,
                          'genre':songs_511_520.genre,
                          'collaboration':songs_511_520.collaboration,
                          'year':songs_511_520.year})
song_511_520

# 521_530
songs_521_530 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_521_530.p", "rb" ) )
songs_521_530
song_521_530 = pd.DataFrame({'song':songs_521_530.song,
                          'artist':songs_521_530.artist,
                          'lyrics':songs_521_530.lyrics,
                          'genre':songs_521_530.genre,
                          'collaboration':songs_521_530.collaboration,
                          'year':songs_521_530.year})
song_521_530

# 531_540
songs_531_540 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_531_540.p", "rb" ) )
songs_531_540
song_531_540 = pd.DataFrame({'song':songs_531_540.song,
                          'artist':songs_531_540.artist,
                          'lyrics':songs_531_540.lyrics,
                          'genre':songs_531_540.genre,
                          'collaboration':songs_531_540.collaboration,
                          'year':songs_531_540.year})
song_531_540

# 541_550
songs_541_550 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_541_550.p", "rb" ) )
songs_541_550
song_541_550 = pd.DataFrame({'song':songs_541_550.song,
                          'artist':songs_541_550.artist,
                          'lyrics':songs_541_550.lyrics,
                          'genre':songs_541_550.genre,
                          'collaboration':songs_541_550.collaboration,
                          'year':songs_541_550.year})
song_541_550

# 551_560
songs_551_560 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_551_560.p", "rb" ) )
songs_551_560
song_551_560 = pd.DataFrame({'song':songs_551_560.song,
                          'artist':songs_551_560.artist,
                          'lyrics':songs_551_560.lyrics,
                          'genre':songs_551_560.genre,
                          'collaboration':songs_551_560.collaboration,
                          'year':songs_551_560.year})
song_551_560

# 561_570
songs_561_570 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_561_570.p", "rb" ) )
songs_561_570
song_561_570 = pd.DataFrame({'song':songs_561_570.song,
                          'artist':songs_561_570.artist,
                          'lyrics':songs_561_570.lyrics,
                          'genre':songs_561_570.genre,
                          'collaboration':songs_561_570.collaboration,
                          'year':songs_561_570.year})
song_561_570

# 571_580
songs_571_580 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_571_580.p", "rb" ) )
songs_571_580
song_571_580 = pd.DataFrame({'song':songs_571_580.song,
                          'artist':songs_571_580.artist,
                          'lyrics':songs_571_580.lyrics,
                          'genre':songs_571_580.genre,
                          'collaboration':songs_571_580.collaboration,
                          'year':songs_571_580.year})
song_571_580


# 581_590
songs_581_590 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_songs/songs_581_590.p", "rb" ) )
songs_581_590
song_581_590 = pd.DataFrame({'song':songs_581_590.song,
                          'artist':songs_581_590.artist,
                          'lyrics':songs_581_590.lyrics,
                          'genre':songs_581_590.genre,
                          'collaboration':songs_581_590.collaboration,
                          'year':songs_581_590.year})
song_581_590


# Stack dataframes
songs = [song_501_510,song_511_520,song_521_530,song_531_540,song_541_550,song_551_560,song_561_570,song_571_580,song_581_590]
songs


db_2012 = pd.concat(songs)
db_2012
db_2012.genre

### Dump df
pickle.dump( db_2012, open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2012.p", "wb" ) )

songs_2012 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2012.p", "rb" ) )

songs_2012
songs_2012.song



##################################################################
##################################################################     
##################################################################

###
### Combine all years and fix missing genres
###

songs_2017 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2017.p", "rb" ) )
songs_2017

songs_2016 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2016.p", "rb" ) )
songs_2016

songs_2015 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2015.p", "rb" ) )
songs_2015

songs_2014 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2014.p", "rb" ) )
songs_2014

songs_2013 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2013.p", "rb" ) )
songs_2013

songs_2012 = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_years/db_2012.p", "rb" ) )
songs_2012

### Stack to make df
songs = [songs_2017,songs_2016,songs_2015,songs_2014,songs_2013,songs_2012]
songs

song_db = pd.concat(songs)
song_db

###
### Begin reclassifining genres
###

#gets freq of genres
song_db.groupby('genre').count()

# make new genre variable
song_db.new_genre = song_db.genre

# reclassify some genres
song_db.loc[song_db.genre == 'dance','new_genre'] = 'pop'
song_db.loc[song_db.genre == 'hip hop','new_genre'] = 'hip-hop'
song_db.loc[song_db.genre == 'hip hop','new_genre'] = 'hip-hop'
song_db.loc[song_db.genre == 'indie','new_genre'] = 'pop'
song_db.loc[song_db.genre == 'rap','new_genre'] = 'hip-hop'


song_db.groupby('new_genre').count()

###
### Check out missings
###

miss_genre = song_db.loc[song_db['genre'] == 'MISSING']
miss_genre
len(miss_genre)
new_genre = ["pop" , "pop" , "hip-hop" , "hip-hop" , "hip-hop" , "hip-hop" , "pop" , "pop" , "hip-hop" , "pop" , "pop" , "hip-hop" , "other" , "pop" , "pop" , "pop" , "hip-hop" , "hip-hop" , "hip-hop" , "pop" , "pop" , "pop" , "pop" , "hip-hop" , "pop" , "pop" , "hip-hop" , "country" , "pop" , "pop" , "pop" , "pop" , "pop" , "pop" , "hip-hop" , "pop" , "pop" , "country"]

miss_genre['genre'] = new_genre

new_missed_genre_dataframe = pd.DataFrame({'song':miss_genre.song,
                          'artist':miss_genre.artist,
                          'lyrics':miss_genre.lyrics,
                          'genre':miss_genre.genre,
                          'collaboration':miss_genre.collaboration,
                          'year':miss_genre.year})
new_missed_genre_dataframe

###
### Take out missings from original database
###

non_miss = song_db[song_db.genre != 'MISSING']

# Create df from this then merge to missing with new genres

songs_w_genre = pd.DataFrame({'song':non_miss.song,
                          'artist':non_miss.artist,
                          'lyrics':non_miss.lyrics,
                          'genre':non_miss.new_genre,
                          'collaboration':non_miss.collaboration,
                          'year':non_miss.year})
songs_w_genre

stacked = [songs_w_genre,new_missed_genre_dataframe]
new_db = pd.concat(stacked)

sorted_db = new_db.sort_index()
sorted_db
sorted_db.loc[85]

sorted_db.loc[200]

sorted_db.lyrics[1]

###
### PICKLE THAT DATAFRAME AND LETS GOOOOOOOO
###

pickle.dump( sorted_db, open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_final_db/final_db.p", "wb" ) )



###
### Fixing some genres
###

# Load in df
song_db = pickle.load( open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_final_db/final_db.p", "rb" ) )
song_db

# reclassify songs
song_db.loc[song_db.song == 'Wild Thoughts', 'genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Everyday We Lit', 'genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Starboy','genre'] = 'pop'
song_db.loc[song_db.song == 'Location','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Redbone','genre'] = 'pop'
song_db.loc[song_db.song == 'iSpy','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Rockabye','genre'] = 'pop'
song_db.loc[song_db.song == 'Broccoli','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Love Galore','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Swalla','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Small Town Boy','genre'] = 'country'
song_db.loc[song_db.song == 'This Is What You Came For','genre'] = 'pop'
song_db.loc[song_db.song == 'Ride','genre'] = 'rock'
song_db.loc[song_db.song == 'The Hills','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Broccoli','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Gold','genre'] = 'pop'
song_db.loc[song_db.song == 'Exchange','genre'] = 'hip-hop'
song_db.loc[song_db.song == '679','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Oui','genre'] = 'hip-hop'
song_db.loc[song_db.song == '2 Phones','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Starboy','genre'] = 'pop'
song_db.loc[song_db.song == 'Sucker For Pain','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Luv','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Back To Sleep','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'No Limit','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'The Hills','genre'] = 'hip-hop'
song_db.loc[song_db.song == '679','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Post To Be','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Hey Mama','genre'] = 'pop'
song_db.loc[song_db.song == 'What Do You Mean?','genre'] = 'pop'
song_db.loc[song_db.song == 'Cool For The Summer','genre'] = 'pop'
song_db.loc[song_db.song == 'The Hanging Tree','genre'] = 'pop'
song_db.loc[song_db.song == 'Hit The Quan','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Rude','genre'] = 'pop'
song_db.loc[song_db.song == 'Let Her Go','genre'] = 'pop'
song_db.loc[song_db.song == 'Latch','genre'] = 'pop'
song_db.loc[song_db.song == "Ain't It Fun",'genre'] = 'rock'
song_db.loc[song_db.song == 'Trumpets','genre'] = 'pop'
song_db.loc[song_db.song == 'Stay The Night','genre'] = 'pop'
song_db.loc[song_db.song == 'Get Lucky','genre'] = 'pop'
song_db.loc[song_db.song == 'Sail','genre'] = 'rock'
song_db.loc[song_db.song == "Don't You Worry Child",'genre'] = 'pop'
song_db.loc[song_db.song == 'Try','genre'] = 'pop'
song_db.loc[song_db.song == 'Bad','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Body Party','genre'] = 'pop'
song_db.loc[song_db.song == 'Adorn','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Let Her Go','genre'] = 'pop'
song_db.loc[song_db.song == 'Climax','genre'] = 'pop'
song_db.loc[song_db.song == 'Heart Attack','genre'] = 'hip-hop'
song_db.loc[song_db.song == 'Adorn','genre'] = 'hip-hop'




pickle.dump( song_db, open( "/Users/brettharder/Documents/Categorical Data/Project/01_Data/pickled_final_db/final_db.p", "wb" ) )








