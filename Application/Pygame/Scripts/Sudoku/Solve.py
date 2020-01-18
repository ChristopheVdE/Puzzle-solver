############################################################################################################
# NAME: Sudoku: create
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Create playable boards
############################################################################################################

# IMPORT PACKAGES ==========================================================================================
import pygame
from Scripts.General.Classes import Button, CenteredText
from Scripts.General.Functions import ActivateGameLoop, quitgame
from Scripts.Sudoku.Functions import board
from Settings.Colors import Colors
from Settings.Fonts import Fonts
# ==========================================================================================================

# GAME LOOP: Sudoku ========================================================================================
def Sudoku_GameLoop(ScreenWidth, ScreenHeight, clock):
# INITITIALIZE SCREEN --------------------------------------------------------------------------------------
    Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.DOUBLEBUF, 32)
# VARIABLES ------------------------------------------------------------------------------------------------
    running = True
# MAIN LOOP ------------------------------------------------------------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    # Set background color
        Screen.fill((Colors["BackgroundColor"]))
    # Display title
        Title = CenteredText("Sudoku", Fonts["TitleFont"], Colors["black"], int(ScreenWidth / 2), 50)
        Title.render(Screen)
    # Get mouse position & track mouse-clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
# BOARD ----------------------------------------------------------------------------------------------------
        grid = board(Screen, 9, (140,100))
        grid.DarwBoardBackground(Colors["black"])
        grid.DrawCubes((255, 255, 255))
        grid.HiglightLines(Colors["NavigationColor"], mouse)     
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
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================