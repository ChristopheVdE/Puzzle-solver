############################################################################################################
# NAME: Binairo: create
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Create playable boards
############################################################################################################

# IMPORT PACKAGES ==========================================================================================
import pygame
from Scripts.General.Classes import Button, CenteredText
from Scripts.General.Functions import ActivateGameLoop, quitgame
from Scripts.Binairo.Functions import board, UpdateBoard
from Settings.Colors import Colors
from Settings.Fonts import Fonts
# ==========================================================================================================

# GAME LOOP: Binairo =======================================================================================
def Binairo_GameLoop(Screen, ScreenWidth, ScreenHeight, clock):
# VARIABLES ------------------------------------------------------------------------------------------------
    running = True
    key = None
    Cube = None
    CreatedBoard = None
    grid = None
# MAIN LOOP ------------------------------------------------------------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_KP0: # cheks for keypress --> combing keypress check with selected cube to update value in cube
                    key = '0'
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = '1'
                if event.key == pygame.K_DELETE or event.key == pygame.K_KP_PERIOD:
                    key = '.'
            #if event.key == pygame.K_DELETE:

    # Wheter or not to return to menu when leaving the sudoku window
        BackToMenu = False
    # Set background color
        Screen.fill(Colors["BackgroundColor"])
    # Display title
        Title = CenteredText("Binairo", Fonts["TitleFont"], Colors["black"], int(ScreenWidth / 2), 50)
        Title.render(Screen)
    # Get mouse position & track mouse-clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
# SETTINGS WINDOW ------------------------------------------------------------------------------------------
    # number of cubes
        # show current number of cubes per row/col
        # increase by 2
        # decrease by 2
    # Turn of higlighting?
    # Reset board
        Reset = Button(Screen, ScreenWidth - 150, 250, 100, 40, (255, 0, 0), (255, 255, 0))
        Reset.render(mouse)
        Reset.text(Fonts["ButtonFont"], Colors["black"], "Reset")
    # Get Hint
        Hint = Button(Screen, ScreenWidth - 150, 300, 100, 40, (255, 0, 0), (255, 255, 0))
        Hint.render(mouse)
        Hint.text(Fonts["ButtonFont"], Colors["black"], "Hint")
    # Check current (partial) board
        Check = Button(Screen, ScreenWidth - 150, 350, 100, 40, (255, 0, 0), (255, 255, 0))
        Check.render(mouse)
        Check.text(Fonts["ButtonFont"], Colors["black"], "Check")
    # Create new board
        New = Button(Screen, ScreenWidth - 150, 400, 100, 40, (255, 0, 0), (255, 255, 0))
        New.render(mouse)
        New.text(Fonts["ButtonFont"], Colors["black"], "New Board")
    # Navigation Buttons --> move nav buttons to this submenu
# BOARD ----------------------------------------------------------------------------------------------------
    # inititialize board class -----------------------------------------------------------------------------
        if not grid or New.functionality(mouse, click, True):
            # Set variables
            FirstIteration = True
            UpdatedBoard = None
            Solved = False
            # Initialize board
            grid = board(Screen, 10, (140, 100))
    # Print board (cubes & lines --> No values) ------------------------------------------------------------
        grid.DarwBoardBackground(Colors["black"])
        grid.DrawCubes((255, 255, 255))
        grid.HiglightLines(Colors["NavigationColor"], mouse)
    # Create new board -------------------------------------------------------------------------------------
        if FirstIteration:
            grid.CreateBoard()
            grid.Immutable()
    # Reset board ------------------------------------------------------------------------------------------
        if Reset.functionality(mouse, click, True):
            UpdatedBoard = []
            for line in grid.solvable:
                UpdatedBoard.append(line)
    # Allow board updates ----------------------------------------------------------------------------------
        Cube = grid.SelectCube(mouse, click, Cube)
        UpdatedBoard = grid.Updatecube(key, UpdatedBoard, Cube)
    # Print values -----------------------------------------------------------------------------------------
        grid.PrintBoard()
    # Check board ------------------------------------------------------------------------------------------
        if Check.functionality(mouse, click, True):
            if not grid.solution == grid.CurrentBoard:
                for row in range(grid.NumberOfCubes):
                    if not grid.solution[row] == grid.CurrentBoard[row]:
                        for char in range(grid.NumberOfCubes):
                            if grid.CurrentBoard[row][char] != '.' and grid.CurrentBoard[row][char] != grid.solution[row][char]:
                                grid.CurrentBoard[row] = UpdateBoard(grid.CurrentBoard, ('.', (row, char)))
        else:
            Solved = True
        if Solved:
            Message = CenteredText("Solved", Fonts["TitleFont"], (255, 0, 0,), ScreenWidth / 2, ScreenHeight / 2)
            Message.render(Screen)
# NAVIGATION BUTTONS ---------------------------------------------------------------------------------------
    # Menu button
        Menu = Button(Screen, ScreenWidth / 2 - 110, ScreenHeight - 75, 100, 40, Colors["NavigationColor"], Colors["NavigationHighlight"])
        Menu.render(mouse)
        Menu.text(Fonts["ButtonFont"], Colors["black"], "MENU")
        SelectedGame = Menu.functionality(mouse, click, ActivateGameLoop("Menu"))
        if SelectedGame: return SelectedGame
    # EXIT Button
        Exit = Button(Screen, ScreenWidth / 2 +10, ScreenHeight - 75, 100, 40, Colors["NavigationColor"], Colors["NavigationHighlight"])
        Exit.render(mouse)
        Exit.text(Fonts["ButtonFont"], Colors["black"], "QUIT")
        SelectedGame = Exit.functionality(mouse, click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)
# ITERATION COUNT ------------------------------------------------------------------------------------------
        FirstIteration = False
        key = None
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================