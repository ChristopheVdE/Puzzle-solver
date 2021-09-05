############################################################################################################
# Name: Solve.py
# Function: Look for positions that have only 1 valid option and update the board with those
############################################################################################################

# Import required packages =================================================================================
import copy
# ==========================================================================================================

# Look for positions that have only 1 valid option and update the board with those =========================
def Solve(pBoard, pHint = False):
    # Get list with all empty positions --------------------------------------------------------------------
    EmptyPositions = pBoard.FindEmpty()

    # Loop over empty positions ----------------------------------------------------------------------------
    SolveCount = 0

    while len(EmptyPositions) != 0:
        LastBoardState = copy.deepcopy(pBoard)

        for Empty in EmptyPositions:
            if (pHint == True and SolveCount <= 1) or pHint == False:
                # Create list with alle possible values for the current empty position
                PossibleValues = pBoard.GetRow(Empty[0])[Empty[1]].GetPossible()
                # Update the value of the current empty position if there is only 1 possible value
                if len(PossibleValues) == 1:
                    pBoard.GetRow(Empty[0])[Empty[1]].UpdateValue(PossibleValues[0], pBoard, Empty)
                    del EmptyPositions[EmptyPositions.index(Empty)]
                    SolveCount += 1
                    if pHint == True and SolveCount >= 1:
                        break

        # See if there are still empty, certain values on the board
        StilCertain = False    
        if pHint == True:
            StilCertain = False      
        else:
            for Empty in EmptyPositions:
                if len(pBoard.GetRow(Empty[0])[Empty[1]].GetPossible()) == 1:
                    StilCertain = True
                elif len(pBoard.GetRow(Empty[0])[Empty[1]].GetPossible()) == 1 and not StilCertain: 
                    StilCertain = False   

        # Break loop if no more cerrain values are found
        if not StilCertain or len(EmptyPositions) == 0:
            return pBoard
#===========================================================================================================