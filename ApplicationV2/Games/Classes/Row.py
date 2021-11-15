############################################################################################################
# Class: Row
############################################################################################################

# Import Class-Modules =====================================================================================
from Games.Classes.Value import Value
# ==========================================================================================================

# Row ======================================================================================================
class Row():
    def __init__(self, pNumberOfColumns, pRowNr):
        self.NumberOfColumns = pNumberOfColumns
        self.Row = []
        for ColNr in range(self.NumberOfColumns):
            self.Row.append(Value((pRowNr, ColNr)))
# Return all Value-Class data for te row ------------------------------------------------------------------
    def GetRowData(self):
        return self.Row
# Return all Values from the Value-Class data in the Row --------------------------------------------------
    def GetRowValues(self):
        RowValues = []
        for ColNr in range(self.NumberOfColumns):
            RowValues.append(self.Row[ColNr].GetValue())                
        return RowValues
# Return all Possible Values from the Value-Class data in the Row -----------------------------------------
    def GetRowPossible(self):
        Possible = []
        for ColNr in range(self.NumberOfColumns):
            Possible.append(self.Row[ColNr].GetPossible())                
        return Possible