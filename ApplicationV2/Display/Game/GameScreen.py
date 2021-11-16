############################################################################################################
# Class: GameScreen
############################################################################################################

# Imports ==================================================================================================
import pygame
from Display.Game.Menu.OptionsMenu import OptionsMenu
from Settings.Default import Colors, ScreenSize
# ==========================================================================================================

# GameScreen ===============================================================================================
class GameScreen():
# Inititalize class ----------------------------------------------------------------------------------------
    def __init__(self):
        self.ScreenWidth = ScreenSize['width']
        self.ScreenHeight = ScreenSize['height']
        self.Screen = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeight), pygame.DOUBLEBUF|pygame.HWSURFACE, 32)
        self.Screen.fill((Colors["Background"]))
# Game OptionsMenu ---------------------------------------------------------------------------------------------
    def OptionsMenu(self):
        X = self.ScreenWidth - 165
        Y = self.ScreenHeight/2 - 150
        Width = 145
        Height = 300
        self.Options = OptionsMenu(self.Screen, X, Y, Width, Height, Colors["black"], Colors["Background"])
# GameBoard ------------------------------------------------------------------------------------------------

# ==========================================================================================================
