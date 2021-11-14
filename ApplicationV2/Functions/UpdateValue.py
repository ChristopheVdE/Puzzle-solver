# Update value of the selected cube (certain values) -------------------------------------------------------
    def Updatecube(self, key=None):
        # Update value of selected cube if key is pressed
        if self.selected and self.selected[0] == "L" and key:
            self.current[self.selected[1][0]][self.selected[1][1]] = str(key)