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

sns.displot(df_a["release_year"])
plt.savefig('Graficas/distplt_releaseyear.png')
plt.show()

sns.lineplot(df_a["release_year"])
plt.savefig('Graficas/lineplt_releaseyear.png')
plt.show()


sns.displot(df_a["production_countries"])
plt.xticks(rotation=90)
plt.savefig('Graficas/displt_countries.png')
plt.show()


sns.boxplot(x = df_a["type"], y = df_a["release_year"])
plt.savefig('Graficas/boxplt_typereleaseyear.png')
plt.show()

sns.boxplot(x = df_a["imdb_score"], y = df_a["release_year"])
plt.xticks(rotation=90)
plt.savefig('Graficas/boxplt_imdbscore.png')
plt.show()

sns.boxplot(x = df_a["type"], y = df_a["imdb_score"])
plt.savefig('Graficas/boxplt_imdbtype.png')
plt.show()

sns.boxplot(x = df_a["type"], y = df_a["tmdb_score"])
plt.savefig('Graficas/boxplt_tmdbtype.png')
plt.show()

sns.histplot(df_a["seasons"], binwidth=1)
plt.savefig('Graficas/seasons.png')
plt.show()

sns.displot(df_a["imdb_score"])
plt.savefig('Graficas/imdb_score.png')
plt.show()

sns.displot(df_a["tmdb_score"])
plt.savefig('Graficas/tmdb_score.png')
plt.show()






