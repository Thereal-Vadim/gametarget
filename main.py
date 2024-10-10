import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Game Target')
icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(icon)

target_img = pygame.image.load('target_images.png')
target_width = 50
target_height = 50

target_x = random.randint (0, SCREEN_WIDTH - target_width)
target_y = random.randint (0, SCREEN_HEIGHT - target_height)

color = (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))


running = True

while running:
    pass

pygame.quit()