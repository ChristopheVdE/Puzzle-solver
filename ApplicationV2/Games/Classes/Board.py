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
        for RowNr in range(self.NumberOfRows):
            self.board.append(Row(self.NumberOfColumns, RowNr))
# Console Print board --------------------------------------------------------------------------------------
    def PrintBoardValues(self):
        print()
        # Cycle rows 
        for RowNr in range(self.NumberOfRows):
            if RowNr % 3 == 0 and RowNr != 0:
                print("- " * 12)
            # Cycle Columns
            for ColNr in range(self.NumberOfColumns):
                if ColNr % 3 == 0 and ColNr != 0:
                    print(" |", end="")
                if self.GetRow(RowNr)[ColNr].GetValue() != 0:
                    print(" {}".format(self.GetRow(RowNr)[ColNr].GetValue()), end="")
                else: 
                    print(" .", end="")
                if ColNr == (self.NumberOfColumns - 1):
                    print()
# Console Print board Possible -----------------------------------------------------------------------------
    def PrintBoardPossible(self):
        print()
        for RowNr in range(self.NumberOfRows):
            print(self.board[RowNr].GetRowPossible())
# Find all empty positions and return them in a list--------------------------------------------------------
    def FindEmpty(self):
        empty_values = []
        for RowNr in range(self.NumberOfRows):
            for ColNr in range(self.NumberOfColumns):
                if self.GetRow(RowNr)[ColNr].GetValue() == 0:
                    empty_values.append((RowNr, ColNr))
        return empty_values
# Return Row Data (Full Class) ----------------------------------------------------------------------------
    def GetRow(self, pRowNr):
        return self.board[pRowNr].GetRowData()
# Return Board Dimensions ---------------------------------------------------------------------------------
    def GetBoardDimensions(self):
        return (self.NumberOfRows, self.NumberOfColumns)
# Return Board Values -------------------------------------------------------------------------------------
    def ReturnRowValuesLists(self):
        RowValuesList = []
        # Cycle rows 
        for RowNr in range(self.NumberOfRows):
            Row = []
            for ColNr in range(self.NumberOfColumns):
                Row.append(self.GetRow(RowNr)[ColNr].GetValue())
            RowValuesList.append(Row)
        return RowValuesList