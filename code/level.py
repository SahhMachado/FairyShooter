#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame.display
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.const import WIN_HEIGHT, COLOR_PURPLE
from code.entity import Entity
from code.entityFactory import EntityFactory

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] =[]
        self.entity_list.extend(EntityFactory.get_entity('level1BG'))
        self.timeout = 20000 # 20 seconds

    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_PURPLE, (10,5))
            self.level_text(14, f'FPS: {clock.get_fps(): .0f}s', COLOR_PURPLE, (10,WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_PURPLE, (10,WIN_HEIGHT - 20))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)