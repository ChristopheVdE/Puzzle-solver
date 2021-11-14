############################################################################################################
# Class: Board
############################################################################################################

# Import ===================================================================================================
import pygame
from Display.General.CenteredText import CenteredText
# ==========================================================================================================

# [CLASS] INTERACTIVE BUTTONS ==============================================================================
class Button():
# Initialisation -------------------------------------------------------------------------------------------
    def __init__(self, Screen, X, Y, Width, Height, NormalColor, HighlightColor, SelectedPuzzle = False):
        self.Screen = Screen
        self.X = int(X)
        self.Y = int(Y)
        self.Width = int(Width)
        self.Height = int(Height)
        self.NormalColor = NormalColor
        self.HighlightColor = HighlightColor
        self.Selected = SelectedPuzzle
# Rendering & Highlight-------------------------------------------------------------------------------------
    def render(self, mouse):
        if (self.X + self.Width > mouse[0] > self.X and self.Y + self.Height > mouse[1] > self.Y) or self.Selected:
            pygame.draw.rect(self.Screen, self.HighlightColor, (self.X, self.Y, self.Width, self.Height))
        else:
            pygame.draw.rect(self.Screen, self.NormalColor, (self.X, self.Y, self.Width, self.Height))
# Adding text to button  -----------------------------------------------------------------------------------
    def text(self, Font, Color, Text):
        self.text = CenteredText(Text, Font, Color, int(self.X + (self.Width / 2)), int(self.Y + (self.Height / 2)))
        self.text.render(self.Screen)
# Adding image to button -----------------------------------------------------------------------------------
    def image(self, Image):
        Image = pygame.image.load(Image)
        Image = pygame.transform.scale(Image, (self.Width, self.Height))
        ImageArea = Image.get_rect()
        ImageArea.center = (self.X + self.Width/2, self.Y + self.Height/2)
        self.Screen.blit(Image, ImageArea)
# Adding functionality to Button ---------------------------------------------------------------------------
    def functionality(self, mouse, click, function):
        if self.X + self.Width > mouse[0] > self.X and self.Y + self.Height > mouse[1] > self.Y and click[0] == 1:
            return function
# ==========================================================================================================