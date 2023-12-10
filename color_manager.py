# color_manager.py

import pygame
from random import randint

class ColorManager:
    @staticmethod
    def generate_random_color():
        return pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))

