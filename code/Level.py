#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from typing import Any

import pygame
from code.EntityFactory import EntityFactory
from code.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.Enemy import Enemy




class Level:
    def __init__(self, window, name, menu_return, player_score):
        self.window = window
        self.name = name
        self.menu_return = menu_return
        self.player_score = player_score
        self.game_mode = menu_return
        self.entity_list = []
        self.timeout = 60000
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.extend(EntityFactory.get_entity('Player1'))
        if self.game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.extend(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.timeout -= clock.get_time()

            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RCTRL]:
                    print("CTRL detectado")

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, Player):
                    shoot = ent.shoot()
                    if shoot:
                        self.entity_list.append(shoot)

            if isinstance(ent, Enemy):
                shoot = ent.shoot()
                if shoot:
                    self.entity_list.append(shoot)

            # texto
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)