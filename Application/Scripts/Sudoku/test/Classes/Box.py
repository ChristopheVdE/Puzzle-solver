############################################################################################################
# Class: Box
############################################################################################################

# 3x3 Box ===============================================================================================
class Box():
    def __init__(self, pBoard, pPosition):
        self.RowNr = (pPosition[0] // 3) * 3
        self.ColNr = (pPosition[1] // 3) * 3
        self.Box = []
        for RowNr in range(self.RowNr, self.RowNr + 3):
            for ColNr in range(self.ColNr, self.ColNr + 3):
                self.Box.append(pBoard.GetRow(RowNr)[ColNr])
    def GetBoxValues(self):
        BoxValues = []
        for BoxVal in self.Box:
            BoxValues.append(BoxVal.GetValue())
        return BoxValues