############################################################################################################
# Class: MultiLineText
############################################################################################################

# [CLASS] MultiLine TEXT ===================================================================================
class MultiLineText():
# Initialisation -------------------------------------------------------------------------------------------
    def __init__(self, Text, Font, Color, Position, MaxWidth):
        self.Text = Text
        self.Font = Font
        self.Color = Color
        self.Position = Position
        self.MaxWidth = int(MaxWidth)
# Rendering ------------------------------------------------------------------------------------------------
    def render(self, Screen):
        X = int(self.Position[0])
        Y = int(self.Position[1])
        space = self.Font.size(' ')[0]  # The width of a space.

        for Sentence in self.Text.splitlines():
            for Word in Sentence.split(' '):
                WordSurface = self.Font.render(Word, True, self.Color)
                WordWidth, WordHeight = WordSurface.get_size()
                if X + WordWidth >= self.MaxWidth:
                    X = self.Position[0]            # reset X
                    Y += WordHeight                 # jump to next line
                Screen.blit(WordSurface, (X, Y))
                X += WordWidth + space
            X = self.Position[0]
            Y += WordHeight
# ==========================================================================================================