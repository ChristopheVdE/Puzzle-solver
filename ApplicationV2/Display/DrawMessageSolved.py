# Check board ----------------------------------------------------------------------------------------------
    def CheckBoard(self, Screen, TitleFont, TitleColor):
        if self.current == self.solution and len(find_empty(self.current)) == 0:
            Message = CenteredText("Solved", TitleFont, TitleColor, self.X + self.BoardSize/ 2, self.Y + self.BoardSize / 2)
            Message.render(Screen)
        elif self.current == self.solution and len(find_empty(self.current)) != 0:
            Message = CenteredText("Impossible", TitleFont, TitleColor, self.X + self.BoardSize/ 2, self.Y + self.BoardSize / 2)
            Message.render(Screen)