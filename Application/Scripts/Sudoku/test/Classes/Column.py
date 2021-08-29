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
    def GetColumnValues(self):
        ColumnValues = []
        for RowNr in range(self.NumberOfRows):
            ColumnValues.append(self.Column[RowNr].GetValue())                
        return ColumnValues
