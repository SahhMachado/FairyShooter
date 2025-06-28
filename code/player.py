#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()

        # up
        if pressed_key[pygame.K_w] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        # down
        if pressed_key[pygame.K_s] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        # left
        if pressed_key[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        # right
        if pressed_key[pygame.K_d] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass
