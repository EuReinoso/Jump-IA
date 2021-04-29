import pygame
from network import Network
from random import choice

pygame.init()

COLORS = [
    (200,0,0),
    (0,200,0),
    (0,0,200),
    (200,200,0),
    (200,0,200),
    (0,200,200)
]

class Individual:
    def __init__(self, rect, network_sizes):
        self.rect = rect
        self.limit = rect.y
        self.network = Network(network_sizes)

        self.y_momentum = 0
        self.y_vel = 0.2

        self.color = choice(COLORS)
        self.jump_force = 7

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
    
    def gravity(self):
        self.rect.y += self.y_momentum
        self.y_momentum += self.y_vel

        if self.rect.y >= self.limit:
            self.y_momentum = 0
            self.rect.y = self.limit
    
    def jump(self):
        if self.y_momentum == 0:
            self.y_momentum -= self.jump_force
    
    def get_action(self, inputs):
        for i in inputs:
            if i == None:
                return

        output = self.network.feedforward(inputs)

        if output == 1:
            self.jump()
