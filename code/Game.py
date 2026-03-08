#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from .Menu import Menu
from code.Score import Score

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in ('NEW GAME 1P',
                               'NEW GAME 2P - COOPERATIVE',
                               'NEW GAME 2P - COMPETITIVE'):

                player_score = [0, 0]

                level = Level(self.window, 'Level1', menu_return, player_score)

                level_return = level.run(player_score)
            elif menu_return == MENU_OPTION[4]:
                pygame.quit() # Close Window
                quit() # end pygame
            else:
                pass