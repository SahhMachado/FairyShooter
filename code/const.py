# C
import pygame.constants

C_PURPLE = 106, 101, 205
C_CREAM = 255, 255, 255
C_PINK = 229, 82, 242

# E
ENTITY_DAMAGE = {
    'level1BG0': 0,
    'level1BG1': 0,
    'level1BG2': 0,
    'level2BG0': 0,
    'level2BG1': 0,
    'level2BG2': 0,
    'player': 1,
    'playerShot': 25,
    'enemy1': 1,
    'enemy2': 1
}

EVENT_ENEMY = pygame.constants.USEREVENT + 1

ENTITY_HEALTH = {
    'level1BG0': 999,
    'level1BG1': 999,
    'level1BG2': 999,
    'level2BG0': 999,
    'level2BG1': 999,
    'level2BG2': 999,
    'player': 300,
    'playerShot': 1,
    'enemy1': 50,
    'enemy2': 60
}

ENTITY_SCORE = {
    'level1BG0': 0,
    'level1BG1': 0,
    'level1BG2': 0,
    'level2BG0': 0,
    'level2BG1': 0,
    'level2BG2': 0,
    'player': 0,
    'playerShot': 0,
    'enemy1': 50,
    'enemy2': 100
}

ENTITY_SPEED = {
    'level1BG0': 0,
    'level1BG1': 1,
    'level1BG2': 3,
    'level2BG0': 0,
    'level2BG1': 1,
    'level2BG2': 2,
    'player': 3,
    'playerShot': 3,
    'enemy1': 2,
    'enemy2': 2
}

ENTITY_SHOT_DELAY = 10

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')
# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 600
WIN_HEIGHT = 480
