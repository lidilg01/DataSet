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

#--- imdb and year---
y = df["imdb_score"]
x = df["release_year"] 

n = len(x)
x = np.array(x)
y = np.array(y)

sumx = sum(x)

sumy = sum(y)

sumx2 = sum(x*x)

sumy2 = sum(y*y)

sumxy = sum(x*y)

promx = sumx/n

promy = sumy/n

m = (sumx*sumy - n * sumxy)/(sumx**2 - n * sumx2)

b = promy - m * promx
sigmax = np.sqrt(sumx2/n - promx**2)
sigmay = np.sqrt(sumy2/n - promy**2)
sigmaxy = sumxy/n - promx * promy
R2 = (sigmaxy/(sigmax*sigmay))**2

print(R2)
print(m)

plt.plot(x, y, 'o', label='Datos')
plt.plot(x, m * x + b, label='Ajuste')
plt.grid()
plt.savefig('Graficas/regression_imdb_score.png')
plt.show()

#---- tmdb and year----

y = df["tmdb_score"]
x = df["release_year"] 

n = len(x)
x = np.array(x)
y = np.array(y)

sumx = sum(x)

sumy = sum(y)

sumx2 = sum(x*x)

sumy2 = sum(y*y)

sumxy = sum(x*y)

promx = sumx/n

promy = sumy/n

m = (sumx*sumy - n * sumxy)/(sumx**2 - n * sumx2)

b = promy - m * promx
sigmax = np.sqrt(sumx2/n - promx**2)
sigmay = np.sqrt(sumy2/n - promy**2)
sigmaxy = sumxy/n - promx * promy
R2 = (sigmaxy/(sigmax*sigmay))**2

print(R2)
print(m)

plt.plot(x, y, 'o', label='Datos')
plt.plot(x, m * x + b, label='Ajuste')
plt.grid()
plt.savefig('Graficas/regression_tmdb_score.png')
plt.show()


# ----------------- runtime and year---------------
y = df["runtime"]
x = df["release_year"] 

n = len(x)
x = np.array(x)
y = np.array(y)

sumx = sum(x)

sumy = sum(y)

sumx2 = sum(x*x)

sumy2 = sum(y*y)

sumxy = sum(x*y)

promx = sumx/n

promy = sumy/n

m = (sumx*sumy - n * sumxy)/(sumx**2 - n * sumx2)

b = promy - m * promx
sigmax = np.sqrt(sumx2/n - promx**2)
sigmay = np.sqrt(sumy2/n - promy**2)
sigmaxy = sumxy/n - promx * promy
R2 = (sigmaxy/(sigmax*sigmay))**2

print(R2)
print(m)

plt.plot(x, y, 'o', label='Datos')
plt.plot(x, m * x + b, label='Ajuste')
plt.grid()
plt.show()


#---------- seasons and year
y = df["seasons"]
x = df["release_year"] 

n = len(x)
x = np.array(x)
y = np.array(y)

sumx = sum(x)

sumy = sum(y)

sumx2 = sum(x*x)

sumy2 = sum(y*y)

sumxy = sum(x*y)

promx = sumx/n

promy = sumy/n

m = (sumx*sumy - n * sumxy)/(sumx**2 - n * sumx2)

b = promy - m * promx
sigmax = np.sqrt(sumx2/n - promx**2)
sigmay = np.sqrt(sumy2/n - promy**2)
sigmaxy = sumxy/n - promx * promy
R2 = (sigmaxy/(sigmax*sigmay))**2

print(R2)
print(m)

plt.plot(x, y, 'o', label='Datos')
plt.plot(x, m * x + b, label='Ajuste')
plt.grid()
plt.show()
