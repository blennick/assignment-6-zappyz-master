"""
Title Screen. Allows for beginning the game or viewing the Credits Screen.
"""

from level_manager import *
from game_screen import *
from credits_screen import *
from sound import *
from screen import *

class TitleScreen(Screen):
    def __init__(self):
        
        super().__init__()

        self._text = self._font.render("Press SPACE to play. Press C to see credits.",True,constants.YELLOW)
        self.sound = Sound(self)

        #plays background song
        self.sound.play_repeat('title')   

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
            elif event.key == pygame.K_SPACE:
                self.sound.play_once('title_bite')
                self.sound.stop_repeat('stopt')
                LevelManager().load_level(GameScreen())
            elif event.key == pygame.K_c:
                self.sound.play_once('title_bite')
                self.sound.stop_repeat('stopt')
                LevelManager().load_level(CreditsScreen())
                

    #No need to do anything here, unless we've got some animation
    def update(self):
        pass
        
    def draw(self, screen):
        # Draw the background and game title image
        screen.blit(self.art.get_image('background'), [0,0])
        screen.blit(self.art.get_image('title_text'), [450, 325])
     
        # Draw my title text!
        screen.blit(self._text, [350, 425])
