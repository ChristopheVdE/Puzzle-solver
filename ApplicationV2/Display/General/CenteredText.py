############################################################################################################
# Class: CenteredText
############################################################################################################

# [CLASS] CENTERED TEXT ====================================================================================
class CenteredText():
# Initialisation -------------------------------------------------------------------------------------------
    def __init__(self, Text, Font, Color, X, Y):
        self.Text = Text
        self.Font = Font
        self.Color = Color
        self.Position = (int(X), int(Y))
# Rendering ------------------------------------------------------------------------------------------------
    def render(self, Screen):
        TextSurface = self.Font.render(self.Text, True, self.Color)
        TextArea = TextSurface.get_rect()
        TextArea.center  = self.Position
        Screen.blit(TextSurface, TextArea)
# ==========================================================================================================