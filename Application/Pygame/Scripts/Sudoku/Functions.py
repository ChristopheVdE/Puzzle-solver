############################################################################################################
# NAME: Sudoku
# AUTHOR: Christophe Van den Eynde
# FUNCTION: All scripts concerning Sudoku's for the pygame apllication
############################################################################################################

# IMPORT PACKAGES ==========================================================================================
import pygame
# ==========================================================================================================

# Board ====================================================================================================
class board():
    def __init__(self, Screen, NumberOfCubes, StartPos):
        self.Screen = Screen
        self.NumberOfCubes = int(NumberOfCubes)
        self.X = int(StartPos[0])
        self.Y = int(StartPos[1])
        self.CubeSize = 40

    def DarwBoardBackground(self, BackgroundColor):
        self.spaceBetweenCubes = 1
        self.BoardSize = int((self.NumberOfCubes * self.CubeSize) + (self.NumberOfCubes * self.spaceBetweenCubes) + 2 + 5)
        pygame.draw.rect(self.Screen, BackgroundColor, (self.X, self.Y, self.BoardSize, self.BoardSize))
    
    def DrawCubes(self, CubeColor):
        # Parameters ---------------------------------------------------------------------------------------
        self.Rows = []      #contains start-coords and size of each row
        self.Cols = []      #contains start-coords and size of each column
        CubeX = self.X + 3  #border arround board = 2
        CubeY = self.Y + 3  #border arround board = 2
        # Create cubes -------------------------------------------------------------------------------------
        for row in range(self.NumberOfCubes):
            # 3x3 grid separation lines: rows (Sudoku)
            if row in [3, 6]:
                CubeY += 1
            for col in range(self.NumberOfCubes):
                # 3x3 grid separation lines: columns (Sudoku)
                if col in [3, 6]:
                    CubeX += 1
                # Draw cube
                pygame.draw.rect(self.Screen, CubeColor, (CubeX, CubeY, self.CubeSize, self.CubeSize))
            # Save coords of colum --------------------------------------------------------------------------
                self.Cols.append((CubeX, self.Y +3))
                CubeX += self.CubeSize + self.spaceBetweenCubes
            # Save coords of Row ----------------------------------------------------------------------------
            self.Rows.append((self.X +3, CubeY))
            # Reset positions for new row -------------------------------------------------------------------
            CubeX = self.X + 3
            CubeY += self.CubeSize + self.spaceBetweenCubes

    def HiglightLines(self, HighlightColor, mouse):
        # Create new surfaces for the higlights
        RowSurface = pygame.Surface((self.BoardSize -6, self.CubeSize))
        ColSurface = pygame.Surface((self.CubeSize, self.BoardSize -6))
        # Set color of highlights
        RowSurface.fill(HighlightColor)
        ColSurface.fill(HighlightColor)
        # Set alpha value of highlights (transparancy)
        RowSurface.set_alpha(1)
        ColSurface.set_alpha(1)
        # Check if mouse position & higlight correct row/ column
        for row in self.Rows:
            for col in self.Cols:
                # Check if mouse is in column-area & higlight column if true
                if col[0] + self.CubeSize > mouse[0] > col[0] and col[1] + self.BoardSize - 2 > mouse[1] > col[1]:
                    self.Screen.blit(ColSurface, (col[0], col[1]))
                # Check if mouse is in row-area & higlight row if true
                if row[0] + self.BoardSize -5 > mouse[0] > row[0] and row[1] + self.CubeSize> mouse[1] > row[1]:
                    self.Screen.blit(RowSurface, (row[0], row[1]))
    
    """
    def UpdateCube(self):
        # print values on board
        # allow selecting of cube if it's not a permanent value
        # allow typing
        # allow pencil
    """

