###
### Create scrape-able song db
###

import pandas as pd
import numpy as np

raw_song_db = pd.read_csv("/Users/brettharder/Documents/GitHub/BB_Top100/Data/Raw/Songs_2018.csv")
raw_song_db

raw_song_db.shape

raw_song_db.columns

###
### Create trimmed songs for lyric and genre scrape
###

songs_lyric_scrape = [x.lower().replace(" ","") for x in raw_song_db.song]
songs_genre_scrape = [x.lower().replace(" ","+") for x in raw_song_db.song]


###
### Create trimmed artist for lyric and genre scrape, and collaboration flag
###

# Lower artist names
lower_artists = [x.lower() for x in raw_song_db.artist]
lower_artists

len(lower_artists)


# Create collaboration flag
collaboration_flag = []
for i in range(0,len(lower_artists)):
    if "&" in lower_artists[i] or "featuring" in lower_artists[i]:
        collaboration_flag.append(1)
    else:
        collaboration_flag.append(0)
collaboration_flag


# Trim artist with "&" or "featuring"
artist_trimmed = []
for i in range(0,len(lower_artists)):
    if "&" and "featuring" in lower_artists[i]:
        if len(lower_artists[i].split("featuring")[0]) < len(lower_artists[i].split("&")[0]):
            artist_trimmed.append(lower_artists[i].split("featuring")[0].strip())
        else:
            artist_trimmed.append(lower_artists[i].split("&")[0].strip())
    elif "&" in lower_artists[i]:
        artist_trimmed.append(lower_artists[i].split("&")[0].strip())
    elif "featuring" in lower_artists[i]:
        artist_trimmed.append(lower_artists[i].split("featuring")[0].strip())
    else:
        artist_trimmed.append(lower_artists[i])
artist_trimmed 


artist_lyric_scrape = [x.lower().replace(" ","") for x in artist_trimmed]
artist_genre_scrape = [x.lower().replace(" ","+") for x in artist_trimmed]

artist_lyric_scrape
artist_genre_scrape

processed_song_db = pd.DataFrame({'song':raw_song_db.song,
                                  'song_lyric_scrape':songs_lyric_scrape,
                                  'song_genre_scrape': songs_genre_scrape,
                                  'artist':raw_song_db.artist,
                                  'artist_lyric_scape':artist_lyric_scrape,
                                  'artist_genre_scrape':artist_genre_scrape,
                                  'collaboration':collaboration_flag,
                                  'year':raw_song_db.year})
processed_song_db

processed_song_db.to_csv('/Users/brettharder/Documents/GitHub/BB_Top100/Data/Published/cleaned_2018_song_db.csv',index=False)












 

