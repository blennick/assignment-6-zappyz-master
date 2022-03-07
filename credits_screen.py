"""
Displays game credits, and credits sources. Provides instructions for the game.
"""

import sound

from level_manager import *
from title_screen import *
from screen import *

class CreditsScreen(Screen):
    def __init__(self):
        super().__init__()
        
        font2 = pygame.font.SysFont('Calibri', 12, True, False)

        #brings in the music and sounds
        self.sound = sound.Sound(self)
        self.sound.play_repeat('credits')
        
        #The underscore character indicates that this is a private instance variable
        self._text = self._font.render("Dan Nygard: File Engineer",True,constants.YELLOW)
        self._text2 = self._font.render("Jack Olson: Game Engineer",True,constants.YELLOW)
        self._text3 = self._font.render("Bryant Lennick: Art Engineer",True,constants.YELLOW)
        self._text4 = self._font.render("In SPACE, move your ship with the arrow keys.",True, constants.YELLOW)
        self._text5 = self._font.render("Rescue aliens to score points, while avoiding asteroids.",True, constants.YELLOW)
        self._text5_1 = self._font.render("Blue aliens = 2 points. Green aliens = 1 point.",True, constants.YELLOW)
        self._text5_2 = self._font.render("Press ESC at any time to go back to Title Screen.", True, constants.YELLOW)
        self._text6 = font2.render("Game background music is \"Evolutius\" by VividReality at " +
                                   "https://opengameart.org/content/evolutius-music, used under CC BY 3.0.",True, constants.YELLOW)
        self._text7 = font2.render("All other background music and sound effects from Sci-Fi Sound Effects Library at " +
                                   "https://opengameart.org/content/sci-fi-sound-effects-library, used under CC BY 3.0.",True, constants.YELLOW)
        self._text8 = font2.render("All game art by Bryant Lennick using Piskel (https://www.piskelapp.com/).",True, constants.YELLOW)      

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.sound.play_once('title_bite')
                self.sound.stop_repeat('stopc')
                LevelManager().leave_level()    

    #No need to do anything here, unless we've got some animation
    def update(self):
        pass
        
    def draw(self, screen):
        # Display the background
        screen.blit(self.art.get_image('background'), [0,0])
        # Draw the credits text
        screen.blit(self._text, [340, constants.SCREEN_HEIGHT / 2])
        screen.blit(self._text2, [340, constants.SCREEN_HEIGHT / 2 + 25])
        screen.blit(self._text3, [340, constants.SCREEN_HEIGHT / 2 + 50])
        screen.blit(self._text4, [340, constants.SCREEN_HEIGHT / 2 - 150])
        screen.blit(self._text5, [340, constants.SCREEN_HEIGHT / 2 - 125])
        screen.blit(self._text5_1, [340, constants.SCREEN_HEIGHT / 2 - 100])
        screen.blit(self._text5_2, [340, constants.SCREEN_HEIGHT / 2 - 75])
        screen.blit(self._text6, [10, constants.SCREEN_HEIGHT -25])
        screen.blit(self._text7, [10, constants.SCREEN_HEIGHT -13])
        screen.blit(self._text8, [10, constants.SCREEN_HEIGHT -37])



        

