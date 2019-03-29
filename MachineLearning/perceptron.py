# -*- coding: utf-8 -*-


import numpy as np

class Perceptron(object):
   
    def __init__(self, nb_features, epochs=100):
        self.weights = np.zeros(nb_features)
        self.bias    = np.zeros(1) 
        self.epochs = epochs
        
    # Bainary step fct
    @staticmethod
    def activation_fct(z):
        if z <= 0:
            return 0
        else:
            return 1
        
        
    def predict(self, X):
        return self.activation_fct(self.weights @ X + self.bias)
    
    def fit(self, X, y):
        for _ in range(self.epochs):
            for i in range(y.shape[0]):
                a = self.predict(X[i])
                error = y[i] - a
                self.weights = self.weights+error*X[i]
                self.bias = self.bias+error
            

        
        
# Train an & gate             
                
X = np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1]
])

y = np.array([0,0,0,1])


p = Perceptron(nb_features=2)
p.fit(X,y)
p.predict([1,0])
