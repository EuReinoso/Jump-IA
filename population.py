from individual import Individual

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
            idv.get_action(inputs)
    
    def gravity(self):
        for idv in self.individuals:
            idv.gravity()

