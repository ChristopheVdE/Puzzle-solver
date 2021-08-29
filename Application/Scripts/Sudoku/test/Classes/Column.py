############################################################################################################
# Class: Column
############################################################################################################

# Column ===================================================================================================
class Column():
    def __init__(self, pboard, pColumnNumber):
        self.NumberOfRows = pboard.NumberOfRows
        self.Column = []
        for RowNr in range(pboard.NumberOfRows):
            self.Column.append(pboard.GetRow(RowNr)[pColumnNumber])
# Return all Value-Class data for te Column ---------------------------------------------------------------
    def GetColumn(self):
        return self.Column
# Return all Values from the Value-Class data in the Column -----------------------------------------------
    def GetColumnValues(self):
        ColumnValues = []
        for RowNr in range(self.NumberOfRows):
            ColumnValues.append(self.Column[RowNr].GetValue())                
        return ColumnValues
# Return all Possible Values from the Value-Class data in the Column --------------------------------------
    def GetColumnPossible(self):
        Possible = []
        for RowNr in range(self.NumberOfRows):
            Possible.append(self.Column[RowNr].GetPossible())                
        return Possible
