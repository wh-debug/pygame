'''
Author: your name
Date: 2021-02-10 16:52:37
LastEditTime: 2021-02-10 16:58:43
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pygame\button.py
'''

import pygame.font

class Button:

    def __init__(self, ai_game, msg):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)