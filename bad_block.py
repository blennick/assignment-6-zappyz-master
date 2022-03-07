"""
Creates a "bad" block object.
"""

import pygame, constants, random, art, game_screen

from block import *
from game_screen import *

class BadBlock(Block):
    """ This class represents the bad blocks in the game """
    def __init__(self):

        self.art = art.Art(game_screen.GameScreen)
        """ Constructor """
        #Call the superclass constructor
        super().__init__(self.art.get_image('asteroid'), 20, 15)

        #bad blocks are created at a random location
        self.rect.x = random.randrange(constants.SCREEN_WIDTH)
        self.rect.y = random.randrange(constants.SCREEN_HEIGHT - 150)

    #move the block, resets to a new location after falling off
    #bad blocks move from the top of the screen to the bottom
    def move(self, level):
        self.rect.y += (3 + level)
        if self.rect.y > constants.SCREEN_HEIGHT:
            self.rect.y = random.randrange(-100, -10)
            self.rect.x = random.randrange(0, constants.SCREEN_WIDTH)
