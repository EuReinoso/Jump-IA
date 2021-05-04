import pygame
from network import Network
from random import choice, randint

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
        self.rect = pygame.Rect(self.rect.x + randint(-30, 50), self.rect.y,
                                 self.rect.width, self.rect.height)
        self.limit = rect.y
        self.network_sizes = network_sizes
        self.network = Network(network_sizes)

        self.y_momentum = 0
        self.y_vel = 0.2

        self.color = choice(COLORS)
        self.jump_force = 7

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect, border_radius= 15)
    
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
        if output[-1][-1] > 0:
            self.jump()
    
    def get_distance(self, obj_distance):
        if obj_distance != None:
            return obj_distance - self.rect.x
    
    def collide(self, rect):
        if self.rect.colliderect(rect):
            return True
