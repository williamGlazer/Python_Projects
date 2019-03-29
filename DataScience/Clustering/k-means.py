# -*- coding: utf-8 -*-

'''
K-MEANS WORKS WELL ON AGGREGATIONS
NOT SO WELL ON CIRCULAR SHAPES
'''

import matplotlib.pyplot as p
from sklearn.cluster import KMeans

from datasets import (
        circles,
        moons,
        blobs,
        anisotropic,
        random,
        varied_variances
)



# Circle Demonstration, sucks -> splits circle in 2 sides (left & right)
X = circles()

kmeans = KMeans(n_clusters=2, random_state=17)
kmeans.fit(X)

p.figure()
p.scatter(X[:,0],X[:,1], c=kmeans.labels_)
p.tight_layout()
p.show()




# Moon Demonstration, sucks -> splits Moons in 2 sides (left & right)
X = moons()

kmeans = KMeans(n_clusters=2, random_state=17)
kmeans.fit(X)

p.figure()
p.scatter(X[:,0],X[:,1], c=kmeans.labels_)
p.tight_layout()
p.show()



# Blobs Demonstration, Works!
X = blobs()

kmeans = KMeans(n_clusters=3, random_state=17)
kmeans.fit(X)

p.figure()
p.scatter(X[:,0],X[:,1], c=kmeans.labels_)
p.tight_layout()
p.show()



# Anisotropic Demonstration, Works!
X = anisotropic()

kmeans = KMeans(n_clusters=3, random_state=17)
kmeans.fit(X)

p.figure()
p.scatter(X[:,0],X[:,1], c=kmeans.labels_)
p.tight_layout()
p.show()




# Radnom Demonstration, ~Works because are there really clusters?
X = random()

kmeans = KMeans(n_clusters=7, random_state=17)
kmeans.fit(X)

p.figure()
p.scatter(X[:,0],X[:,1], c=kmeans.labels_)
p.tight_layout()
p.show()




# Varied_variances Demonstration, Farily Works 
X = varied_variances()

kmeans = KMeans(n_clusters=3, random_state=17)
kmeans.fit(X)

p.figure()
p.scatter(X[:,0],X[:,1], c=kmeans.labels_)
p.tight_layout()
p.show()