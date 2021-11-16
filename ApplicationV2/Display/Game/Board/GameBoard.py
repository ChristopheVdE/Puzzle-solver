############################################################################################################
# Class: GameBoard
############################################################################################################

# Imports ==================================================================================================
import pygame
from Games.Classes.Board import Board
from Settings.Default import Colors, ScreenSize
# ==========================================================================================================

# [CLASS] SUBMENU ==========================================================================================
class GameBoard():
# Initialisation -------------------------------------------------------------------------------------------
    def __init__(self, Screen, X, Y, MaxWidth, MaxHeight, NrRows, NrColumns, CubeSize = 40, SpaceBetweenCubes = 1):
        self.Screen = Screen
        self.CubeSize = CubeSize
        self.SpaceBetweenCubes = SpaceBetweenCubes
        self.Width = int(NrRows *  (self.CubeSize + self.SpaceBetweenCubes))
        self.MaxWidth = MaxWidth
        self.Height = int(NrColumns *  (self.CubeSize + self.SpaceBetweenCubes))
        self.MaxHeight = MaxHeight
        self.X = int(X)
        self.Y = int(Y)
        self.Selected = None
# Calc Board Center ----------------------------------------------------------------------------------------
    def CalcBoardCenter(self):
        self.CenterX = (self.X + self.MaxWidth)/2
        self.CenterY = (self.Y + self.MaxHeight)/2
        self.X = self.CenterX - (self.Width/2)
        self.Y = self.CenterY - (self.Height/2)
# Create board surface and fill it (background) ------------------------------------------------------------
    def BoardBackground(self):
        # Create surface 
        self.BoardSurface = pygame.Surface((self.Width, self.Height), pygame.DOUBLEBUF|pygame.HWSURFACE, 32)
        self.BoardSurface.fill(Colors['black'])
        # Render surface
        self.Screen.blit(self.BoardSurface, (self.X, self.Y))
# ==========================================================================================================
