#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as p
from sklearn.cluster import DBSCAN

from datasets import (
        circles,
        moons,
        blobs,
        anisotropic,
        random,
        varied_variances
)



# Circle Demonstration, Works!
X = circles()

dbscan = DBSCAN(eps=0.11, min_samples=5)
dbscan.fit(X)

# Get inliers & Outliers
X_inlier = X[dbscan.labels_ != -1]
y_inlier = dbscan.labels_[dbscan.labels_ != -1]

X_outlier = X[dbscan.labels_ == -1]

p.figure()
p.scatter(X_inlier[:,0], X_inlier[:,1], c=y_inlier, cmap='Dark2')
p.scatter(X_outlier[:,0], X_outlier[:,1], c='k')
p.tight_layout()
p.show()




# Moons Demonstration, Works!
X = moons()

dbscan = DBSCAN(eps=0.1, min_samples=5)
dbscan.fit(X)

# Get inliers & Outliers
X_inlier = X[dbscan.labels_ != -1]
y_inlier = dbscan.labels_[dbscan.labels_ != -1]

X_outlier = X[dbscan.labels_ == -1]

p.figure()
p.scatter(X_inlier[:,0], X_inlier[:,1], c=y_inlier, cmap='Dark2')
p.scatter(X_outlier[:,0], X_outlier[:,1], c='k')
p.tight_layout()
p.show()




# Blobs Demonstration, Works!
X = blobs()

dbscan = DBSCAN(eps=0.75, min_samples=5)
dbscan.fit(X)

# Get inliers & Outliers
X_inlier = X[dbscan.labels_ != -1]
y_inlier = dbscan.labels_[dbscan.labels_ != -1]

X_outlier = X[dbscan.labels_ == -1]

p.figure()
p.scatter(X_inlier[:,0], X_inlier[:,1], c=y_inlier, cmap='Dark2')
p.scatter(X_outlier[:,0], X_outlier[:,1], c='k')
p.tight_layout()
p.show()



# Anisotropic Demonstration, Works!
X = anisotropic()

dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan.fit(X)

# Get inliers & Outliers
X_inlier = X[dbscan.labels_ != -1]
y_inlier = dbscan.labels_[dbscan.labels_ != -1]

X_outlier = X[dbscan.labels_ == -1]

p.figure()
p.scatter(X_inlier[:,0], X_inlier[:,1], c=y_inlier, cmap='Dark2')
p.scatter(X_outlier[:,0], X_outlier[:,1], c='k')
p.tight_layout()
p.show()




# random Demonstration, Works!
X = random()

dbscan = DBSCAN(eps=0.1, min_samples=5)
dbscan.fit(X)

# Get inliers & Outliers
X_inlier = X[dbscan.labels_ != -1]
y_inlier = dbscan.labels_[dbscan.labels_ != -1]

X_outlier = X[dbscan.labels_ == -1]

p.figure()
p.scatter(X_inlier[:,0], X_inlier[:,1], c=y_inlier, cmap='Dark2')
p.scatter(X_outlier[:,0], X_outlier[:,1], c='k')
p.tight_layout()
p.show()




# Varied_variances Demonstration, ~Works Because varied variences but DBSCAN
# has a fixed Variance!
X = varied_variances()

dbscan = DBSCAN(eps=1.5, min_samples=5)
dbscan.fit(X)

# Get inliers & Outliers
X_inlier = X[dbscan.labels_ != -1]
y_inlier = dbscan.labels_[dbscan.labels_ != -1]

X_outlier = X[dbscan.labels_ == -1]

p.figure()
p.scatter(X_inlier[:,0], X_inlier[:,1], c=y_inlier, cmap='Dark2')
p.scatter(X_outlier[:,0], X_outlier[:,1], c='k')
p.tight_layout()
p.show()