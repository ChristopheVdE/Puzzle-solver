############################################################################################################
# Name: Solve.py
# Function: Look for positions that have only 1 valid option and update the board with those
############################################################################################################

# Import required packages =================================================================================
import copy
# ==========================================================================================================

# Look for positions that have only 1 valid option and update the board with those =========================
def Solve(pBoard):
    # Get list with all empty positions --------------------------------------------------------------------
    EmptyPositions = pBoard.FindEmpty()

    # Loop over empty positions ----------------------------------------------------------------------------
    while len(EmptyPositions) != 0:
        LastBoardState = copy.deepcopy(pBoard)

        for Empty in EmptyPositions:
            # Create list with alle possible values for the current empty position
            PossibleValues = pBoard.GetRow(Empty[0])[Empty[1]].GetPossible()
            # Update the value of the current empty position if there is only 1 possible value
            if len(PossibleValues) == 1:
                pBoard.GetRow(Empty[0])[Empty[1]].UpdateValue(PossibleValues[0], pBoard, Empty)
                del EmptyPositions[EmptyPositions.index(Empty)]

        # Break loop if no more cerrain values are found
        StilCertain = False  
        for Empty in EmptyPositions:
            if len(pBoard.GetRow(Empty[0])[Empty[1]].GetPossible()) == 1:
                StilCertain = True
            elif len(pBoard.GetRow(Empty[0])[Empty[1]].GetPossible()) == 1 and not StilCertain: 
                StilCertain = False   
        if not StilCertain or len(EmptyPositions) == 0:
            return pBoard
#===========================================================================================================