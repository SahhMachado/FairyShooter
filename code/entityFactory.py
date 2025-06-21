#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH

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

        return None
