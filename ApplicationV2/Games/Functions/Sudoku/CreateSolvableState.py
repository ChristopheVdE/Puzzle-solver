############################################################################################################
# Name: CreateSolvableState.py
# Function: Remove values from a fully filled in board (as long as there is only 1 solution) to create a solvable boardstate
############################################################################################################

# Import required packages =================================================================================
import copy
import random
from Games.Functions.Sudoku.Solve import Solve
# ==========================================================================================================

# Solvable state ===========================================================================================
def SolvableState(pSolution):
    # Create list of coordinates in board ------------------------------------------------------------------
    coords = []
    for RowNr in range(pSolution.GetBoardDimensions()[0]):
        for ColNr in range(pSolution.GetBoardDimensions()[1]):
            coords.append((RowNr, ColNr))
    
    # Create duplicate boards for testing ------------------------------------------------------------------
    EmptiedBoard = copy.deepcopy(pSolution)

    # Loop through coordinates and see if removal of value at coord still gives same solution of board -----
    RemovedCoordsCount = 0

    while len(coords) != 0:
        # Choose a random position out of coordinates 
        position = random.choice(coords)

        # Create duplicate of the emptied board (used for solving and comparing solution to original solution)
        TestBoard = copy.deepcopy(EmptiedBoard)

        # Update testboard with empty value
        TestBoard.GetRow(position[0])[position[1]].UpdateValue(0, TestBoard, position)
        RemovedCoordsCount += 1

        # Start testing if board is still solvable without guessing when 1/3 of the board values have been removed
        if RemovedCoordsCount >= (pSolution.GetBoardDimensions()[0] * pSolution.GetBoardDimensions()[1]) / 3:
            # Test if solution of board is still the same (stop board from having multiple solutions)
            TestBoard = Solve(TestBoard)
        
            if TestBoard.ReturnRowValuesLists() == pSolution.ReturnRowValuesLists():
                EmptiedBoard.GetRow(position[0])[position[1]].UpdateValue(0, EmptiedBoard, position)
            else:
                break

            # Remove tested position out of coordinates list using the postions index in the coords list
            del coords[coords.index(position)]
        else:
            EmptiedBoard.GetRow(position[0])[position[1]].UpdateValue(0, EmptiedBoard, position)
            del coords[coords.index(position)]    

    # Set all remaining values a correct ------------------------------------------------------------------------
    for RowNr in range(EmptiedBoard.GetBoardDimensions()[0]):
        for ColNr in range(EmptiedBoard.GetBoardDimensions()[1]):
            if EmptiedBoard.GetRow(RowNr)[ColNr].GetValue() != 0:
                EmptiedBoard.GetRow(RowNr)[ColNr].SetValueAsCorrect()

    # Return final board ----------------------------------------------------------------------------------------
    return EmptiedBoard
#================================================================================================================