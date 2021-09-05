# Draw the empty cubes -------------------------------------------------------------------------------------
    def DrawCubes(self, CubeColor, CorrectColor):
        # Parameters ---------------------------------------------------------------------------------------
        self.Rows = []      #contains start-coords and size of each row
        self.Cols = []      #contains start-coords and size of each column
        CubeX = 3  #border arround board = 2
        CubeY = 3  #border arround board = 2
        # Create cubes -------------------------------------------------------------------------------------
        for row in range(self.NumberOfCubes):
            if row in [3, 6]:                       # 3x3 grid separation lines: rows (Sudoku)
                CubeY += 1
            for col in range(self.NumberOfCubes):   # 3x3 grid separation lines: columns (Sudoku)
                if col in [3, 6]:
                    CubeX += 1
            # Draw cubes ------------------------------------------------------------------------------------
                if (row, col) in self.immutable:    # Value is correct --> dark background, light font
                    pygame.draw.rect(self.BoardSurface, CorrectColor, (CubeX, CubeY, self.CubeSize, self.CubeSize))
                else:                               # Value is wrong --> light background, dark font
                    pygame.draw.rect(self.BoardSurface, CubeColor, (CubeX, CubeY, self.CubeSize, self.CubeSize))
            # Save coords of colum --------------------------------------------------------------------------
                if len(self.Cols) < self.NumberOfCubes:
                    self.Cols.append((CubeX, 3))
                CubeX += self.CubeSize + self.spaceBetweenCubes
            # Save coords of Row ----------------------------------------------------------------------------
            self.Rows.append((3, CubeY))
            # Reset positions for new row -------------------------------------------------------------------
            CubeX = 3
            CubeY += self.CubeSize + self.spaceBetweenCubes