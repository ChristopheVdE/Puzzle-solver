# Highlight row & col of the location of the mouse ---------------------------------------------------------
    def HiglightLines(self, HighlightColor, mouse):
        # Create new surfaces for the higlights
        RowSurface = pygame.Surface((self.BoardSize -6, self.CubeSize))
        ColSurface = pygame.Surface((self.CubeSize, self.BoardSize -6))
        # Set color of highlights
        RowSurface.fill(HighlightColor)
        ColSurface.fill(HighlightColor)
        # Set alpha value of highlights (transparancy)
        RowSurface.set_alpha(50)
        ColSurface.set_alpha(50)
        # Check if mouse is in column-area & higlight column if true
        for col in self.Cols:
            if self.X + col[0] + self.CubeSize > mouse[0] > self.X + col[0] - 1 and self.Y + col[1] + self.BoardSize - 6 > mouse[1] > self.Y + col[1] - 1:
                self.BoardSurface.blit(ColSurface, (col[0], col[1]))
        # Check if mouse is in row-area & higlight row if true
        for row in self.Rows:
            if self.X + row[0] + self.BoardSize -6 > mouse[0] > self.X + row[0] -1 and self.Y + row[1] + self.CubeSize> mouse[1] > self.Y + row[1] -1:
                self.BoardSurface.blit(RowSurface, (row[0], row[1]))