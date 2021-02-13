#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 06:48:22 2021

@author: nuvilabs
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()
import numpy as np
class KMean:
    def __init__(self,k,max_iter=300):
        """
        Parameters
        ----------
        k : The number of clusters to form as well as the number of centroids to generate.
        max_iter : Maximum number of iterations of the k-means algorithm for a single run.
        Returns
        -------
        None.
        """
        self.k = k
        self.centroids = None
        self.max_iter = max_iter
        
    def initialize_centroids(self, points, k):
        """returns k centroids from the initial points"""
        centroids = points.copy()
        np.random.shuffle(centroids)
        return centroids[:k]
    
    def closest_centroid(self, points, centroids):
        """returns an array containing the index to the nearest centroid for each point"""
        distances = np.sqrt(((points - centroids[:, np.newaxis])**2).sum(axis=2))
        
        return np.argmin(distances, axis=0)
    def move_centroids(self, points, closest, centroids):
        """returns the new centroids assigned from the points closest to them"""
        return np.array([points[closest==k].mean(axis=0) for k in range(centroids.shape[0])])
    
    def fit(self, points):
        self.centroids = self.initialize_centroids(points, self.k)
        centroids = None
        for i in range(self.max_iter):
            closest = self.predict(points)
            self.centroids = self.move_centroids(points, closest, self.centroids)
        return closest 
    
    def predict(self, points):
        closest = self.closest_centroid(points, self.centroids)
        return closest 
    


if __name__=='__main__':                  
    k = KMean(5)
    points = np.vstack(((np.random.randn(150, 2) * 0.75 + np.array([1, 0])),
                      (np.random.randn(50, 2) * 0.25 + np.array([-0.5, 0.5])),
                      (np.random.randn(50, 2) * 0.5 + np.array([-0.5, -0.5]))))
    closest = k.fit(points)
    fig = plt.figure()
    
    ax = plt.axes(xlim=(-4, 4), ylim=(-4, 4))
    
    ax.cla()
    ax.scatter(points[:, 0], points[:, 1], c=closest)
    ax.scatter(k.centroids[:, 0], k.centroids[:, 1], c='r', s=100)