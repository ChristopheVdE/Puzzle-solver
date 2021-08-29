############################################################################################################
# Class: Board
############################################################################################################

# Import Class-Modules =====================================================================================
from Classes.Row import Row
# ==========================================================================================================

# Board ====================================================================================================
class Board():
# Inititalize class ----------------------------------------------------------------------------------------
    def __init__(self, pStartPos, pNumberOfRows, pNumberOfColumns):
        self.NumberOfColumns = pNumberOfColumns
        self.NumberOfRows = pNumberOfRows
        self.X = int(pStartPos[0])
        self.Y = int(pStartPos[1])
        self.CubeSize = 40
        self.SpaceBetweenCubes = 1
        self.BoardSize = int((self.NumberOfRows * self.CubeSize) + (self.NumberOfRows * self.SpaceBetweenCubes) + 2 + 5)
        self.Selected = None
# Create empty board ---------------------------------------------------------------------------------------
    def CreateEmptyBoard(self):
        self.board = []
        for row in range(self.NumberOfRows):
            self.board.append(Row(self.NumberOfColumns))
# Console Print board --------------------------------------------------------------------------------------
    def PrintBoardValues(self):
        print()
        for RowNr in range(self.NumberOfRows):
            print(self.board[RowNr].GetRowValues())
# Find all empty positions and return them in a list--------------------------------------------------------
    def FindEmpty(self):
        empty_values = []
        for RowNr in range(self.NumberOfRows):
            for ColNr in range(self.NumberOfColumns):
                if self.GetRow(RowNr)[ColNr].GetValue() == 0:
                    empty_values.append((RowNr, ColNr))
        return empty_values
    def GetRow(self, pRowNr):
        return self.board[pRowNr].GetRowData()