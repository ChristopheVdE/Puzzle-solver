############################################################################################################
# Class: SubMenu
############################################################################################################

# Imports ==================================================================================================
import pygame
from Display.General.CenteredText import CenteredText
from Display.General.MultiLineText import MultiLineText
# ==========================================================================================================

# [CLASS] SUBMENU ==========================================================================================
class SubMenu():
# Initialisation -------------------------------------------------------------------------------------------
    def __init__(self, Screen, X, Y, Width, Height, EdgeColor, InnerColor):
        self.Screen = Screen
        self.X = int(X)
        self.Y = int(Y)
        self.Width = int(Width)
        self.Height = int(Height)
        self.EdgeColor = EdgeColor
        self.InnerColor = InnerColor
# Submenu outline ------------------------------------------------------------------------------------------
    def Outline(self):
        # Submenu - outline
        pygame.draw.rect(self.Screen, self.EdgeColor, (self.X - 2, self.Y - 2, self.Width + 4, self.Height + 4))
        # Submenu - color
        pygame.draw.rect(self.Screen, self.InnerColor, (self.X, self.Y, self.Width, self.Height))
# Submenu title --------------------------------------------------------------------------------------------
    def Title(self, Text, Font, Color):
        # Get text size
        TextSurface = Font.render(Text, True, Color)
        TextWidth, TextHeight = TextSurface.get_size()
        # Text outline & background
        #Text_X = (self.X + self.Width + 2) - (TextWidth)*1.5      
        pygame.draw.rect(self.Screen, self.EdgeColor, (self.X + self.Width/8 - 2, self.Y - TextHeight*1.5/2 - 2, self.Width/8*6 +4, TextHeight * 1.5 + 4))
        pygame.draw.rect(self.Screen, self.InnerColor, (self.X + self.Width/8, self.Y -TextHeight*1.5/2, self.Width/8*6, TextHeight * 1.5))
        # Text
        Text_X = (self.X + self.Width/2 +2 )
        Title = CenteredText(Text, Font, Color, Text_X, self.Y)
        Title.render(self.Screen)
# Submenu image --------------------------------------------------------------------------------------------
    def Image(self, Image):
        Image = pygame.image.load(Image)
        Image = pygame.transform.scale(Image, (115, 115))
        ImageArea = Image.get_rect()
        ImageArea.center = (self.X + self.Width/2, self.Y +80)
        self.Screen.blit(Image, ImageArea)
# Submenu text ---------------------------------------------------------------------------------------------
    def MultiLineText(self, Text, Font, Color):
        self.Text = MultiLineText(Text, Font, Color, (self.X + 10, int(self.Y + 80 + 150/ 2)), self.X + self.Width - 20)
        self.Text.render(self.Screen)
# ===========================================================================================================
