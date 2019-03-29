#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering


# Read
cc_data = pd.read_csv('CC_GENERAL.csv', index_col=False)


# Plot CREDIT_LIMIT v. BALANCE
cc_data.plot.scatter(x='CREDIT_LIMIT', y='BALANCE')
plt.show()


# Graph of Elbow Method
subsample = cc_data.sample(1000,random_state=17)
X = pd.concat([subsample['CREDIT_LIMIT'],subsample['BALANCE']],axis=1)

wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.figure() 
plt.scatter(range(1,11), wcss)
plt.show()
#elbow is 3 or 4


# train kMeans on X & plot with colors
kmeans = KMeans(n_clusters=3, random_state=17)
kmeans.fit(X)

plt.figure()
plt.scatter(X['CREDIT_LIMIT'],X['BALANCE'], c=kmeans.labels_)
plt.tight_layout()
plt.axis('equal')
plt.show()


kmeans = KMeans(n_clusters=4, random_state=17)
kmeans.fit(X)

plt.figure()
plt.scatter(X['CREDIT_LIMIT'],X['BALANCE'], c=kmeans.labels_)
plt.tight_layout()
plt.axis('equal')
plt.show()


#DBSCAN BAD CHOICE SINCE VARIABLE VARIANCE


# Let's try HAC
hac = AgglomerativeClustering(n_clusters=5, linkage='ward')
hac.fit(X)

plt.figure()
plt.scatter(X['CREDIT_LIMIT'],X['BALANCE'], c=hac.labels_)
plt.tight_layout()
plt.show()
