"""
Our good blocks. These will be aliens that must be rescued.
"""


import pygame, constants, random, game_screen

from block import *
from art import *
from file_manager import *

class GoodBlock(Block):
    """ This class represents the good blocks in the game """
    def __init__(self, img_type = 'alien'):
        """ Constructor """
        self.art = Art(game_screen.GameScreen)
        #Call the superclass constructor
        super().__init__(self.art.get_image(img_type), 20, 15)
        
        self.rect.x = random.randrange(constants.SCREEN_WIDTH)
        self.rect.y = random.randrange(constants.SCREEN_HEIGHT - 100)
        self.value = int(FileManager().get_value(img_type))

    #Move the block, resets to the right side after running off the edge
    #Good blocks move from right to left across the screen
    def move(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.rect.x = constants.SCREEN_WIDTH
