############################################################################################################
# NAME: Main Menu
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Main Menu for the Pygame apllication
# USAGE python MainMenu.py
############################################################################################################

# PACKAGES =================================================================================================
import os
import sys
import pygame
from Settings.Default import ScreenSize
# ==========================================================================================================

# MAIN GAME LOOP ===========================================================================================
def mainloop(SelectedGame, ScreenWidth, ScreenHeight, clock, Images):
    while True:
        for game in SelectedGame:
            if game[0] == "Menu" and game[1] == True:
                from Games.GameLoops.MainMenu import MainMenu as GameLoop
                pygame.time.delay(100)
                SelectedGame = GameLoop(ScreenSize['width'], ScreenSize['height'], clock, Images)
            elif game[0] == "SudokuPlay" and game[1] == True:
                from Games.GameLoops.Sudoku import Sudoku_GameLoop as GameLoop
                SelectedGame = GameLoop(clock)
            # elif game[0] == "SudokuSolve" and game[1] == True:
            #     from Scripts.Sudoku.Solve import Sudoku_GameLoop as GameLoop
            #     SelectedGame = GameLoop(ScreenSize['width'], ScreenSize['height'], clock)
            # elif game[0] == "HudokuPlay" and game[1] == True:
            #     from Scripts.Hudoku.Create import Hudoku_GameLoop as GameLoop
            #     SelectedGame = GameLoop(ScreenSize['width'], ScreenSize['height'], clock)
            # elif game[0] == "HudokuSolve" and game[1] == True:
            #     from Scripts.Hudoku.Solve import Hudoku_GameLoop as GameLoop
            #     SelectedGame = GameLoop(ScreenSize['width'], ScreenSize['height'], clock)
            # elif game[0] == "BinairoPlay" and game[1] == True:
            #     from Scripts.Binairo.Create import Binairo_GameLoop as GameLoop
            #     SelectedGame = GameLoop(ScreenSize['width'], ScreenSize['height'], clock, Images)
            # elif game[0] == "BinairoSolve" and game[1] == True:
            #     from Scripts.Binairo.Solve import Binairo_GameLoop as GameLoop
            #     SelectedGame = GameLoop(ScreenSize['width'], ScreenSize['height'], clock, Images)
            elif game[0] == "Quit" and game[1] == True:
                pygame.quit()
                sys.exit()
# ==========================================================================================================

# GENERAL INFO =============================================================================================
def main():
# Initialize game ------------------------------------------------------------------------------------------
    pygame.init()

# Caption --------------------------------------------------------------------------------------------------
    pygame.display.set_caption('Puzzle solver')

# Logo -----------------------------------------------------------------------------------------------------
    Images = os.path.dirname(os.path.realpath(__file__)) + '\Display\Images'
    icon = pygame.image.load(Images + '\logo.png')
    pygame.display.set_icon(icon)

# Clock ----------------------------------------------------------------------------------------------------
    clock = pygame.time.Clock()

# Set Start-screen to Menu ---------------------------------------------------------------------------------
    SelectedGame = [("Menu", True)]

# Start main loop ------------------------------------------------------------------------------------------
    mainloop(SelectedGame, ScreenSize['width'], ScreenSize['height'], clock, Images)
# ==========================================================================================================

# Start Script =============================================================================================
if __name__ == '__main__':
    main()
# ==========================================================================================================