import pygame
from random import randrange

pygame.init()

class Block:
    def __init__ (self, size, position):
        self.rect_types = [
            pygame.Rect(position[0], position[1], size[0], size[1]),
            pygame.Rect(position[0], position[1], size[0] * 2, size[1]),
            pygame.Rect(position[0], position[1], size[0], size[1] * 2),
            pygame.Rect(position[0], position[1], size[0] * 2, size[1] * 2)]
        
        self.count_types = len(self.rect_types)

        self.type = randrange(0, self.count_types)
        self.rect = self.rect_types[self.type]

    def draw(self, window):
        pygame.draw.rect(window, (100, 100, 100), self.rect)
    
    def  move(vel):
        self.rect.x -= vel
