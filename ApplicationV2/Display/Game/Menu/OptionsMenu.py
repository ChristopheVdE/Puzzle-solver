############################################################################################################
# Class: OptionsMenu
############################################################################################################

# Imports ==================================================================================================
# Display modules ------------------------------------------------------------------------------------------
from Display.Game.Menu.SubMenu import SubMenu
from Display.General.Button import Button
# Functions ------------------------------------------------------------------------------------------------
from Games.Functions.ActivateGameLoop import ActivateGameLoop
# Settings -------------------------------------------------------------------------------------------------
from Settings.Default import Colors, Fonts
# ==========================================================================================================

# [CLASS] SUBMENU ==========================================================================================
class OptionsMenu():
# Initialisation -------------------------------------------------------------------------------------------
    def __init__(self, Screen, X, Y, Width, Height, EdgeColor, InnerColor):
        self.Screen = Screen
        self.X = int(X)
        self.Y = int(Y)
        self.Width = int(Width)
        self.Height = int(Height)
        self.EdgeColor = EdgeColor
        self.InnerColor = InnerColor
# Menu Outline ---------------------------------------------------------------------------------------------
    def MenuOutline(self):
        outline = SubMenu(self.Screen, self.X, self.Y, self.Width, self.Height, Colors["black"], Colors["Background"])
        outline.Outline()
        outline("Sudoku", Fonts["Button"], Colors["black"])
# OPTIONS BUTTONS ------------------------------------------------------------------------------------------
    def OptionButtons(self, Mouse):
    # Create new board -------------------------------------------------------------------------------------
        New = Button(self.Screen, self.Width - 160, self.Height/2 - 120, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        New.render(Mouse)
        New.text(Fonts["Button"], Colors["black"], "New")
    # Reset board ------------------------------------------------------------------------------------------
        Reset = Button(self.Screen, self.Width - 160, self.Height/2 - 70, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        Reset.render(Mouse)
        Reset.text(Fonts["Button"], Colors["black"], "Reset")
    # Get Hint ---------------------------------------------------------------------------------------------
        Hint = Button(self.Screen, self.Width - 160, self.Height/2 - 20, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        Hint.render(Mouse)
        Hint.text(Fonts["Button"], Colors["black"], "Hint")
    # Check current (partial) board ------------------------------------------------------------------------
        Check = Button(self.Screen, self.Width - 160, self.Height/2 + 30, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        Check.render(Mouse)
        Check.text(Fonts["Button"], Colors["black"], "Check")
# NAVIGATION BUTTONS ---------------------------------------------------------------------------------------
    def NavigationButtons(self, Mouse, Click):
    # Display: Menu button ---------------------------------------------------------------------------------
        Menu = Button(self.Screen, self.Width - 160, self.Height/2 + 90, 65, 40, Colors["Navigation"], Colors["NavigationHighlight"])
        Menu.render(Mouse)
        Menu.text(Fonts["Button"], Colors["black"], "MENU")
    # Display: Exit Button ---------------------------------------------------------------------------------
        Exit = Button(self.Screen, self.Width - 90, self.Height/2 + 90, 65, 40, Colors["Navigation"], Colors["NavigationHighlight"])
        Exit.render(Mouse)
        Exit.text(Fonts["Button"], Colors["black"], "QUIT") 
    # Functions --------------------------------------------------------------------------------------------
        SelectedGame = Menu.functionality(Mouse, Click, ActivateGameLoop("Menu"))
        if SelectedGame: return SelectedGame
        SelectedGame = Exit.functionality(Mouse, Click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# ==========================================================================================================
