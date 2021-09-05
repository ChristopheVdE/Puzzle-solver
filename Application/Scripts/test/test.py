
# Import ===================================================================================================
# Import Class-Modules -------------------------------------------------------------------------------------
from Classes.Board import Board
from Classes.Box import Box
from Classes.Column import Column
# Import Functions -----------------------------------------------------------------------------------------
from Functions.Sudoku.BruteForce import BruteForce
from Functions.Sudoku.CreateSolvableState import SolvableState
from Functions.GetHint import GetHint
# ==========================================================================================================

# test init ================================================================================================
x = Board((1, 1), 9, 9)

x.CreateEmptyBoard()
# x.PrintBoardValues()
x.GetRow(1)[1].UpdateValue(2, x, (1,1))
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


# Create solution
BruteForce(x)
x.PrintBoardValues()
# Create Solvable State
y = SolvableState(x)
y.PrintBoardValues()
# Get Hint (fill in 1 certain value)
y = GetHint(y, 'Sudoku')
y.PrintBoardValues()

