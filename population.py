from individual import Individual
from random import random

class Population:
    def __init__(self, population_size):
        self.population_size = population_size
        self.individuals = []

    def init(self,rect, network_sizes):
        for i in range(self.population_size):
            self.individuals.append(Individual(rect, network_sizes))

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
            if idv.collide(rect):
                self.individuals.remove(idv)
    
    def crossover(self, rect, network_sizes):
        idv1 = self.individuals[0]
        idv2 = self.individuals[1]

        while len(self.individuals) < self.population_size:
            cut = round(random() * len(idv1.network.weights))

            weights1 = idv1.network.weights[0:cut] + idv2.network.weights[cut::]
            weights2 = idv2.network.weights[0:cut] + idv1.network.weights[cut::]

            son1 = Individual(rect, network_sizes)
            son1.network.weights = weights1

            son2 = Individual(rect, network_sizes)
            son2.network.weights = weights2

            self.individuals.append(son1)
            self.individuals.append(son2)

