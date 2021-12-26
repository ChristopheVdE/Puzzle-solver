############################################################################################################
# Name: SetPossible.py
# Function: Set the initial possible values for the entire board
############################################################################################################

from copy import copy

# Function =================================================================================================
def SetAllPossible(pBoard, pPossible: list):
    Rows, Cols = pBoard.GetBoardDimensions()
    for RowNr in range(Rows):
        for ColNr in range(Cols):
            pBoard.GetRow(RowNr)[ColNr].SetPossible(copy(pPossible))
    return pBoard
# ==========================================================================================================