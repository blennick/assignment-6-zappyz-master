"""
Controls all of the sounds in the game.
"""

import pygame
import title_screen
import game_screen
import credits_screen

from level_manager import *
from file_manager import *

class Sound():
    
    def __init__(self, level):
        
        # Loads all sounds and music associated with level
        self._title_sound_bite = pygame.mixer.Sound(FileManager().get_sound_path('title_bite'))
        
        if isinstance(level, title_screen.TitleScreen):
            self._title_screen_song = pygame.mixer.Sound(FileManager().get_sound_path('title'))
            
        elif isinstance(level, game_screen.GameScreen):
            self._game_song = pygame.mixer.Sound(FileManager().get_sound_path('game'))
            self._objective_sound = pygame.mixer.Sound(FileManager().get_sound_path('objective'))
            self._game_finish_sound = pygame.mixer.Sound(FileManager().get_sound_path('finish'))
            self._crash = pygame.mixer.Sound(FileManager().get_sound_path('crash'))
            self._warp = pygame.mixer.Sound(FileManager().get_sound_path('warp'))
            
        elif isinstance(level, credits_screen.CreditsScreen):
            self._credits_song = pygame.mixer.Sound(FileManager().get_sound_path('credits'))
            

    def play_once(self, id):
        # play previously loaded song referenced by id
        if id == 'title_bite':
            self._title_sound_bite.play(0)
        elif id == 'objective':
            self._objective_sound.play(0)
        elif id == 'finish':
            self._game_finish_sound.play(0)
        elif id == 'crash':
            self._crash.play(0)
        elif id == 'warp':
            self._warp.play(0)

    def play_repeat(self, id):
        # play a previously loaded song referenced by id on repeat
        if id == 'title':
            self._title_screen_song.play(-1)
        elif id == 'game':
            self._game_song.play(-1)
        elif id == 'credits':
            self._credits_song.play(-1)
            
    def stop_repeat(self, id):
        # stop a previously playing song referenced by id
        if id == 'stopt':
            self._title_screen_song.stop()
        elif id == 'stopg':
            self._game_song.stop()
        elif id == 'stopc':
            self._credits_song.stop()


        
