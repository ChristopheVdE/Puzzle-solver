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
        self.ButtonY = self.Y
        self.Width = int(Width)
        self.Height = int(Height)
        self.EdgeColor = EdgeColor
        self.InnerColor = InnerColor
# Menu Outline ---------------------------------------------------------------------------------------------
    def MenuOutline(self):
        outline = SubMenu(self.Screen, self.X, self.Y, self.Width, self.Height, Colors["black"], Colors["Background"])
        outline.Outline()
        outline.Title("Sudoku", Fonts["Button"], Colors["black"])
        self.X += 5
        self.Y += 25
# OPTIONS BUTTONS ------------------------------------------------------------------------------------------
    def OptionButtons(self, pMouse, pMode = 'Play'):
        self.ButtonY = self.Y
    # Create new board -------------------------------------------------------------------------------------
        self.New = Button(self.Screen, self.X, self.ButtonY, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        self.New.render(pMouse)
        self.New.text(Fonts["Button"], Colors["black"], "New")
        self.ButtonY += 45
    # Reset board ------------------------------------------------------------------------------------------
        self.Reset = Button(self.Screen, self.X, self.ButtonY, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        self.Reset.render(pMouse)
        self.Reset.text(Fonts["Button"], Colors["black"], "Reset")
        self.ButtonY += 45
    # Get Hint ---------------------------------------------------------------------------------------------
        self.Hint = Button(self.Screen, self.X, self.ButtonY, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        self.Hint.render(pMouse)
        self.Hint.text(Fonts["Button"], Colors["black"], "Hint")
        self.ButtonY += 45
    # Solve or check ---------------------------------------------------------------------------------------
        if pMode == 'Play':
        # Check current (partial) board --------------------------------------------------------------------
            self.Check = Button(self.Screen, self.X, self.ButtonY, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
            self.Check.render(pMouse)
            self.Check.text(Fonts["Button"], Colors["black"], "Check")
            self.ButtonY += 45
        else:
        # Check current (partial) board --------------------------------------------------------------------
            self.Solve = Button(self.Screen, self.X, self.ButtonY, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
            self.Solve.render(pMouse)
            self.Solve.text(Fonts["Button"], Colors["black"], "Solve")
            self.ButtonY += 45            
# NAVIGATION BUTTONS ---------------------------------------------------------------------------------------
    def NavigationButtons(self, pMouse, Click):
        ButtonX = self.X
        self.ButtonY += 50
    # Display: Menu button ---------------------------------------------------------------------------------
        Menu = Button(self.Screen, ButtonX, self.ButtonY, 65, 40, Colors["Navigation"], Colors["NavigationHighlight"])
        Menu.render(pMouse)
        Menu.text(Fonts["Button"], Colors["black"], "MENU")
        ButtonX += 70
    # Display: Exit Button ---------------------------------------------------------------------------------
        Exit = Button(self.Screen, ButtonX, self.ButtonY, 65, 40, Colors["Navigation"], Colors["NavigationHighlight"])
        Exit.render(pMouse)
        Exit.text(Fonts["Button"], Colors["black"], "QUIT") 
    # Functions --------------------------------------------------------------------------------------------
        SelectedGame = Menu.functionality(pMouse, Click, ActivateGameLoop("Menu"))
        if SelectedGame: return SelectedGame
        SelectedGame = Exit.functionality(pMouse, Click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# ==========================================================================================================
