############################################################################################################
# NAME: Binairo: create
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Create playable boards
############################################################################################################

# IMPORT PACKAGES ==========================================================================================
import random
import pygame
from Scripts.General.Classes import Button, CenteredText
from Scripts.General.Functions import ActivateGameLoop, quitgame
from Scripts.Binairo.Functions import board, UpdateBoard, CountEmpty
from Settings.Colors import Colors
from Settings.Fonts import Fonts
# ==========================================================================================================

# GAME LOOP: Binairo =======================================================================================
def Binairo_GameLoop(Screen, ScreenWidth, ScreenHeight, clock, Images):
# VARIABLES ------------------------------------------------------------------------------------------------
    running = True
    key = None
    grid = None
    Cube = None
    CreatedBoard = None
    NumberOfCubes = 10
# MAIN LOOP ------------------------------------------------------------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    key = '0'
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = '1'
                if event.key == pygame.K_DELETE or event.key == pygame.K_KP_PERIOD:
                    key = '.'
# SCREEN & CAPTION -----------------------------------------------------------------------------------------
    # Set background color
        Screen.fill(Colors["BackgroundColor"])
    # Display title
        Title = CenteredText("Binairo", Fonts["TitleFont"], Colors["black"], int(ScreenWidth / 2), 50)
        Title.render(Screen)
    # Get mouse position & track mouse-clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
# SETTINGS BUTTONS -----------------------------------------------------------------------------------------
    # Number of cubes per row/ Board size ------------------------------------------------------------------
        # Dispay number
        pygame.draw.rect(Screen, (255, 0, 0), (ScreenWidth - 160, 200, 40, 40))
        Cubes = CenteredText(str(NumberOfCubes), Fonts["ButtonFont"], Colors["black"], int(ScreenWidth - 160 + 20), 200 + 40/2)
        Cubes.render(Screen)
        # Increase number
        Increase = Button(Screen, ScreenWidth - 120, 200, 20, 20, (255, 0, 0), (255, 255, 0))
        Increase.render(mouse)
        Increase.image(Images + '\ArrowUp.png')
        NrCubes = Increase.functionality(mouse, click, int(NumberOfCubes + 2))
        if NrCubes and NrCubes in range(2, 14, 2):
            pygame.time.delay(150)
            NumberOfCubes = NrCubes
        # Decrease number
        Decrease = Button(Screen, ScreenWidth - 120, 220, 20, 20, (255, 0, 0), (255, 255, 0))
        Decrease.render(mouse)
        Decrease.image(Images + '\ArrowDown.png')
        NrCubes = Decrease.functionality(mouse, click, int(NumberOfCubes - 2))
        if NrCubes and NrCubes in range(2, 14, 2):
            pygame.time.delay(150)
            NumberOfCubes = NrCubes
    # Create new board -------------------------------------------------------------------------------------
        New = Button(Screen, ScreenWidth - 95, 200, 70, 40, (255, 0, 0), (255, 255, 0))
        New.render(mouse)
        New.text(Fonts["ButtonFont"], Colors["black"], "New")
    # Reset board ------------------------------------------------------------------------------------------
        Reset = Button(Screen, ScreenWidth - 160, 250, 135, 40, (255, 0, 0), (255, 255, 0))
        Reset.render(mouse)
        Reset.text(Fonts["ButtonFont"], Colors["black"], "Reset")
    # Get Hint ---------------------------------------------------------------------------------------------
        Hint = Button(Screen, ScreenWidth - 160, 300, 135, 40, (255, 0, 0), (255, 255, 0))
        Hint.render(mouse)
        Hint.text(Fonts["ButtonFont"], Colors["black"], "Hint")
    # Check current (partial) board ------------------------------------------------------------------------
        Check = Button(Screen, ScreenWidth - 160, 350, 135, 40, (255, 0, 0), (255, 255, 0))
        Check.render(mouse)
        Check.text(Fonts["ButtonFont"], Colors["black"], "Check")
# NAVIGATION BUTTONS ---------------------------------------------------------------------------------------
    # Menu button ------------------------------------------------------------------------------------------
        Menu = Button(Screen, ScreenWidth - 160, 410, 65, 40, Colors["NavigationColor"], Colors["NavigationHighlight"])
        Menu.render(mouse)
        Menu.text(Fonts["ButtonFont"], Colors["black"], "MENU")
        SelectedGame = Menu.functionality(mouse, click, ActivateGameLoop("Menu"))
        if SelectedGame: return SelectedGame
    # Exit Button ------------------------------------------------------------------------------------------
        Exit = Button(Screen, ScreenWidth - 90, 410, 65, 40, Colors["NavigationColor"], Colors["NavigationHighlight"])
        Exit.render(mouse)
        Exit.text(Fonts["ButtonFont"], Colors["black"], "QUIT")
        SelectedGame = Exit.functionality(mouse, click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# UPDATE DISPLAY: SCREEN & SETTINGS (NOT BOARD) ------------------------------------------------------------
        if not grid:
            pygame.display.update()
# BOARD ----------------------------------------------------------------------------------------------------
    # inititialize board class -----------------------------------------------------------------------------
        if not grid or New.functionality(mouse, click, True):
            # Set variables
            FirstIteration = True
            UpdatedBoard = None
            Solved = False        
            # Initialize board
            grid = board(Screen, NumberOfCubes, (140, 100))
            pygame.time.delay(100)
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
    # Give hint --------------------------------------------------------------------------------------------
        if Hint.functionality(mouse, click, True):
            Coords = []
            for row in range(grid.NumberOfCubes):
                for char in range(grid.NumberOfCubes):
                    if grid.CurrentBoard[row][char] == '.':
                        Coords.append((row, char))
            if len(Coords) != 0:
                tip = random.choice(Coords)
                grid.CurrentBoard[tip[0]] = UpdateBoard(grid.CurrentBoard, (grid.solution[tip[0]][tip[1]], tip))
            pygame.time.delay(200)
    # Allow board updates ----------------------------------------------------------------------------------
        Cube = grid.SelectCube(mouse, click, Cube)
        UpdatedBoard = grid.Updatecube(key, UpdatedBoard, Cube)
    # Print values -----------------------------------------------------------------------------------------
        grid.PrintBoard()
    # Check board ------------------------------------------------------------------------------------------
        if Check.functionality(mouse, click, True) or CountEmpty(grid.CurrentBoard) == 0:
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
# UPDATE DISPLAY: BOARD ------------------------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)
# RESET VARIABLES ------------------------------------------------------------------------------------------
        FirstIteration = False
        key = None
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================