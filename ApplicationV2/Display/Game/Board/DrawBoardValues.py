# Print Board ----------------------------------------------------------------------------------------------
    def PrintBoard(self, Screen):
    # Print values -----------------------------------------------------------------------------------------
        for row in range(len(self.Rows)):
            for col in range(len(self.Cols)):
                CubeCoords = (self.Cols[col][0], self.Rows[row][1])
            # Immutabe values ------------------------------------------------------------------------------
                if self.current[row][col] != "0" and (row, col) in self.immutable:
                    value = CenteredText(self.current[row][col], Fonts["Immutable"], Colors["Immutable"], (CubeCoords[0] + self.CubeSize / 2), (CubeCoords[1] + self.CubeSize / 2))
                    value.render(self.BoardSurface)
            # New values -----------------------------------------------------------------------------------
                elif self.current[row][col] != "0" and not isinstance(self.current[row][col], list) and not (row, col) in self.immutable:
                    value = CenteredText(self.current[row][col], Fonts["Certain"], Colors["Certain"], (CubeCoords[0] + self.CubeSize / 2), (CubeCoords[1] + self.CubeSize / 2))
                    value.render(self.BoardSurface)
            # Pencil ---------------------------------------------------------------------------------------
                elif isinstance(self.current[row][col], list) and not (row, col) in self.immutable:
                    # Coordinates for each value in pencil list
                    Coords = [
                        (int(CubeCoords[0] + self.CubeSize * 5/6), int(CubeCoords[1] + self.CubeSize * 1/6)),
                        (int(CubeCoords[0] + self.CubeSize * 5/6), int(CubeCoords[1] + self.CubeSize * 3/6)),
                        (int(CubeCoords[0] + self.CubeSize * 5/6), int(CubeCoords[1] + self.CubeSize * 5/6)),
                        (int(CubeCoords[0] + self.CubeSize * 3/6), int(CubeCoords[1] + self.CubeSize * 1/6)),
                        (int(CubeCoords[0] + self.CubeSize * 3/6), int(CubeCoords[1] + self.CubeSize * 3/6)),
                        (int(CubeCoords[0] + self.CubeSize * 3/6), int(CubeCoords[1] + self.CubeSize * 5/6)),
                        (int(CubeCoords[0] + self.CubeSize * 1/6), int(CubeCoords[1] + self.CubeSize * 1/6)),
                        (int(CubeCoords[0] + self.CubeSize * 1/6), int(CubeCoords[1] + self.CubeSize * 3/6)),
                        (int(CubeCoords[0] + self.CubeSize * 1/6), int(CubeCoords[1] + self.CubeSize * 5/6))
                    ]
                    # Render
                    for i in range(len(self.current[row][col])):
                        value = CenteredText(self.current[row][col][i], Fonts["Pencil"], Colors["Pencil"], Coords[i][0], Coords[i][1])
                        value.render(self.BoardSurface)
    # Render BoardSurface on Main-Screen -------------------------------------------------------------------
        Screen.blit(self.BoardSurface, (self.X, self.Y))