import pygame, sys

pygame.init()

WINDOW_SIZE = (640, 480)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Jump IA')

while True:

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()

    pygame.display.update()