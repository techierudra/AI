# Import required libraries
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


# Generate random data
np.random.seed(0)
points = np.random.randn(100, 2)


# Create a KMeans instance with 2 clusters (we choose 2 arbitrarily)
kmeans = KMeans(n_clusters=2)


# Fit the model to the data
kmeans.fit(points)


# Get the cluster assignments for each data point
labels = kmeans.labels_


# Plot the data points colored by their cluster assignments
plt.scatter(points[:, 0], points[:, 1], c=labels)
plt.show()