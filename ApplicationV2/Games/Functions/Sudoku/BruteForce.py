############################################################################################################
# Function: BruteForce
############################################################################################################

# Import ===================================================================================================
import random
# Import Class-Modules -------------------------------------------------------------------------------------
from Games.Classes.Column import Column
from Games.Classes.Box import Box
from Games.Functions.Sudoku.CalcPossible import CalcAllPossible, CalcPossible
# ==========================================================================================================

# Brute force a solution -----------------------------------------------------------------------------------
def BruteForce(pBoard):
    # Find empty positions ---------------------------------------------------------------------------------
    all_empty = pBoard.FindEmpty()
    if not all_empty:
        # solution found
        return True
    else:
        options = list(range(1,10))
        # Add randomness
        for empty_pos in all_empty:
            RowNr, ColNr = empty_pos
            # Check possible Values to use in the bruteforce 
            CalcPossible(pBoard, empty_pos)
            options = pBoard.GetRow(RowNr)[ColNr].GetPossible()

            random.shuffle(options)
        # CHECK POSSIBLE VALUES FOR EMPTY POSITION & UPDATE BOARD IF FOUND ---------------------------------
            for option in options:
                # search row, column and box
                if (
                    not option in pBoard.GetRowValues(RowNr)  # row
                    and not option in Column(pBoard, ColNr).GetColumnValues()  # column
                    and not option in Box(pBoard, empty_pos).GetBoxValues()  # box
                ):
                    # update board if value is valid
                    pBoard.GetRow(RowNr)[ColNr].UpdateValue(option)
                    CalcAllPossible(pBoard, empty_pos)
                    # try a value in the next empty position if a valid value was inserted, return true if value is possible
                    if BruteForce(pBoard):
                        return True
                    # reset value if next empty has no valid number
                    pBoard.GetRow(RowNr)[ColNr].UpdateValue(0)
                    CalcAllPossible(pBoard, empty_pos)
            # required for recursive, says that next empty has no valid number
            return False
