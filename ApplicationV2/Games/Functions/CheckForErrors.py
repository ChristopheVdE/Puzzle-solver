############################################################################################################
# Name: CheckForErrors.py
# Function: check the board against the solution, remove all wrong values and set al correct values as correct
############################################################################################################

def CheckForErrors(pCurrentBoard, pSolution):
    for RowNr in range(pCurrentBoard.NumberOfRows):
        for ColNr in range(pCurrentBoard.NumberOfColumns):
            if pCurrentBoard.GetRow(RowNr)[ColNr].GetValue() == pSolution.GetRow(RowNr)[ColNr].GetValue():
                pCurrentBoard.GetRow(RowNr)[ColNr].SetValueAsCorrect()
            else:
                pCurrentBoard.GetRow(RowNr)[ColNr].UpdateValue(0, pCurrentBoard, (RowNr, ColNr))
    return pCurrentBoard