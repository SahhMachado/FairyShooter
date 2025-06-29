#!/usr/bin/python
# -*- coding: utf-8 -*-
from json.encoder import py_encode_basestring_ascii

import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.const import WIN_WIDTH, C_PURPLE, MENU_OPTION, C_PINK, C_CREAM


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menuBG.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(52, 'Fairy', C_CREAM, ((WIN_WIDTH / 2), 110))
            self.menu_text(50, 'Fairy', C_PURPLE, ((WIN_WIDTH / 2), 110))
            self.menu_text(52, 'Shooter', C_CREAM, ((WIN_WIDTH / 2), 180))
            self.menu_text(50, 'Shooter', C_PURPLE, ((WIN_WIDTH / 2), 180))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(26, MENU_OPTION[i], C_CREAM, ((WIN_WIDTH / 2), 300 + 30 * i))
                    self.menu_text(25, MENU_OPTION[i], C_PURPLE, ((WIN_WIDTH / 2), 300 + 30 * i))
                else:
                    self.menu_text(26, MENU_OPTION[i], C_CREAM, ((WIN_WIDTH / 2), 300 + 30 * i))
                    self.menu_text(25, MENU_OPTION[i], C_PINK, ((WIN_WIDTH / 2), 300 + 30 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit() # End pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP: # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)