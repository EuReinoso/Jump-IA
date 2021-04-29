import pygame, sys
from individual import Individual
from block import Block

pygame.init()

WINDOW_SIZE = (640, 480)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Jump IA')

ground_size = (WINDOW_SIZE[0], 100)
ground = pygame.Rect(0, WINDOW_SIZE[1] - ground_size[1], ground_size[0], ground_size[1])

individual_size = (50, 50)
individual_rect = pygame.Rect(150, ground.y - individual_size[1], individual_size[0], individual_size[1])
individual = Individual(individual_rect)

block_size = (50, 50)
block_position = (WINDOW_SIZE[0], ground.y - block_size[1])
blocks = []
block_ticks = 0

vel = 10

def gen_blocks():
    global block_ticks
    block_ticks += 1

    if block_ticks >= 160:
        block_ticks = 0
        blocks.append(Block(block_size, block_position))

def update_blocks():
    if len(blocks) > 0:
        for blk in blocks:
            blk.draw(window)
            blk.move(10)

def draw():
    pygame.draw.rect(window, (200, 200, 200), ground)
    update_blocks()
    individual.draw(window)



time = pygame.time.Clock()
fps = 60

while True:

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                individual.jump()

    draw()
    gen_blocks()
    individual.gravity()
    pygame.display.update()
    time.tick(fps)