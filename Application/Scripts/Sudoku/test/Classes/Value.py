############################################################################################################
# Class: Value
############################################################################################################

# Import Class-Modules =====================================================================================
from Classes.Column import Column
from Classes.Box import Box
# ==========================================================================================================

# Values ===================================================================================================
class Value():
    def __init__(self):
        self.Correct = False
        self.Value = 0
        self.PossibleValues = list(range(1,10))   
        self.UserPencil = []
# Update Values --------------------------------------------------------------------------------------------
    def UpdateValue(self, pNewValue):
        if self.Correct == False: 
            self.Value = pNewValue
            self.PossibleValues = [pNewValue]
    def SetValueAsCorrect(self):
        self.Correct = True
    def GetValue(self):
        return self.Value
# Calcuate Possible Values ---------------------------------------------------------------------------------
    def GetPossible(self):
        return self.PossibleValues
    def CalcPossible(self, pBoard, pPosition):
        self.RemovePossible(pBoard, pPosition)
        self.AddPossible(pBoard, pPosition)

    def RemovePossible(self, pBoard, pPosition):     
        for Value in self.PossibleValues:           
            if (
                Value in pBoard.board[pPosition[0]].GetRowValues()  # row
                or Value in Column(pBoard, pPosition[1]).GetColumnValues()  # column
                or Value in Box(pBoard, pPosition).GetBoxValues()  # box
            ):
                self.PossibleValues.remove(Value)

    def AddPossible(self, pBoard, pPosition):
        for Value in range(1,10) :
            if (
                Value not in self.PossibleValues
                and not Value in pBoard.board[pPosition[0]].GetRowValues()  # row
                and not Value in Column(pBoard, pPosition[1]).GetColumnValues()  # column
                and not Value in Box(pBoard, pPosition).GetBoxValues()  # box
            ):
                self.PossibleValues.append(Value)
# Reset Possible Values ------------------------------------------------------------------------------------                
    def ResetPossible(self):
        self.PossibleValues = list(range(1,10))     