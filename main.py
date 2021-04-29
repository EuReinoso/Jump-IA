import pygame, sys

pygame.init()

WINDOW_SIZE = (640, 480)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Jump IA')

ground_size = (WINDOW_SIZE[0], 100)
ground = pygame.Rect(0, WINDOW_SIZE[1] - ground_size[1], ground_size[0], ground_size[1])

def draw():
    pygame.draw.rect(window, (200, 200, 200), ground)

while True:

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw()
    pygame.display.update()