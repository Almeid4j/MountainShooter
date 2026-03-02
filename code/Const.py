# C
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)

import pygame

# E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player': 5,
    'Enemy1': 2,
}

ENTITY_SHOT_DELAY = {
    'Enemy1': 60,
    'Enemy2': 40
}

PLAYER_KEY_UP = pygame.K_w
PLAYER_KEY_DOWN = pygame.K_s
PLAYER_KEY_LEFT = pygame.K_a
PLAYER_KEY_RIGHT = pygame.K_d
PLAYER_KEY_SHOOT = pygame.K_SPACE

# M
MENU_OPTION = ('NEW GAME 1P' ,
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')


WIN_WIDTH = 576
WIN_HEIGHT = 324