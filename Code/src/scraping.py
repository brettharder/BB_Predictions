# -----------------------------
# Functionality to scrape songs
# -----------------------------

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import collections, re
import numpy as np

import pandas as pd
import time

import sys
sys.path

def song_scrape(df,start_row,end_row,scrape_timer):
    """
    args:
        df: dataframe of songs to scrape
        start_row: row to start scrape of data
        end_row: row-1 of data to scrape
        scrape_timer: time between scrapes
    """
    
    # Subset to start and end rows to scrape
    sample_df = df[start_row:end_row]
    sample_df = sample_df.reset_index()
    
    # Initialize lyrics, lyric_bag of words, and genre lists
    scraped_song_lyrics = []
    lyric_bag = []
    song_genre = []

    # Loop through start and end_row to scrape
    for i in sample_df.index:
        
        # Scrape lyrics and output list of all lyrics
        lyrics_list = scrape_lyrics(sample_df,i)
        
        # Format list as a string
        song_str = format_lyrics(lyrics_list)
        
        # Append string to scraped_song_lyrics (list of all lyric strings)
        scraped_song_lyrics.append(song_str)
        
        # Create bag-of-words from lyrics_list
        song_bag = create_bag_of_words(lyrics_list)
        
        # Append song_bag to lyric_bag
        lyric_bag.append(song_bag)
        
    
        ##### GENRE SCRAPE
        genre = scrape_genre(sample_df,i)
        song_genre.append(genre)
        
        time.sleep(scrape_timer)
    
    # Return scraped_song_lyrics, lyric_bag, and song_genre
    return scraped_song_lyrics, lyric_bag, song_genre
    
    
# Scrape lyrics function

def scrape_lyrics(df,row):
    """
    args:
        df: sample of df to scrape rows
        row: row of df to scrape
    
    returns:
        list of all song lyrics
    """
    
    # Read page 
    quote_page = "https://www.azlyrics.com/lyrics/" + df.artist_lyric_scrape[row] + "/"+ df.song_lyric_scrape[row]+".html"
    
    # Use url commands to convert to html
    page = urlopen(quote_page)
    
    # BeautifulSoup will parse html
    soup = BeautifulSoup(page, "html.parser")
    
    # Use HTML tag to get web data
    name_box = soup.find("div",attrs={"class":"col-xs-12 col-lg-8 text-center"})
    name = name_box.text.strip()
    
    # Split lines
    line_split = name.splitlines()
    
    start_lyric = line_split.index("\"" + df.song[row] +"\"")
    end_lyric = line_split.index("if  ( /Android|webOS|iPhone|iPod|iPad|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) ")
    
    lyric_lines = line_split[start_lyric:end_lyric]
    
    return lyric_lines


def format_lyrics(lyric_list):
    """
    args:
        lyric_list: output from scrape_lyrics
    returns:
        string of song lyrics w/ original order
    """
    # Creates string of all lryics in song
    song_lyrics_str = ' '.join(map(str, lyric_list))
    
    return song_lyrics_str


def create_bag_of_words(lyric_lines):
    """
    args:
        lyric_lines: output from scrape_lyrics
    returns:
        dictionary of bag of words {lyric:freq}
    """
    # Create bag of words
    bagofwords = [ collections.Counter(re.findall(r'\w+', txt.lower())) for txt in lyric_lines]
    sumbag = sum(bagofwords, collections.Counter())
    
    # Create dictionary of words 
    bag = dict(sumbag)
    
    return bag

def scrape_genre(df,row):
    # Read page 
    quote_page = "https://www.last.fm/music/" + df.artist_genre_scrape[row] + "/_/" + df.song_genre_scrape[row]
    # Use url commands to convert to html
    page = urlopen(quote_page)
    # BeautifulSoup will parse html
    soup = BeautifulSoup(page, "html.parser")
    
    # Use HTML tag to get web data
    name_box = soup.find("ul",attrs={"class":"tags-list tags-list--global"})  
    if name_box == None:
        return 'MISSING'
    else:
        name = name_box.text.strip()
    
        genres = ["hip-hop","pop","hip hop","rap","country","rock","indie","latin pop"]
        genre_rank = {}
        count = 0
        for i in genres:
            if i in name:
                genre_rank[i] = count
                count = count + 1
    
        if genre_rank == {}:
            genre_rank = {'other':0}
        return min(genre_rank, key=genre_rank.get)
    



