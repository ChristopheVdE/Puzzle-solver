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
        self.MaxWidth = MaxWidth
        self.MaxHeight = MaxHeight
        self.X = int(X)
        self.Y = int(Y)
        self.NrRows = NrRows
        self.NrColumns = NrColumns
        self.Selected = None
# Calc Board Size: -----------------------------------------------------------------------------------------
    def CalcBoardSize(self, GameType):
        self.BoardBorder = 3
        BoxBorder = 1
        if GameType == 'Sudoku':
            self.Width = int(self.NrRows * (self.CubeSize + self.SpaceBetweenCubes) + (2*self.BoardBorder + BoxBorder))
            self.Height = int(self.NrColumns *  (self.CubeSize + self.SpaceBetweenCubes) + 2*self.BoardBorder + BoxBorder)
        else:
            self.Width = int(self.NrRows *  (self.CubeSize + self.SpaceBetweenCubes) + 2*self.BoardBorder)
            self.Height = int(self.NrColumns *  (self.CubeSize + self.SpaceBetweenCubes) + 2*self.BoardBorder)
# Calc Board Center ----------------------------------------------------------------------------------------
    def CalcBoardCenter(self):
        self.CenterX = (self.X + self.MaxWidth)/2
        self.CenterY = (self.Y + self.MaxHeight)/2
        self.X = self.CenterX - (self.Width/2)
        self.Y = self.CenterY - (self.Height/2)
# Create board surface and fill it (background) ------------------------------------------------------------
    def BoardBackground(self):
        self.BoardSurface = pygame.Surface((self.Width, self.Height), pygame.DOUBLEBUF|pygame.HWSURFACE, 32)
        self.BoardSurface.fill(Colors['black'])
# Draw the empty cubes -------------------------------------------------------------------------------------
    def DrawCubes(self, CubeColor, CorrectColor):
        # Parameters ---------------------------------------------------------------------------------------
        self.Rows = []      # contains start-coords and size of each row
        self.Cols = []      # contains start-coords and size of each column
        CubeX = self.BoardBorder          # border arround board = 2
        CubeY = self.BoardBorder          # border arround board = 2
        # Create cubes -------------------------------------------------------------------------------------
        for row in range(self.NrRows):
            if row in [3, 6]:                       # 3x3 grid separation lines: rows (Sudoku)
                CubeY += 1
            for col in range(self.NrColumns):       # 3x3 grid separation lines: columns (Sudoku)
                if col in [3, 6]:
                    CubeX += 1
            # Draw cubes ------------------------------------------------------------------------------------
                # if (row, col) in self.immutable:    # Value is correct  --> dark background, light font
                #     pygame.draw.rect(self.BoardSurface, CorrectColor, (CubeX, CubeY, self.CubeSize, self.CubeSize))
                # else:                               # Value is wrong    --> light background, dark font
                pygame.draw.rect(self.BoardSurface, CubeColor, (CubeX, CubeY, self.CubeSize, self.CubeSize))
            # Save coords of colum --------------------------------------------------------------------------
                if len(self.Cols) < self.NrColumns:
                    self.Cols.append((CubeX, 3))
                CubeX += self.CubeSize + self.SpaceBetweenCubes
            # Save coords of Row ----------------------------------------------------------------------------
            self.Rows.append((3, CubeY))
            # Reset positions for new row -------------------------------------------------------------------
            CubeX = 3
            CubeY += self.CubeSize + self.SpaceBetweenCubes
# Draw the values ------------------------------------------------------------------------------------------

# Highlight row & col of the location of the mouse ---------------------------------------------------------
    def HiglightLines(self, HighlightColor, mouse):
        # Create new surfaces for the higlights
        RowSurface = pygame.Surface((self.Width -6, self.CubeSize))
        ColSurface = pygame.Surface((self.CubeSize, self.Height -6))
        # Set color of highlights
        RowSurface.fill(HighlightColor)
        ColSurface.fill(HighlightColor)
        # Set alpha value of highlights (transparancy)
        RowSurface.set_alpha(50)
        ColSurface.set_alpha(50)
        # Check if mouse is in column-area & higlight column if true
        for col in self.Cols:
            if self.X + col[0] + self.CubeSize > mouse[0] > self.X + col[0] - 1 and self.Y + col[1] + self.Height - 6 > mouse[1] > self.Y + col[1] - 1:
                self.BoardSurface.blit(ColSurface, (col[0], col[1]))
        # Check if mouse is in row-area & higlight row if true
        for row in self.Rows:
            if self.X + row[0] + self.Width -6 > mouse[0] > self.X + row[0] -1 and self.Y + row[1] + self.CubeSize> mouse[1] > self.Y + row[1] -1:
                self.BoardSurface.blit(RowSurface, (row[0], row[1]))

# Render the playboard -------------------------------------------------------------------------------------
    def Rendersurface(self):
        self.Screen.blit(self.BoardSurface, (self.X, self.Y))
# ==========================================================================================================
