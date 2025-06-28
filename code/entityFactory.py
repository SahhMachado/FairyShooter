#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1BG':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'level1BG{i}',(0,0)))
                    list_bg.append(Background(f'level1BG{i}',(WIN_WIDTH, 0)))
                return list_bg
            case 'player':
                return Player('player', (10, 100))
            case 'enemy1':
                return Enemy('enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'enemy2':
                return Enemy('enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

        return None
