############################################################################################################
# Name: CreateSolvableState.py
# Function: Remove values from a fully filled in board (as long as there is only 1 solution) to create a solvable boardstate
############################################################################################################

# Import required packages =================================================================================
import copy
import random
from Games.Functions.Sudoku.Solve import Solve
from Games.Functions.Sudoku.CalcPossible import CalcAllPossible
# ==========================================================================================================

# Solvable state ===========================================================================================
def SolvableState(pSolution):
    # Create list of coordinates in board ------------------------------------------------------------------
    coords = []
    Rows, Cols = pSolution.GetBoardDimensions()
    for RowNr in range(Rows):
        for ColNr in range(Cols):
            coords.append((RowNr, ColNr))
    
    # Create duplicate boards for testing ------------------------------------------------------------------
    EmptiedBoard = copy.deepcopy(pSolution)

    # Loop through coordinates and see if removal of value at coord still gives same solution of board -----
    RemovedCoordsCount = 0

    while len(coords) != 0:
        # Choose a random position out of coordinates 
        position = random.choice(coords)
        RowNr, ColNr = position

        # Create duplicate of the emptied board (used for solving and comparing solution to original solution)
        TestBoard = copy.deepcopy(EmptiedBoard)

        # Update testboard with empty value
        TestBoard.GetRow(RowNr)[ColNr].UpdateValue(0)
        CalcAllPossible(TestBoard, position)
        RemovedCoordsCount += 1

        # Test if solution of board is still the same (stop board from having multiple solutions)
        TestBoard = Solve(TestBoard, False)
    
        if TestBoard.ReturnRowValuesLists() == pSolution.ReturnRowValuesLists():
            EmptiedBoard.GetRow(RowNr)[ColNr].UpdateValue(0)
            CalcAllPossible(EmptiedBoard, position)
        else:
            TestBoard = copy.deepcopy(EmptiedBoard)
            CalcAllPossible(TestBoard, position)

        # Remove tested position out of coordinates list using the postions index in the coords list
        del coords[coords.index(position)]

    # Set all remaining values a correct ------------------------------------------------------------------------
    for RowNr in range(EmptiedBoard.GetBoardDimensions()[0]):
        for ColNr in range(EmptiedBoard.GetBoardDimensions()[1]):
            if EmptiedBoard.GetRow(RowNr)[ColNr].GetValue() != 0:
                EmptiedBoard.GetRow(RowNr)[ColNr].SetValueAsCorrect()

    # Return final board ----------------------------------------------------------------------------------------
    return EmptiedBoard
#================================================================================================================