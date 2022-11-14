import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyparsing import line
from sklearn.cluster import KMeans

df = pd.read_csv("DataFrame/Viki_sorted.csv")

x = df['release_year'].values

y = df['imdb_score'].values

X = np.array(list(zip(x, y)))


kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
labels = kmeans.predict(X)

centroids = kmeans.cluster_centers_

color = ['m.', 'r.', 'c.', 'y.', 'b.']

for i in range(len(X)):
    print('Coordenada: ', X[i], 'Label: ', labels[i])
    plt.plot(X[i][0], X[i][1], color[labels[i]], markersize=10)

plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='+', s=150, linewidths=1, zorder=10)
plt.savefig('Graficas/kmeans.png')
plt.show()