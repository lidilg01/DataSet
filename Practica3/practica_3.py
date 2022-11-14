import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns

df_a = pd.read_csv("DataFrame/Viki_sorted.csv")

print(df_a["imdb_score"].mean()) 
print(df_a["imdb_score"].min()) 
print(df_a["imdb_score"].max()) 
print(df_a["imdb_score"].describe())

print(df_a["tmdb_score"].mean()) 
print(df_a["tmdb_score"].min()) 
print(df_a["tmdb_score"].max()) 
print(df_a["tmdb_score"].describe())

