import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

arquivo_csv = "auto-mpg.csv"  
df = pd.read_csv(arquivo_csv)

df.replace('?', np.nan, inplace=True)
df = df.apply(pd.to_numeric, errors='coerce')
df.dropna(inplace=True)

X = df[["cylinders", "displacement", "horsepower", "weight", "acceleration"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)

df['cluster'] = kmeans.fit_predict(X_scaled)

plt.scatter(df['weight'], df['acceleration'], c=df['cluster'], cmap='viridis')
plt.xlabel('Peso')
plt.ylabel('Aceleração')
plt.title('Clusterização K-means (3 clusters)')
plt.colorbar(label='Cluster')
plt.show()

centroids = kmeans.cluster_centers_
centroids = scaler.inverse_transform(centroids) 
print("Centros dos clusters:")
print(centroids)
