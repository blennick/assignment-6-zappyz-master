"""
Runs the main game. Generates 25 bad guys to begin, then adds five bad guys
and increments their speed at each new level.
"""


import random

from level_manager import *
from screen import *
from block import *
from bad_block import *
from good_block import *
from player import *
from end_game_screen import *
from sound import *

class GameScreen(Screen):
    def __init__(self, score = 0, lives = 3, level = 1):

        super().__init__()
        # three sprite groups - blocks (asteroids), aliens (must rescue), and all.
        # all just holds everything - it helps update things in the while loop
        self.block_list = pygame.sprite.Group()
        self.alien_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()       


        #This creates a group of 25 bad blocks, +5 per level
        for i in range(20 + (5*level)):
            block = BadBlock()
            
            self.block_list.add(block)
            self.all_sprites_list.add(block)

        #This creates five good sprites of 1 value
        for i in range(5):
            block = GoodBlock()
            self.alien_list.add(block)
            self.all_sprites_list.add(block)

        #Now, five good sprites of 2 value
        for i in range (5):
            block = GoodBlock('alien2')
            self.alien_list.add(block)
            self.all_sprites_list.add(block)
            
        #This creates the player, and adds the player to all sprites.
        self.player = Player()       
        self.all_sprites_list.add(self.player)


        #Keeps track of score and lives
        self.score = score
        self.lives = lives
        self.level = level

        #brings in the music and sounds
        self.sound = Sound(self)
        self.sound.play_repeat('game')


    #Fairly standard keyboard input to control the ship
    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.sound.play_once('title_bite')
                self.sound.stop_repeat('stopg')
                LevelManager().leave_level()
            elif event.key == pygame.K_LEFT:
                self.player.move_left()
            elif event.key == pygame.K_RIGHT:
                self.player.move_right()
            elif event.key == pygame.K_UP:
                self.player.move_up()
            elif event.key == pygame.K_DOWN:
                self.player.move_down()

        #The below stops the ship when keys are lifted
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.player.stop_x()
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.player.stop_y()
                

    def update(self):

        #moves the player
        self.player.update_position()

        #moves the asteroids
        for block in self.block_list:
            block.move(self.level)
            if pygame.sprite.collide_rect(block, self.player):
                self.sound.play_once('crash')
                self.lives -= 1
                self.block_list.remove(block)
                self.all_sprites_list.remove(block)

        #moves the gold
        for block in self.alien_list:
            block.move()
            if pygame.sprite.collide_rect(block, self.player):
                self.sound.play_once('objective')
                self.score += block.value
                self.alien_list.remove(block)
                self.all_sprites_list.remove(block)

        #Moves to a new level when all gold is found, adds one life for completing the level
        if len(self.alien_list) == 0:
            self.sound.stop_repeat('stopg')
            self.lives += 1
            LevelManager().leave_level()
            LevelManager().load_level(GameScreen(self.score, self.lives, self.level+1))

        #Moves to title screen after dying
        if self.lives == 0:
            self.sound.stop_repeat('stopg')
            self.sound.play_once('finish')
            LevelManager().leave_level()
            LevelManager().load_level(EndGameScreen(self.score))

        #Triggers warp drive sound
        if self.player.rect.x == 0 or self.player.rect.y == constants.SCREEN_WIDTH:
            self.sound.play_once('warp')
        if self.player.rect.y == 0 or self.player.rect.y == constants.SCREEN_HEIGHT:
            self.sound.play_once('warp')
        
        
    def draw(self, screen):
        # Clear the screen and draw background
        screen.blit(self.art.get_image('background'), [0,0])
        screen.blit(self.art.get_image('planet'), [100, 200])
        screen.blit(self.art.get_image('alien_ship'), [500, 150])
        
        #Draw the score and lives counter
        score_text = self._font.render("Score: " + str(self.score) + " Lives: " +
                                 str(self.lives) + " Level: " + str(self.level), True, constants.BLUE)
        screen.blit(score_text, [0, 0])
     
        # Draw everything else
        self.all_sprites_list.draw(screen)
