# Return selected cube -------------------------------------------------------------------------------------
    def SelectCube(self, mouse, click):
        for row in range(len(self.Rows)):
            for col in range(len(self.Cols)):
                if not (row, col) in self.immutable:
                    if self.X + self.Cols[col][0] + self.CubeSize > mouse[0] > self.X + self.Cols[col][0] and self.Y + self.Rows[row][1] + self.CubeSize > mouse[1] > self.Y + self.Rows[row][1]:
                        # left mouse to wright a value
                        if click[0] == 1:
                            BoardPos = (row, col)
                            CubeCoords = (self.Cols[col][0], self.Rows[row][1])
                            self.selected = ("L", BoardPos, CubeCoords)
                        elif click[2] == 1:
                            BoardPos = (row, col)
                            CubeCoords = (self.Cols[col][0], self.Rows[row][1])
                            self.selected = ("R", BoardPos, CubeCoords)
        if self.selected:
            if not self.X + self.selected[2][0] + self.CubeSize > mouse[0] > self.X + self.selected[2][0] and not self.Y + self.selected[2][1] + self.CubeSize > mouse[0] > self.Y + self.selected[2][1]:
                self.selected = None