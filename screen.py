"""
Base class for all screens. Provides init method, ensures that all other
methods are implemented.
"""

import pygame
import constants
from art import *

class Screen():
    def __init__(self):
        self._font = pygame.font.SysFont('Calibri', 25, True, False)
        self.art = Art(self)
    
    def handle_keyboard_event(self, event):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError
        
    def draw(self, screen):
        raise NotImplementedError
