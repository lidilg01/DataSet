import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import numpy as np
import scipy.stats as stats

df = pd.read_csv("DataFrame/Viki_sorted.csv")

grp1 = df["imdb_score"]
grp2 = df["tmdb_score"]

#prueba estadistica para comprobar si las distribuciones son iguales
# hipotesis nula = las distribuciones de los grupos son iguales
# hipotesis alterna = las distribuciones de los grupos son diferentes

# conduct the Wilcoxon-Signed Rank Test
print(stats.wilcoxon(grp1, grp2))

# resultado WilcoxonResult(statistic=359085.0, pvalue=3.5022733907091873e-16)
#Como el valor de p es mayor a 0.05 aceptamos la hipotesis nula por tanto
# las distribuciones son iguales