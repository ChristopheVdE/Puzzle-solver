############################################################################################################
# Function: BruteForce
############################################################################################################

# Import ===================================================================================================
import random
# Import Class-Modules -------------------------------------------------------------------------------------
from Classes.Column import Column
from Classes.Box import Box
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
            # Check possible Values to use in the bruteforce 
            pBoard.board[empty_pos[0]].Row[empty_pos[1]].CalcPossible(pBoard, empty_pos)
            options = pBoard.board[empty_pos[0]].Row[empty_pos[1]].PossibleValues

            random.shuffle(options)
        # CHECK POSSIBLE VALUES FOR EMPTY POSITION & UPDATE BOARD IF FOUND ---------------------------------
            for option in options:
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
