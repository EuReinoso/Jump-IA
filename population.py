from individual import Individual
from random import random

class Population:
    def __init__(self, population_size):
        self.population_size = population_size
        self.individuals = []
        self.score = 0
        self.best_score = 0

        self.count_generations = 0
        self.last_individual = None

    def init(self,rect, network_sizes):
        for i in range(self.population_size):
            self.individuals.append(Individual(rect, network_sizes))
        self.best_individual = self.individuals[0] #temp

    def draw(self, window):
        for idv in self.individuals:
            idv.draw(window)
    
    def get_actions(self, inputs):
        for idv in self.individuals:
            temp = idv.get_distance(inputs[0])
            inputs[0] = temp
            idv.get_action(inputs)
    
    def gravity(self):
        for idv in self.individuals:
            idv.gravity()

    def collide(self, rect):
        for idv in self.individuals:
            if idv.collide(rect) and len(self.individuals) > 0:
                if len(self.individuals) == 1:
                    self.last_individual = idv

                self.individuals.remove(idv)

    
    def score_increment(self, vel):
        self.score += vel

    def replication(self, rect, network_sizes):    
        if self.score > self.best_score:  
            self.best_score = self.score
        
        idv = self.last_individual
        self.count_generations += 1
        self.score = 0
        self.individuals.clear()

        while len(self.individuals) < self.population_size:
            son = Individual(rect, network_sizes)
            son.network.weights = idv.network.weights
            son.network.biases = idv.network.biases
            son.network.mutation()
            self.individuals.append(son)

