"""
Implements all art objects.
"""

import pygame
import title_screen
import game_screen
import bad_block
import constants

from level_manager import *
from file_manager import *

class Art():

    #creates the art object
    def __init__(self, level):
        self._space_background = pygame.image.load(FileManager().get_path('background'))
        self._destroyed_planet = pygame.image.load(FileManager().get_path('planet'))
        self._alien_ship = pygame.image.load(FileManager().get_path('alien_ship'))
        
        if isinstance(level, title_screen.TitleScreen):
            self._space_background_text = pygame.image.load(FileManager().get_path('title_text'))

        else:
            self._asteroid = pygame.image.load(FileManager().get_path('asteroid')).convert()
            self._asteroid.set_colorkey(constants.BLACK)
            
            self._player = pygame.image.load(FileManager().get_path('player')).convert()
            self._player.set_colorkey(constants.BLACK)

            self._alien1 = pygame.image.load(FileManager().get_path('alien')).convert()
            self._alien1.set_colorkey(constants.BLACK)

            self._alien2 = pygame.image.load(FileManager().get_path('alien2')).convert()
            self._alien2.set_colorkey(constants.BLACK)


    def get_image(self, id):
        # retrieve an image referenced by id
        if id == 'background':
            return self._space_background
        elif id == 'title_text':
            return self._space_background_text
        elif id == 'asteroid':
            return self._asteroid
        elif id == 'player':
            return self._player
        elif id == 'alien':
            return self._alien1
        elif id == 'planet':
            return self._destroyed_planet
        elif id == 'alien_ship':
            return self._alien_ship
        elif id == 'alien2':
            return self._alien2
        
