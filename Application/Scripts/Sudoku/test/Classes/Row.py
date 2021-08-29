############################################################################################################
# Class: Row
############################################################################################################

# Import Class-Modules =====================================================================================
from Classes.Value import Value
# ==========================================================================================================

# Row ======================================================================================================
class Row():
    def __init__(self, pNumberOfColumns):
        self.NumberOfColumns = pNumberOfColumns
        self.Row = []
        for value in range(self.NumberOfColumns):
            self.Row.append(Value())
    def GetRowValues(self):
        RowValues = []
        for ColNr in range(self.NumberOfColumns):
            RowValues.append(self.Row[ColNr].GetValue())                
        return RowValues
    def GetRowData(self):
        return self.Row