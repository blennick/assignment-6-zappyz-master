"""
Creates the object controlled by the player.
"""

import pygame, constants, random, game_screen

from block import *
from art import *


class Player(Block):
    def __init__(self):
        self.art = Art(game_screen.GameScreen)
        
        #Call the superclass constructor
        super().__init__(self.art.get_image('player'), 20, 15)

        self.rect.x = constants.SCREEN_WIDTH/2
        self.rect.y = constants.SCREEN_HEIGHT - 30
        self.x_speed = 0
        self.y_speed = 0

    #these functions change the x and y speeds
    def move_left(self):
        self.x_speed = -5 
    def move_right(self):
        self.x_speed = 5      
    def move_up(self):
        self.y_speed = -5       
    def move_down(self):
        self.y_speed = 5
    def stop_x(self):
        self.x_speed = 0
    def stop_y(self):
        self.y_speed = 0

    #changes the x and y coordinates of the player
    def update_position(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        #wrap to the opposite side to avoid going off screen
        if self.rect.x < 0:
            self.rect.x = constants.SCREEN_WIDTH            
        if self.rect.x > constants.SCREEN_WIDTH:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = constants.SCREEN_HEIGHT
        if self.rect.y > constants.SCREEN_HEIGHT:
            self.rect.y = 0
        
