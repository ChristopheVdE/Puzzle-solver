############################################################################################################
# NAME: Binairo: create
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Create playable boards
############################################################################################################

# IMPORT PACKAGES ==========================================================================================
import pygame
from Scripts.General.Classes import Button, CenteredText, Submenu
from Scripts.General.Functions import ActivateGameLoop, quitgame
from Scripts.Binairo.Functions import board
from Settings.Default import Colors, Fonts
# ==========================================================================================================

# GAME LOOP: Binairo =======================================================================================
def Binairo_GameLoop(ScreenWidth, ScreenHeight, clock, Images):
# VARIABLES ------------------------------------------------------------------------------------------------
    running = True
    grid = None
    NumberOfCubes = 10
# INITITIALIZE SCREEN --------------------------------------------------------------------------------------
    Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.DOUBLEBUF|pygame.HWSURFACE, 32)
# MAIN LOOP ------------------------------------------------------------------------------------------------
    while running:
        key = None
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
# MOUSE POSITION & CLICKS ----------------------------------------------------------------------------------
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
# SCREEN BACKGROUND ----------------------------------------------------------------------------------------
        Screen.fill(Colors["BackgroundColor"])
# OPTIONS SUBMENU ------------------------------------------------------------------------------------------
        Title = Submenu(Screen, ScreenWidth - 165, ScreenHeight / 2 - 150, 145, 300, Colors["black"], Colors["Background"])
        Title.Outline()
        Title.Title("Binairo", Fonts["Button"], Colors["black"])
# OPTIONS BUTTONS ------------------------------------------------------------------------------------------
    # Number of cubes per row/ Board size ------------------------------------------------------------------
        # Dispay number
        pygame.draw.rect(Screen, Colors["Options"], (ScreenWidth - 160, ScreenHeight/2 - 120, 40, 40))
        Cubes = CenteredText(str(NumberOfCubes), Fonts["Button"], Colors["black"], int(ScreenWidth - 160 + 20), ScreenHeight/2 - 120 + 40/2)
        Cubes.render(Screen)
        # Increase number
        Increase = Button(Screen, ScreenWidth - 120, ScreenHeight/2 - 120, 20, 20, Colors["Options"], Colors["OptionsHighlight"])
        Increase.render(mouse)
        Increase.image(Images + '\ArrowUp.png')
        NrCubes = Increase.functionality(mouse, click, int(NumberOfCubes + 2))
        if NrCubes and NrCubes in range(2, 16, 2):
            pygame.time.delay(150)
            NumberOfCubes = NrCubes
        # Decrease number
        Decrease = Button(Screen, ScreenWidth - 120, ScreenHeight/2 - 100, 20, 20, Colors["Options"], Colors["OptionsHighlight"])
        Decrease.render(mouse)
        Decrease.image(Images + '\ArrowDown.png')
        NrCubes = Decrease.functionality(mouse, click, int(NumberOfCubes - 2))
        if NrCubes and NrCubes in range(2, 16, 2):
            pygame.time.delay(150)
            NumberOfCubes = NrCubes
    # Create new board -------------------------------------------------------------------------------------
        New = Button(Screen, ScreenWidth - 95, ScreenHeight/2 - 120, 70, 40, Colors["Options"], Colors["OptionsHighlight"])
        New.render(mouse)
        New.text(Fonts["Button"], Colors["black"], "New")
    # Reset board ------------------------------------------------------------------------------------------
        Reset = Button(Screen, ScreenWidth - 160, ScreenHeight/2 - 70, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        Reset.render(mouse)
        Reset.text(Fonts["Button"], Colors["black"], "Reset")
    # Get Hint ---------------------------------------------------------------------------------------------
        Hint = Button(Screen, ScreenWidth - 160, ScreenHeight/2 - 20, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        Hint.render(mouse)
        Hint.text(Fonts["Button"], Colors["black"], "Hint")
    # Check current (partial) board ------------------------------------------------------------------------
        Check = Button(Screen, ScreenWidth - 160, ScreenHeight/2 + 30, 135, 40, Colors["Options"], Colors["OptionsHighlight"])
        Check.render(mouse)
        Check.text(Fonts["Button"], Colors["black"], "Check")
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
            grid = board(NumberOfCubes, (ScreenWidth, ScreenHeight))
            # Create empty board
            grid.CreateEmptyBoard()
            # BruteForce a solution
            grid.BruteForce()
            # Create a solvable boardstate for the solution
            grid.SolvableState()
            # Current board = solvable board
            grid.CurrentBoard()
            # Make the original values immutable
            grid.Immutable()
            # Print Background
            grid.CenterRectangle(ScreenWidth, ScreenHeight, 175, 0)
            # Slight delay (for smaller boards)
            pygame.time.delay(100)
    # Reset board ------------------------------------------------------------------------------------------
        elif Reset.functionality(mouse, click, True):
            grid.CurrentBoard() 
            grid.Immutable()
            # Slight delay (for smaller boards)
            pygame.time.delay(100)
    # Check Board ------------------------------------------------------------------------------------------
        elif Check.functionality(mouse, click, True):
            grid.Immutable()
            # Slight delay (for smaller boards)
            pygame.time.delay(100)
    # Get Hint ---------------------------------------------------------------------------------------------
        elif Hint.functionality(mouse, click, True):
            grid.Hint()
            grid.Immutable()
            # Slight delay
            pygame.time.delay(200)
    # Row/col higlighting ----------------------------------------------------------------------------------
        grid.BoardBackground(Colors["black"])
        grid.DrawCubes(Colors["Cube"], Colors["Correct"])
        grid.HiglightLines(Colors["Navigation"], mouse)
    # Allow board updates ----------------------------------------------------------------------------------
        grid.SelectCube(mouse, click)       
        grid.Pencil(key)
        grid.Updatecube(key)
    # Print values -----------------------------------------------------------------------------------------
        grid.PrintBoard(Screen)
        grid.CheckBoard(Screen, Fonts["Message"], Colors["Message"])
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================