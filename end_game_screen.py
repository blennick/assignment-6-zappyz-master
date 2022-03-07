"""
End game screen. Gives final score and allows to play again.
"""

import game_screen
from level_manager import *
from screen import *

class EndGameScreen(Screen):
    def __init__(self, num):
        super().__init__()

        self._text = self._font.render("Game Over. Final Score: " + str(num),True,constants.YELLOW)
        self._text2 = self._font.render("Press SPACE to play again. Press Esc to return to Title Screen",True,constants.YELLOW)

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
            if event.key == pygame.K_SPACE:
                LevelManager().leave_level()
                LevelManager().load_level(game_screen.GameScreen())
                

    #No need to do anything here, unless we've got some animation
    def update(self):
        pass
        
    def draw(self, screen):  
        # Draw background and text
        screen.blit(self.art.get_image('background'), [0,0])
        screen.blit(self._text, [400, constants.SCREEN_HEIGHT / 2 - 35])
        screen.blit(self._text2, [250, constants.SCREEN_HEIGHT / 2])
