import pygame

pygame.init()

class Individual:
    def __init__(self, rect):
        self.rect = rect
        self.limit = rect.y
        
        self.y_momentum = 10
        self.y_vel = 0

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 200), self.rect)
    
    def gravity():
        self.rect.y += self.y_vel
        self.y_vel += self.y_momentum

        if self.rect.y >= self.limit:
            self.y_vel = 0
    
    def jump():
        self.y_vel -= self.y_momentum