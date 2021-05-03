import pygame, sys
from individual import Individual
from block import Block
from population import Population
import numpy as np

pygame.init()

WINDOW_SIZE = (640, 480)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Jump IA')

ground_size = (WINDOW_SIZE[0], 100)
ground = pygame.Rect(0, WINDOW_SIZE[1] - ground_size[1], ground_size[0], ground_size[1])

network_sizes = [3, 1]

individual_size = (50, 50)
individual_rect = pygame.Rect(150, ground.y - individual_size[1], individual_size[0], individual_size[1])
individual = Individual(individual_rect, network_sizes)

block_size = (50, 50)
block_position = (WINDOW_SIZE[0], ground.y - block_size[1])
blocks = []
block_ticks = 0

vel_init = 5
vel = vel_init
acelerate_ticks = 0

population_size = 30
population = Population(population_size)
population.init(individual_rect, network_sizes)

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
            blk.move(vel)

            if blocks[0].rect.x <= - 100:
                blocks.pop(0)
def acelerate():
    global acelerate_ticks, vel
    acelerate_ticks += 1
    if acelerate_ticks >= 160:
        acelerate_ticks = 0
        vel += 0.5

def get_block_distance():
    if len(blocks) > 0:
        return blocks[0].rect.x

def get_block_type():
    if len(blocks) > 0:
        return blocks[0].type

def draw():
    pygame.draw.rect(window, (200, 200, 200), ground)
    update_blocks()
    population.draw(window)

def restart():
    global vel, blocks
    #population.crossover(individual_rect, network_sizes)
    population.replication(individual_rect, network_sizes)
    vel = vel_init
    blocks.clear()


time = pygame.time.Clock()
fps = 1000

while True:

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                individual.jump()

    gen_blocks()
    acelerate()
    population.get_actions([get_block_distance(), get_block_type(), vel])
    population.gravity()

    if len(population.individuals) == 1:
        restart()

    if len(blocks) > 0:
        population.collide(blocks[0].rect)

    draw()
    pygame.display.update()
    time.tick(fps)