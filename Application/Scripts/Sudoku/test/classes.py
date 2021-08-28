############################################################################################################
# NAME: Sudoku
# AUTHOR: Christophe Van den Eynde
# FUNCTION: All scripts concerning Sudoku's for the pygame apllication
############################################################################################################

# IMPORT PACKAGES ==========================================================================================
import pygame
import random
# from Scripts.General.Classes import CenteredText
# from Settings.Default import Colors, Fonts
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
                if self.board[RowNr].Row[ColNr].Value == 0:
                    empty_values.append((RowNr, ColNr))
        return empty_values

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
            RowValues.append(self.Row[ColNr].Value)                
        return RowValues
    
# Column ===================================================================================================
class Column():
    def __init__(self, pboard, pColumnNumber):
        self.NumberOfRows = pboard.NumberOfRows
        self.Column = []
        for RowNr in range(pboard.NumberOfRows):
            self.Column.append(pboard.board[RowNr].Row[pColumnNumber])
    def GetColumnValues(self):
        ColumnValues = []
        for RowNr in range(self.NumberOfRows):
            ColumnValues.append(self.Column[RowNr].Value)                
        return ColumnValues

# 3x3 Box ===============================================================================================
class Box():
    def __init__(self, pBoard, pPosition):
        self.RowNr = (pPosition[0] // 3) * 3
        self.ColNr = (pPosition[1] // 3) * 3
        self.Box = []
        for RowNr in range(self.RowNr, self.RowNr + 3):
            for ColNr in range(self.ColNr, self.ColNr + 3):
                self.Box.append(pBoard.board[RowNr].Row[ColNr])
    def GetBoxValues(self):
        BoxValues = []
        for BoxVal in self.Box:
            BoxValues.append(BoxVal.Value)
        return BoxValues
        
# Values ===================================================================================================
class Value():
    def __init__(self):
        self.Correct = False
        self.Value = 0
        self.PossibleValues = list(range(1,10))
        self.UserPencil = []
    def UpdateValue(self, pNewValue):
        if self.Correct == False: 
            self.Value = pNewValue
    def SetValueAsCorrect(self):
        self.Correct = True

# test init ================================================================================================
x = Board((1, 1), 9, 9)

x.CreateEmptyBoard()
# x.PrintBoardValues()
#x.board[1].Row[1].UpdateValue(2)
x.PrintBoardValues()

print('row')
print(x.board[1].GetRowValues())

print('column')
y = Column(x, 1)
print(y.GetColumnValues())

print('Box')
z = Box(x, (1,1))
print(z.GetBoxValues())

# print(x.board[0].Row[0].SystemPencil)

# y = Column(x,1)

# print(y.Column[0].Value)




# Brute force a solution -----------------------------------------------------------------------------------
def BruteForce(pBoard):
    # Find empty positions --------------------------------------------------------------------
    all_empty = pBoard.FindEmpty()
    if not all_empty:
        # solution found
        return True
    else:
        options = list(range(1,10))
        # Add randomness
        for empty_pos in all_empty:
            random.shuffle(options)
        # CHECK POSSIBLE VALUES FOR EMPTY POSITION & UPDATE BOARD IF FOUND ---------------------------------
            for option in options:
                #pBoard.PrintBoardValues()
                # search row, column and box
                if (
                    not option in pBoard.board[empty_pos[0]].GetRowValues()  # row
                    and not option in Column(pBoard, empty_pos[1]).GetColumnValues()  # column
                    and not option in Box(pBoard, empty_pos).GetBoxValues()  # box
                ):
                    # update board if value is valid
                    pBoard.board[empty_pos[0]].Row[empty_pos[1]].UpdateValue(option)
                    # try a value in the next empty position if a valid value was inserted, return true if value is possible
                    if BruteForce(pBoard):
                        return True
                    # reset value if next empty has no valid number
                    pBoard.board[empty_pos[0]].Row[empty_pos[1]].UpdateValue(0)
            # required for recursive, says that next empty has no valid number
            return False

BruteForce(x)
x.PrintBoardValues()