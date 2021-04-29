import pygame
from network import Network

pygame.init()

class Individual:
    def __init__(self, rect, network_sizes):
        self.rect = rect
        self.limit = rect.y
        self.network = Network(network_sizes)
        
        self.y_momentum = 0
        self.y_vel = 0.2

        self.jump_force = 7

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 200), self.rect)
    
    def gravity(self):
        self.rect.y += self.y_momentum
        self.y_momentum += self.y_vel

        if self.rect.y >= self.limit:
            self.y_momentum = 0
    
    def jump(self):
        if self.y_momentum == 0:
            self.y_momentum -= self.jump_force
    
    def get_action(self, inputs):
        for i in inputs:
            if i == None:
                return

        output = self.network.feedforward(inputs)

        if output >= 0.5:
            self.jump()
