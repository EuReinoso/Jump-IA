import numpy as np
from random import random, seed
from datetime import datetime

def sigmoid(z):
    z = np.array(z, dtype= np.float128)
    return 1.0/(1.0 + np.exp(-z))

def threshold(z):
    if z >= 0:
        return 1
    return 0

def relu(z):
    return np.maximum(z, 0)

class Network:
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            #a = sigmoid(np.dot(w, a) + b)
            #a = threshold(np.dot(w, a) + b)
            a = relu(np.dot(w,a) + b)
        return a

    def mutation(self):
        for i in range(len(self.biases)):
            for j in range(len(self.biases[i])):
                for k in range(len(self.biases[i][j])):
                    seed(datetime.now())
                    if random() <= 0.05:
                        self.biases[0][0] = np.random.randn()
        
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    seed(datetime.now())
                    if  random() <= 0.05:
                        self.weights[i][j][k] = np.random.randn()

    