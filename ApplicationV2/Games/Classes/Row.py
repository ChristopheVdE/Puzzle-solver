############################################################################################################
# Class: Row
############################################################################################################

# Import Class-Modules =====================================================================================
from Games.Classes.Value import Value
# ==========================================================================================================

# Row ======================================================================================================
class Row():
    def __init__(self, pNumberOfColumns: int, pRowNr: int):
        self.NumberOfColumns = pNumberOfColumns
        self.Row = []
        for ColNr in range(self.NumberOfColumns):
            self.Row.append(Value((pRowNr, ColNr)))
# [GENERAL] Return all Value-Class data for te row ---------------------------------------------------------
    def GetRowData(self) -> list:
        return self.Row
# [GENERAL] Return all Values from the Value-Class data in the Row -----------------------------------------
    def GetRowValues(self) -> list:
        RowValues = []
        for ColNr in range(self.NumberOfColumns):
            RowValues.append(self.Row[ColNr].GetValue())                
        return RowValues
# [GENERAL] Return all Possible Values from the Value-Class data in the Row --------------------------------
    def GetRowPossible(self) -> list:
        Possible = []
        for ColNr in range(self.NumberOfColumns):
            Possible.append(self.Row[ColNr].GetPossible())                
        return Possible