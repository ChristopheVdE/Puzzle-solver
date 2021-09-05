# [PLAY] Pencil values for the selected cube (temp values)--------------------------------------------------
    def Pencil(self, key=None):
        # Pencil in values ---------------------------------------------------------------------------------
        if self.selected and self.selected[0] == "R" and key:
            if key != '0':
            # Create list of temp values -------------------------------------------------------------------
                if not isinstance(self.current[self.selected[1][0]][self.selected[1][1]], list):
                    tempValues = []
                else:
                    tempValues = self.current[self.selected[1][0]][self.selected[1][1]]
            # Add temp values to list ----------------------------------------------------------------------
                if not key in tempValues:
                    tempValues.append(str(key))
                else:
                    tempValues.remove(str(key))
                tempValues.sort()
            # Remove all temp values if delete is pressed --------------------------------------------------
            else:
                tempValues = '0'
            # Update board ---------------------------------------------------------------------------------
            self.current[self.selected[1][0]][self.selected[1][1]] = tempValues