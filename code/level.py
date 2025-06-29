#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
from random import choice

import pygame.display
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.const import WIN_HEIGHT, C_PURPLE, EVENT_ENEMY, SPAWN_TIME, C_PINK
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.timeout = 20000 # 20 seconds
        self.entity_list: list[Entity] =[]
        self.entity_list.extend(EntityFactory.get_entity('level1BG'))
        self.entity_list.append(EntityFactory.get_entity('player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, Player):
                    shot = ent.shot()
                    if shot is not None:
                        self.entity_list.append(shot)
                if ent.name == 'player':
                    self.level_text(14, f'Player - Health: {ent.health} | Score: {ent.score}', C_PINK, (10, 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    spawn = random.choice(('enemy1', 'enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(spawn))

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_PURPLE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps(): .0f}', C_PURPLE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', C_PURPLE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

           # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)