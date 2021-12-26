############################################################################################################
# Name: CalcPossible.py
# Function: Calculate all possible values for a value/box or for all related values/ boxes
############################################################################################################

# Import modules ===========================================================================================
from Games.Classes.Box import Box
from Games.Classes.Column import Column
# ==========================================================================================================

# Functions ================================================================================================
# Calcuate Possible Values to Remove -----------------------------------------------------------------------
def RemovePossible(pBoard, pPosition: tuple):     
    RowNr, ColNr = pPosition
    for Value in pBoard.GetRow(RowNr)[ColNr].GetPossible():           
        if (
            Value in pBoard.GetRowValues(RowNr)  # row
            or Value in Column(pBoard, pPosition[1]).GetColumnValues()  # column
            or Value in Box(pBoard, pPosition).GetBoxValues()  # box
        ):
            pBoard.GetRow(RowNr)[ColNr].RemovePossible(Value)
    return pBoard
# Calcuate Possible Values to Add --------------------------------------------------------------------------
def AddPossible(pBoard, pPosition):
    RowNr, ColNr = pPosition
    for Value in range(1,10):
        if (
            Value not in pBoard.GetRow(RowNr)[ColNr].GetPossible()
            and not Value in pBoard.GetRowValues(RowNr)  # row
            and not Value in Column(pBoard, ColNr).GetColumnValues()  # column
            and not Value in Box(pBoard, pPosition).GetBoxValues()  # box
        ):
            pBoard.GetRow(RowNr)[ColNr].AddPossible(Value)
    return pBoard
# Calcuate Possible Values ---------------------------------------------------------------------------------
def CalcPossible(pBoard, pPosition):
    RowNr, ColNr = pPosition
    if pBoard.GetRow(RowNr)[ColNr].GetValue() == 0:
        RemovePossible(pBoard, pPosition)
        AddPossible(pBoard, pPosition)
    return pBoard
# Calc All relevant Possible Values ------------------------------------------------------------------------
def CalcAllPossible(pBoard, pPosition):
    for Value in pBoard.GetRow(pPosition[0]):
        pBoard = CalcPossible(pBoard, Value.Position)
    for Value in Column(pBoard, pPosition[1]).GetColumn():
        pBoard = CalcPossible(pBoard, Value.Position)
    for Value in Box(pBoard, pPosition).GetBox():
        pBoard = CalcPossible(pBoard, Value.Position)
    return pBoard
# ==========================================================================================================