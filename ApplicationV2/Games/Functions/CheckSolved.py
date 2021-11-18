############################################################################################################
# Name: CkeckSolved.py
# Function: Compares current board to solution and returns wheter current board is solved
############################################################################################################

def CheckSolved(pCurrentBoard, pSolution):
    BoardDimensions = pCurrentBoard.GetBoardDimensions()
    for row in range(BoardDimensions[0]):
        for col in range(BoardDimensions[1]):
            if pCurrentBoard.GetRow(row)[col].GetValue() != pSolution.GetRow(row)[col].GetValue():
                return False
    return True