'''dEMONSTRATION of K Means Clustering
Requires : python 2.7.x, Numpy 1.7.1+, Matplotlib, 1.2.1+'''
import sys
import numpy as np

# generate 3 cluster data
# data = np.genfromtxt('data1.csv', delimiter=',')
m1, cov1 = [9, 8], [[1.5, 2], [1, 2]]
m2, cov2 = [5, 13], [[2.5, -1.5], [-1.5, 1.5]]
m3, cov3 = [3, 7], [[0.25, 0.5], [-0.1, 0.5]]
data1 = np.random.multivariate_normal(m1, cov1, 250)
data2 = np.random.multivariate_normal(m2, cov2, 180)
data3 = np.random.multivariate_normal(m3, cov3, 100)
X = np.vstack((data1,np.vstack((data2,data3))))
print X
np.random.shuffle(X)

from kmeans import kMeans
centroids, C = kMeans(X, K = 3)