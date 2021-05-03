import pygame, sys
from individual import Individual
from block import Block
from population import Population
import numpy as np

pygame.init()
pygame.font.init()

font = pygame.font.get_default_font()
font_info = pygame.font.SysFont(font, 30)

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

def show_info():
    txt_generation      = 'Generation: '    + str(population.count_generations)
    txt_best_score      = 'Best Score: '    + str(int(population.best_score))
    txt_score           = 'Score: '         + str(int(population.score))

    render_generation   = font_info.render(txt_generation,  1, (200, 200, 200))
    render_best_score   = font_info.render(txt_best_score,  1, (200, 200, 200))
    render_score        = font_info.render(txt_score,       1, (200, 200, 200))

    window.blit(render_generation,  (10, 10))
    window.blit(render_best_score,  (10, 40))
    window.blit(render_score,       (10, 70))

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

def turn_fps():
    global fps
    if fps == fps_normal:
        fps = fps_fast
    else:
        fps = fps_normal


time = pygame.time.Clock()
fps_fast = 1000
fps_normal = 60
fps = fps_normal
while True:

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                turn_fps()


    gen_blocks()
    acelerate()
    population.get_actions([get_block_distance(), get_block_type(), vel])
    population.gravity()
    population.score_increment(vel)

    if len(population.individuals) < 1:
        restart()

    if len(blocks) > 0:
        population.collide(blocks[0].rect)

    draw()
    show_info()
    pygame.display.update()
    time.tick(fps)