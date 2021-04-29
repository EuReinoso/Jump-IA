import pygame

pygame.init()

class Individual:
    def __init__(self, rect):
        self.rect = rect
        self.limit = rect.y
        
        self.y_momentum = 0
        self.y_vel = 0.2

        self.jump_force = 6

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 200), self.rect)
    
    def gravity(self):
        self.rect.y += self.y_momentum
        self.y_momentum += self.y_vel

        if self.rect.y >= self.limit:
            self.y_momentum = 0
    
    def jump(self):
        self.y_momentum -= self.jump_force