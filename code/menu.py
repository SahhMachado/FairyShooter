#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.const import WIN_WIDTH, COLOR_PURPLE, MENU_OPTION, COLOR_PINK, COLOR_CREAM


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assets/menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(52, 'Fairy', COLOR_CREAM, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'Fairy', COLOR_PURPLE, ((WIN_WIDTH / 2), 70))
            self.menu_text(52, 'Shooter', COLOR_CREAM, ((WIN_WIDTH / 2), 120))
            self.menu_text(50, 'Shooter', COLOR_PURPLE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(26, MENU_OPTION[i], COLOR_CREAM, ((WIN_WIDTH / 2), 250 + 30 * i))
                self.menu_text(25, MENU_OPTION[i], COLOR_PINK, ((WIN_WIDTH / 2), 250 + 30 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit() # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)