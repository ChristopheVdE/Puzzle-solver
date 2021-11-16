############################################################################################################
# Class: GameScreen
############################################################################################################

# Imports ==================================================================================================
import pygame
from Display.Game.Menu.OptionsMenu import OptionsMenu
from Display.Game.Board.GameBoard import GameBoard
from Settings.Default import Colors, ScreenSize
# ==========================================================================================================

# GameScreen ===============================================================================================
class GameScreen():
# Inititalize class ----------------------------------------------------------------------------------------
    def __init__(self):
        self.ScreenWidth = ScreenSize['width']
        self.ScreenHeight = ScreenSize['height']
        self.RightReservedSpace = 165
        self.ValueSummaryHeight = 0
        self.Screen = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeight), pygame.DOUBLEBUF|pygame.HWSURFACE, 32)
        self.Screen.fill((Colors["Background"]))
        self.Board = None
# Game OptionsMenu -----------------------------------------------------------------------------------------
    def RenderOptionsMenu(self):
        X = self.ScreenWidth - self.RightReservedSpace
        Y = self.ScreenHeight/2 - 150
        Height = 300
        self.Options = OptionsMenu(self.Screen, X, Y, 145, Height, Colors["black"], Colors["Background"])
# PossibleValues overview ----------------------------------------------------------------------------------
    def RenderPossibleValues(self):
        X = self.ScreenWidth - self.RightReservedSpace
        Y = self.ScreenHeight/2 - 150 + 350                 # --> display under uptions menu
# Summary Amount of Values per type ------------------------------------------------------------------------
    def RenderValueSummary(self):
        X = 0
        Y = 0
        self.ValueSummaryHeight = 50
        Width = self.ScreenWidth - self.RightReservedSpace    # --> display above board
# GameBoard ------------------------------------------------------------------------------------------------
    def RenderGameBoard(self, NrRows, NrColumns, CubeSize = 40, SpaceBetweenCubes = 1):
        X = 0
        Y = 0 + self.ValueSummaryHeight
        Width = self.ScreenWidth - self.RightReservedSpace
        Height = self.ScreenHeight - self.ValueSummaryHeight
        self.Board = GameBoard(self.Screen, X, Y, Width, Height, NrRows, NrColumns, CubeSize, SpaceBetweenCubes)
# ==========================================================================================================
