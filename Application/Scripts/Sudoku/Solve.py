############################################################################################################
# NAME: Sudoku: create
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Create playable boards
############################################################################################################

# IMPORT PACKAGES ==========================================================================================
import pygame
from Scripts.General.Classes import Button, CenteredText, Submenu
from Scripts.General.Functions import ActivateGameLoop, quitgame
from Scripts.Sudoku.Functions import board
from Settings.Default import Colors, Fonts
# ==========================================================================================================

# GAME LOOP: Sudoku ========================================================================================
def Sudoku_GameLoop(ScreenWidth, ScreenHeight, clock):
# VARIABLES ------------------------------------------------------------------------------------------------
    running = True
    grid = None
# INITITIALIZE SCREEN --------------------------------------------------------------------------------------
    Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.DOUBLEBUF|pygame.HWSURFACE, 32)
# MAIN LOOP ------------------------------------------------------------------------------------------------
    while running:
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_KP0 or event.key == pygame.K_DELETE:
                    key = '0'
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = '1'
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    key = '2'
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    key = '3'
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    key = '4'
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    key = '5'
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    key = '6'
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    key = '7'
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    key = '8'
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    key = '9'
# MOUSE POSITION & CLICKS ----------------------------------------------------------------------------------
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
# SCREEN BACKGOURND ----------------------------------------------------------------------------------------
        Screen.fill(Colors["Background"])
# OPTIONS SUBMENU ------------------------------------------------------------------------------------------
        Title = Submenu(Screen, ScreenWidth - 165, ScreenHeight / 2 - 150, 145, 300, Colors["black"], Colors["Background"])
        Title.Outline()
        Title.Title("Sudoku", Fonts["Button"], Colors["black"])
# OPTIONS BUTTONS ------------------------------------------------------------------------------------------
    # Create new board -------------------------------------------------------------------------------------
        New = Button(Screen, ScreenWidth - 160, ScreenHeight/2 - 120, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        New.render(mouse)
        New.text(Fonts["Button"], Colors["black"], "New")
    # Reset board ------------------------------------------------------------------------------------------
        Solve = Button(Screen, ScreenWidth - 160, ScreenHeight/2 - 70, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        Solve.render(mouse)
        Solve.text(Fonts["Button"], Colors["black"], "Solve")
# NAVIGATION BUTTONS ---------------------------------------------------------------------------------------
    # Menu button ------------------------------------------------------------------------------------------
        Menu = Button(Screen, ScreenWidth - 160, ScreenHeight/2 + 90, 65, 40, Colors["Navigation"], Colors["NavigationHighlight"])
        Menu.render(mouse)
        Menu.text(Fonts["Button"], Colors["black"], "MENU")
        SelectedGame = Menu.functionality(mouse, click, ActivateGameLoop("Menu"))
        if SelectedGame: return SelectedGame
    # Exit Button ------------------------------------------------------------------------------------------
        Exit = Button(Screen, ScreenWidth - 90, ScreenHeight/2 + 90, 65, 40, Colors["Navigation"], Colors["NavigationHighlight"])
        Exit.render(mouse)
        Exit.text(Fonts["Button"], Colors["black"], "QUIT")
        SelectedGame = Exit.functionality(mouse, click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# BOARD ----------------------------------------------------------------------------------------------------
    # Create new Board -------------------------------------------------------------------------------------
        if not grid or New.functionality(mouse, click, True):
            # Display update
            pygame.display.update()
            # Initialize board
            grid = board((ScreenWidth, ScreenHeight))
            # Create empy board
            grid.CreateEmptyBoard()
            # Current board = solvable board (= empty board)
            grid.CurrentBoard()
            # Print Background
            grid.CenterRectangle(ScreenWidth, ScreenHeight, 175, 0)
            # Slight delay (for smaller boards)
            pygame.time.delay(100)
    # Solve board ------------------------------------------------------------------------------------------
        elif Solve.functionality(mouse, click, True):
            grid.PrepareSolve()
            # check for errors on raw input before looking for cerain values
            if not grid.Errors():
                # Find certain values & update board with them
                grid.FindCertain()
            # check for errors on processed input before brute forcing solution (extra safety)
                if not grid.Errors():
                    grid.BruteForce()                
            grid.PrepareRender()
    # Row/col higlighting ----------------------------------------------------------------------------------
        grid.BoardBackground(Colors["black"])
        grid.DrawCubes(Colors["Cube"], Colors["Correct"])
        grid.HiglightLines(Colors["Navigation"], mouse)
    # Allow board updates ----------------------------------------------------------------------------------
        grid.SelectCube(mouse, click)       
        grid.Updatecube(key)
    # Print values -----------------------------------------------------------------------------------------
        grid.PrintBoard(Screen)
        grid.CheckBoard(Screen, Fonts["Message"], Colors["Message"])
# UPDATE DISPLAY: BOARD ------------------------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================



















