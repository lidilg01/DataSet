import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime

df = pd.read_csv("DataFrame/Viki.csv")

df = df.drop(['age_certification'], axis=1)
df = df.dropna(subset='description')
df = df.dropna(subset='imdb_id')

#print(df["imdb_score"].mean()) 
#print(df["imdb_score"].min()) 
#print(df["imdb_score"].max()) 
#print(df["imdb_score"].describe())

#print(df["tmdb_score"].mean()) 
#print(df["tmdb_score"].min()) 
#print(df["tmdb_score"].max()) 
#print(df["tmdb_score"].describe())

df.to_csv("DataFrame/Viki_ab.csv", index=False)

df = df.fillna({'seasons':0,'imdb_votes':0,'imdb_score':7.08,'tmdb_score':7.28,'tmdb_popularity':8.71}) 
df = df.sort_values(by=["release_year"])
df.to_csv("DataFrame/Viki_sorted.csv", index=False)
