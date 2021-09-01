############################################################################################################
# Name: CheckBoard.py
# Function: check the board against the solution, remove all wrong values and set al correct values al correct
############################################################################################################

def CheckBoard(pCurrentBoard, pSolution):
    for RowNr in range(pCurrentBoard.NumberOfRows):
        for ColNr in range(pCurrentBoard.NumberOfColumns):
            if pCurrentBoard.getRow(RowNr)[ColNr].GetValue() == pSolution.GetRow(RowNr)[ColNr].GetValue():
                pCurrentBoard.getRow(RowNr)[ColNr].SetValueAsCorrect()
            else:
                pCurrentBoard.getRow(RowNr)[ColNr].UpdateValue(0)