############################################################################################################
# NAME: Menu
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Gameloop for the Main Menu
############################################################################################################

# Import modules ===========================================================================================
# Packages -------------------------------------------------------------------------------------------------
import os
import sys
import pygame
import importlib
# Import modules -------------------------------------------------------------------------------------------
from Scripts.General.Classes import Button, CenteredText, MultiLineText, Submenu
from Scripts.General.Functions import quitgame, ActivateGameLoop
from Settings.Colors import Colors
from Settings.Fonts import Fonts
# ==========================================================================================================

# MAIN MENU ================================================================================================
def MainMenu(Screen, ScreenWidth, ScreenHeight, clock, Images):
    menu = True
    # if button was Pressed
    SudokuSelected = False
    BinairoSelected = False
# MAIN LOOP ------------------------------------------------------------------------------------------------
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
    # Get mouse position & track mouse-clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
    # Background
        Screen.fill(Colors["BackgroundColor"])
    # Title
        MenuTitle = CenteredText("Puzzle Solver", Fonts["TitleFont"], Colors["black"], ScreenWidth/2, ScreenHeight/7)
        MenuTitle.render(Screen)
# [SUBMENU] CHOOSE PUZZLE ----------------------------------------------------------------------------------
    # Title
        PuzzleType = Submenu(Screen, 140, ScreenHeight/7 + 70, 250, 325, Colors["black"], Colors["BackgroundColor"])
        PuzzleType.Outline()
        PuzzleType.Title("CHOOSE PUZZLE", Fonts["ButtonFont"], Colors["black"])
    # Select Sudoku button
        Sudoku = Button(Screen, 155, ScreenHeight / 7 + 95, 218, 40, Colors["ButtonColor"], Colors["HighlightColor"], SudokuSelected)
        Sudoku.render(mouse)
        Sudoku.text(Fonts["ButtonFont"], Colors["black"], "Sudoku")
    # Select Binairo button
        Binairo = Button(Screen, 155, ScreenHeight / 7 + 145, 218, 40, Colors["ButtonColor"], Colors["HighlightColor"], BinairoSelected)
        Binairo.render(mouse)
        Binairo.text(Fonts["ButtonFont"], Colors["black"], "Binairo")        
# [SUBMENU] PUZZLE INFO ------------------------------------------------------------------------------------
    # GENERAL ----------------------------------------------------------------------------------------------
        PuzzleInfo = Submenu(Screen, 140 + 270, ScreenHeight/7 + 70, 250, 325, Colors["black"], Colors["BackgroundColor"])
        PuzzleInfo.Outline()
        PuzzleInfo.Title("PUZZLE INFO", Fonts["ButtonFont"], Colors["black"])
    # PUZZLE INFO: SUDOKU ----------------------------------------------------------------------------------
        # Sudoku button activation
        if (Sudoku.X + Sudoku.Width > mouse[0] > Sudoku.X and Sudoku.Y + Sudoku.Height > mouse[1] > Sudoku.Y) or SudokuSelected:
            if click[0] == 1:
                SudokuSelected = True
            BinairoSelected = False
        # Puzzle image & text
            PuzzleInfo.Image(Images + '\Sudoku.jpg')
            PuzzleInfo.MultiLineText("Fill a 9×9 grid.\nEach column, row and 3×3 grid should contain all digits from 1 to 9.", Fonts["ButtonFont"], Colors["black"])
        # Play button
            Play = Button(Screen, PuzzleInfo.X + 15, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Colors["Playbutton"], Colors["PlayHighlight"])
            Play.render(mouse)
            Play.text(Fonts["ButtonFont"], Colors["black"], "PLAY")
            SelectedGame = Play.functionality(mouse, click, ActivateGameLoop("SudokuPlay"))
            if SelectedGame: return SelectedGame
        # Solve button
            Solve = Button(Screen, PuzzleInfo.X + 135, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Colors["Playbutton"], Colors["PlayHighlight"])
            Solve.render(mouse)
            Solve.text(Fonts["ButtonFont"], Colors["black"], "SOLVE")
            SelectedGame = Solve.functionality(mouse, click, ActivateGameLoop("SudokuSolve"))
            if SelectedGame: return SelectedGame
    # PUZZLE INFO: BINAIRO ---------------------------------------------------------------------------------
        # Sudoku button activation
        if (Binairo.X + Binairo.Width > mouse[0] > Binairo.X and Binairo.Y + Binairo.Height > mouse[1] > Binairo.Y) or BinairoSelected:
            if click[0] == 1:
                BinairoSelected = True
            SudokuSelected = False
        # Puzzle image & text
            PuzzleInfo.Image(Images + '\Binairo.png')
            PuzzleInfo.MultiLineText("Each column/ row needs to have te same ammount of 1 and 0.\nMax 2 times the same number next to eachother.\nNo identical rows/ columns alowed.", Fonts["ButtonFont"], Colors["black"])
        # Play button
            Play = Button(Screen, PuzzleInfo.X + 15, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Colors["Playbutton"], Colors["PlayHighlight"])
            Play.render(mouse)
            Play.text(Fonts["ButtonFont"], Colors["black"], "PLAY")
            SelectedGame = Play.functionality(mouse, click, ActivateGameLoop("BinairoPlay"))
            if SelectedGame: return SelectedGame
        # Solve button
            Solve = Button(Screen, PuzzleInfo.X + 135, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Colors["Playbutton"], Colors["PlayHighlight"])
            Solve.render(mouse)
            Solve.text(Fonts["ButtonFont"], Colors["black"], "SOLVE")
            SelectedGame = Solve.functionality(mouse, click, ActivateGameLoop("BinairoSolve"))
            if SelectedGame: return SelectedGame
# EXIT BUTTON ----------------------------------------------------------------------------------------------
        Exit = Button(Screen, ScreenWidth/2 - 50, ScreenHeight - 75, 100, 40, Colors["NavigationColor"], Colors["NavigationHighlight"])
        Exit.render(mouse)
        Exit.text(Fonts["ButtonFont"], Colors["black"], "EXIT")
        SelectedGame = Exit.functionality(mouse, click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)
    return ActivateGameLoop("Quit")
# ==========================================================================================================