def CenterRectangle(self, ScreenWidth, ScreenHeight, Unoccupy_X, Unoccupy_Y):
    # Calcualte centered X
    self.X = self.X / 2 - self.BoardSize / 2
    while self.X + self.BoardSize > ScreenWidth - Unoccupy_X:
        self.X = self.X - (self.CubeSize + 1)
    # Calcualte centered Y
    self.Y = self.Y / 2 - self.BoardSize / 2
    while self.Y + self.BoardSize > ScreenHeight - Unoccupy_Y:
        self.Y = self.Y - (self.CubeSize + 1)