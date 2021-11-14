############################################################################################################
# NAME: MainMenu.py
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Gameloop for the Main Menu
############################################################################################################

# Import modules ===========================================================================================
# Packages -------------------------------------------------------------------------------------------------
import pygame
# Import modules -------------------------------------------------------------------------------------------
from Display.General.Button import Button
from Display.General.CenteredText import CenteredText
from Games.Functions.ActivateGameLoop import ActivateGameLoop
from Display.Game.Menu.SubMenu import SubMenu
# Import Settings ------------------------------------------------------------------------------------------
from Settings.Default import Colors, Fonts
# ==========================================================================================================

# MAIN MENU ================================================================================================
def MainMenu(ScreenWidth, ScreenHeight, clock, Images):
# INITITIALIZE SCREEN --------------------------------------------------------------------------------------
    Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.DOUBLEBUF, 32)
# VARIABLES ------------------------------------------------------------------------------------------------
    menu = True
    SudokuSelected = False
    HudokuSelected = False
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
        Screen.fill(Colors["Background"])
    # Title
        MenuTitle = CenteredText("Puzzle Solver", Fonts["Title"], Colors["black"], ScreenWidth/2, ScreenHeight/7)
        MenuTitle.render(Screen)
# [SUBMENU] CHOOSE PUZZLE ----------------------------------------------------------------------------------
    # Title
        PuzzleType = SubMenu(Screen, 140, ScreenHeight/7 + 70, 250, 325, Colors["black"], Colors["Background"])
        PuzzleType.Outline()
        PuzzleType.Title("CHOOSE PUZZLE", Fonts["Button"], Colors["black"])
    # Select Sudoku button
        Sudoku = Button(Screen, 155, ScreenHeight / 7 + 95, 218, 40, Colors["PuzzleSelector"], Colors["PuzzleHighlight"], SudokuSelected)
        Sudoku.render(mouse)
        Sudoku.text(Fonts["Button"], Colors["black"], "Sudoku")
    # Select Hudoku button
        Hudoku = Button(Screen, 155, ScreenHeight / 7 + 145, 218, 40, Colors["PuzzleSelector"], Colors["PuzzleHighlight"], HudokuSelected)
        Hudoku.render(mouse)
        Hudoku.text(Fonts["Button"], Colors["black"], "Hudoku")
    # Select Binairo button
        Binairo = Button(Screen, 155, ScreenHeight / 7 + 195, 218, 40, Colors["PuzzleSelector"], Colors["PuzzleHighlight"], BinairoSelected)
        Binairo.render(mouse)
        Binairo.text(Fonts["Button"], Colors["black"], "Binairo")        
