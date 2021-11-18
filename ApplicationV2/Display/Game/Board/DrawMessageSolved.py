############################################################################################################
# Function: Render Message: Board solved
############################################################################################################

# Import ===================================================================================================
from Display.General.CenteredText import CenteredText
from Settings.Default import Colors, Fonts
# ==========================================================================================================

# Check board ----------------------------------------------------------------------------------------------
def RenderMessageSolved(pScreen, pCurrentBoard, pSolution):
    if pCurrentBoard == pSolution:
        if pCurrentBoard.FindEmpty():
            Message = CenteredText("Impossible", Fonts["Message"], Colors["Message"], self.X + self.BoardSize/ 2, self.Y + self.BoardSize / 2)
            Message.render(pScreen)
        else:
            Message = CenteredText("Solved", Fonts["Message"], Colors["Message"], self.X + self.BoardSize/ 2, self.Y + self.BoardSize / 2)
            Message.render(pScreen)
        return True
    else:
        return False