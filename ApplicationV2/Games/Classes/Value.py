############################################################################################################
# Class: Value
############################################################################################################

# Import Class-Modules =====================================================================================
from Games.Classes.Column import Column
from Games.Classes.Box import Box
# ==========================================================================================================

# Values ===================================================================================================
class Value():
    def __init__(self, pPosition: tuple):
        self.Correct = False
        self.Value = 0
        self.PossibleValues = list(range(1,10))   
        self.UserPencil = []
        self.Position = pPosition
# Update Values --------------------------------------------------------------------------------------------
    def UpdateValue(self, pNewValue, pBoard, pPosition):
        if self.Correct == False: 
            self.Value = pNewValue
            self.PossibleValues = [pNewValue]
            self.CalcAllPossible(pBoard, pPosition)
# [GENERAL] Update User pencil -----------------------------------------------------------------------------
    def UpdatePencil(self, pNewValue: int):
        if self.Correct == False:
            if pNewValue in self.UserPencil:
                self.UserPencil.remove(pNewValue)
            else:
                self.UserPencil.append(pNewValue)
# [GENERAL] Set Value as Correct ---------------------------------------------------------------------------
    def SetValueAsCorrect(self):
        self.Correct = True
# [GENERAL] Return Value -----------------------------------------------------------------------------------
    def GetValue(self) -> int:
        return self.Value
# [GENERAL] Return Possible Values -------------------------------------------------------------------------
    def GetPossible(self) -> list:
        self.PossibleValues.sort()
        return self.PossibleValues
# [GENERAL] Return User Pencil Values ----------------------------------------------------------------------
    def GetUserPencils(self) -> list:
        self.UserPencil.sort()
        return self.UserPencil
# [GENERAL] Return if Value is correct ---------------------------------------------------------------------
    def GetCorrect(self) -> bool:
        return self.Correct
# Calcuate Possible Values ---------------------------------------------------------------------------------
    def CalcPossible(self, pBoard, pPosition):
        if self.Value == 0:
            self.RemovePossible(pBoard, pPosition)
            self.AddPossible(pBoard, pPosition)
        else:
            self.PossibleValues = [self.Value]
# Calcuate Possible Values to Remove -----------------------------------------------------------------------
    def RemovePossible(self, pBoard, pPosition):     
        for Value in self.PossibleValues:           
            if (
                Value in pBoard.board[pPosition[0]].GetRowValues()  # row
                or Value in Column(pBoard, pPosition[1]).GetColumnValues()  # column
                or Value in Box(pBoard, pPosition).GetBoxValues()  # box
            ):
                self.PossibleValues.remove(Value)
# Calcuate Possible Values to Add --------------------------------------------------------------------------
    def AddPossible(self, pBoard, pPosition):
        for Value in range(1,10):
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
# Calc All relevant Possible Values ------------------------------------------------------------------------
    def CalcAllPossible(self, pBoard, pPosition):
        for Value in pBoard.GetRow(pPosition[0]):
            Value.CalcPossible(pBoard, Value.Position)
        for Value in Column(pBoard, pPosition[1]).GetColumn():
            Value.CalcPossible(pBoard, Value.Position)
        for Value in Box(pBoard, pPosition).GetBox():
            Value.CalcPossible(pBoard, Value.Position)

