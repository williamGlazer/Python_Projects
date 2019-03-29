#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as p
from sklearn.cluster import AgglomerativeClustering

from datasets import (
        circles,
        moons,
        blobs,
        anisotropic,
        random,
        varied_variances
)

'''
PLAY WITH LINKAGE
FOR DIFFERENT RESULTS
'''



X= circles()

hac = AgglomerativeClustering(n_clusters=2, linkage='single')
hac.fit(X)

p.figure()
p.scatter(X[:,0], X[:,1], c=hac.labels_)
p.tight_layout()
p.show()


X= moons()

hac = AgglomerativeClustering(n_clusters=2, linkage='single')
hac.fit(X)

p.figure()
p.scatter(X[:,0], X[:,1], c=hac.labels_)
p.tight_layout()
p.show()


X= blobs()

hac = AgglomerativeClustering(n_clusters=3, linkage='single')
hac.fit(X)

p.figure()
p.scatter(X[:,0], X[:,1], c=hac.labels_)
p.tight_layout()
p.show()



X= anisotropic()

hac = AgglomerativeClustering(n_clusters=3, linkage='single')
hac.fit(X)

p.figure()
p.scatter(X[:,0], X[:,1], c=hac.labels_)
p.tight_layout()
p.show()



X= random()

hac = AgglomerativeClustering(n_clusters=2, linkage='ward')
hac.fit(X)

p.figure()
p.scatter(X[:,0], X[:,1], c=hac.labels_)
p.tight_layout()
p.show()





X= varied_variances()

hac = AgglomerativeClustering(n_clusters=3, linkage='ward')
hac.fit(X)

p.figure()
p.scatter(X[:,0], X[:,1], c=hac.labels_)
p.tight_layout()
p.show()