import pygame

pygame.init()

class Individual:
    def __init__(self, rect):
        self.rect = rect
        
        self.y_momentum = 10
        self.y_vel = 0

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 200), self.rect)
    
    def gravity(ground_y):
        self.rect.y += self.y_vel
        self.y_vel += self.y_momentum

        if self.rect.y >= ground_y:
            self.y_vel = 0
    
    def jump():
        self.y_vel -= self.y_momentum