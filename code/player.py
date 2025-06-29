#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.entity import Entity
from code.playerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY

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

    def shot(self):
        self.shot_delay -= 1
        if self.shot_delay  == 0:
            self.shot_delay = ENTITY_SHOT_DELAY
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_SPACE]:
                return PlayerShot(f'{self.name}Shot', (self.rect.centerx, self.rect.centery))
        return None