# [SUBMENU] PUZZLE INFO ------------------------------------------------------------------------------------
    # GENERAL ----------------------------------------------------------------------------------------------
        PuzzleInfo = SubMenu(Screen, 140 + 270, ScreenHeight/7 + 70, 250, 325, Colors["black"], Colors["Background"])
        PuzzleInfo.Outline()
        PuzzleInfo.Title("PUZZLE INFO", Fonts["Button"], Colors["black"])
    # PUZZLE INFO: SUDOKU ----------------------------------------------------------------------------------
        # Sudoku button activation
        if (Sudoku.X + Sudoku.Width > mouse[0] > Sudoku.X and Sudoku.Y + Sudoku.Height > mouse[1] > Sudoku.Y) or SudokuSelected:
            if click[0] == 1:
                SudokuSelected = True
            HudokuSelected = False
            BinairoSelected = False
        # Puzzle image & text
            PuzzleInfo.Image(Images + '\Sudoku.jpg')
            PuzzleInfo.MultiLineText("Fill a 9×9 grid.\nEach column, row and 3×3 grid should contain all digits from 1 to 9.", Fonts["Button"], Colors["black"])
        # Play button
            Play = Button(Screen, PuzzleInfo.X + 15, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Colors["Play"], Colors["PlayHighlight"])
            Play.render(mouse)
            Play.text(Fonts["Button"], Colors["black"], "PLAY")
            SelectedGame = Play.functionality(mouse, click, ActivateGameLoop("SudokuPlay"))
            if SelectedGame: return SelectedGame
        # Solve button
            Solve = Button(Screen, PuzzleInfo.X + 135, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Colors["Play"], Colors["PlayHighlight"])
            Solve.render(mouse)
            Solve.text(Fonts["Button"], Colors["black"], "SOLVE")
            SelectedGame = Solve.functionality(mouse, click, ActivateGameLoop("SudokuSolve"))
            if SelectedGame: return SelectedGame
    # PUZZLE INFO: HUDOKU ----------------------------------------------------------------------------------
        # Hudoku button activation
        if (Hudoku.X + Hudoku.Width > mouse[0] > Hudoku.X and Hudoku.Y + Hudoku.Height > mouse[1] > Hudoku.Y) or HudokuSelected:
            if click[0] == 1:
                HudokuSelected = True
            SudokuSelected = False
            BinairoSelected = False
        # Puzzle image & text
            PuzzleInfo.Image(Images + '\Hudoku.png')
            PuzzleInfo.MultiLineText("Fill a 9×9 grid.\nEach column, row and 3×3 grid should contain all digits from 1 to 9.\nThe 'H' in the middle counts as an extra grid and must also contain all values from 1 to 9", Fonts["Button"], Colors["black"])
        # Play button
            Play = Button(Screen, PuzzleInfo.X + 15, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Colors["Play"], Colors["PlayHighlight"])
            Play.render(mouse)
            Play.text(Fonts["Button"], Colors["black"], "PLAY")
            SelectedGame = Play.functionality(mouse, click, ActivateGameLoop("HudokuPlay"))
            if SelectedGame: return SelectedGame
        # Solve button
            Solve = Button(Screen, PuzzleInfo.X + 135, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Colors["Play"], Colors["PlayHighlight"])
            Solve.render(mouse)
            Solve.text(Fonts["Button"], Colors["black"], "SOLVE")
            SelectedGame = Solve.functionality(mouse, click, ActivateGameLoop("HudokuSolve"))
            if SelectedGame: return SelectedGame
    # PUZZLE INFO: BINAIRO ---------------------------------------------------------------------------------
        # Sudoku button activation
        if (Binairo.X + Binairo.Width > mouse[0] > Binairo.X and Binairo.Y + Binairo.Height > mouse[1] > Binairo.Y) or BinairoSelected:
            if click[0] == 1:
                BinairoSelected = True
            SudokuSelected = False
            HudokuSelected = False
        # Puzzle image & text
            PuzzleInfo.Image(Images + '\Binairo.png')
            PuzzleInfo.MultiLineText("Each column/ row needs to have te same ammount of 1 and 0.\nMax 2 times the same number next to eachother.\nNo identical rows/ columns alowed.", Fonts["Button"], Colors["black"])
        # Play button
            Play = Button(Screen, PuzzleInfo.X + 15, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Colors["Play"], Colors["PlayHighlight"])
            Play.render(mouse)
            Play.text(Fonts["Button"], Colors["black"], "PLAY")
            SelectedGame = Play.functionality(mouse, click, ActivateGameLoop("BinairoPlay"))
            if SelectedGame: return SelectedGame
        # Solve button
            Solve = Button(Screen, PuzzleInfo.X + 135, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Colors["Play"], Colors["PlayHighlight"])
            Solve.render(mouse)
            Solve.text(Fonts["Button"], Colors["black"], "SOLVE")
            SelectedGame = Solve.functionality(mouse, click, ActivateGameLoop("BinairoSolve"))
            if SelectedGame: return SelectedGame
# EXIT BUTTON ----------------------------------------------------------------------------------------------
        Exit = Button(Screen, ScreenWidth/2 - 50, ScreenHeight - 75, 100, 40, Colors["Navigation"], Colors["NavigationHighlight"])
        Exit.render(mouse)
        Exit.text(Fonts["Button"], Colors["black"], "EXIT")
        SelectedGame = Exit.functionality(mouse, click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)
    return ActivateGameLoop("Quit")
# ==========================================================================================================