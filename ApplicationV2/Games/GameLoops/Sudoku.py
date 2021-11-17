############################################################################################################
# NAME: Sudoku: create
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Create playable boards
############################################################################################################

# IMPORT PACKAGES ==========================================================================================
import copy
import pygame
# -- Display -----------------------------------------------------------------------------------------------
from Display.Game.GameScreen import GameScreen
# -- Functions ---------------------------------------------------------------------------------------------
from Games.Functions.ActivateGameLoop import ActivateGameLoop
from Games.Functions.GetPressedKey import GetPressedKey
from Games.Functions.Sudoku.BruteForce import BruteForce
from Games.Functions.Sudoku.CreateSolvableState import SolvableState
from Games.Functions.GetHint import GetHint
from Games.Functions.CheckAgaintSolution import CheckAgainstSolution
# -- Classes -----------------------------------------------------------------------------------------------
from Games.Classes.Board import Board
# -- Settings ----------------------------------------------------------------------------------------------
from Settings.Default import Colors, Fonts
# ==========================================================================================================

# GAME LOOP: Sudoku ========================================================================================
def Sudoku_GameLoop(clock):
# VARIABLES ------------------------------------------------------------------------------------------------
    running = True
    Solution = None
    StartBoard = None
    Game = None
# INITITIALIZE SCREEN --------------------------------------------------------------------------------------
    Screen = GameScreen()
# MAIN LOOP ------------------------------------------------------------------------------------------------
    while running:
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                key = GetPressedKey(event)
# MOUSE POSITION & CLICKS ----------------------------------------------------------------------------------
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
# OPTIONS SUBMENU ------------------------------------------------------------------------------------------
        Screen.RenderOptionsMenu()
        Screen.Options.MenuOutline()
    # Options ----------------------------------------------------------------------------------------------
        Screen.Options.OptionButtons(mouse)
    # Navigation -------------------------------------------------------------------------------------------
        SelectedGame = Screen.Options.NavigationButtons(mouse, click)
        if SelectedGame: return SelectedGame
# BOARD ----------------------------------------------------------------------------------------------------
    # Initiate board ---------------------------------------------------------------------------------------
        if not Screen.Board or not Game or Screen.Options.New.functionality(mouse, click, True):
            # Create board
            Solution = Board(9,9)
            Solution.CreateEmptyBoard()
            BruteForce(Solution)
            StartBoard = SolvableState(Solution)
            Game = copy.deepcopy(StartBoard)
            # Start render
            pygame.display.update()
            Screen.RenderGameBoard(9, 9 ,40, 1)
            Screen.RenderValueSummary()
            Screen.Board.CalcBoardSize('Sudoku')
            Screen.Board.CalcBoardCenter()
    # Reset Board ------------------------------------------------------------------------------------------
        elif Screen.Options.Reset.functionality(mouse, click, True):
            Game = copy.deepcopy(StartBoard)
    # Hint -------------------------------------------------------------------------------------------------
        elif Screen.Options.Hint.functionality(mouse, click, True):
            Game = GetHint(Game, 'Sudoku')
    # Check Board ------------------------------------------------------------------------------------------
        elif Screen.Options.Check.functionality(mouse, click, True):
            Game = CheckAgainstSolution(Game, Solution)
    # Render board -----------------------------------------------------------------------------------------
        Screen.Board.BoardBackground()
        Screen.Board.DrawCubes(Game, Colors['Cube'], Colors['Correct'])
        Screen.Board.RenderValues(Game, 'User')
        Screen.Board.HiglightLines(Colors["Navigation"], mouse)
        Screen.Board.Rendersurface()
    # Update Value -----------------------------------------------------------------------------------------




# # BOARD --------------------------------------------------------------------------------------------------
#     # Create new Board -----------------------------------------------------------------------------------
#         if not grid or New.functionality(mouse, click, True):
#             # Display update
#             pygame.display.update()
#             # Initialize board
#             grid = Board((ScreenWidth, ScreenHeight))
#             # Create empty board
#             grid.CreateEmptyBoard()
#             # BruteForce a solution
#             grid.BruteForce()
#             # Create a solvable boardstate for the solution
#             grid.SolvableState()
#             # Current board = solvable board
#             grid.CurrentBoard()
#             # Make the original values immutable
#             grid.Immutable()
#             # Print Background
#             grid.CenterRectangle(ScreenWidth, ScreenHeight, 175, 0)
#             # Slight delay (for smaller boards)
#             pygame.time.delay(100)        
#     # Reset board ------------------------------------------------------------------------------------------
#         elif Reset.functionality(mouse, click, True):
#             grid.CurrentBoard() 
#             grid.Immutable()
#             # Slight delay (for smaller boards)
#             pygame.time.delay(100)
#     # Check Board ------------------------------------------------------------------------------------------
#         elif Check.functionality(mouse, click, True):
#             grid.Immutable()
#             # Slight delay (for smaller boards)
#             pygame.time.delay(100)
#     # Get Hint ---------------------------------------------------------------------------------------------
#         elif Hint.functionality(mouse, click, True):
#             grid.Hint()
#             grid.Immutable()
#             # Slight delay
#             pygame.time.delay(200)
#     # Row/col higlighting ----------------------------------------------------------------------------------
#         grid.BoardBackground(Colors["black"])
#         grid.DrawCubes(Colors["Cube"], (220,220,220))
#         grid.HiglightLines(Colors["Navigation"], mouse)
#     # Allow board updates ----------------------------------------------------------------------------------
#         grid.SelectCube(mouse, click)       
#         grid.Pencil(key)
#         grid.Updatecube(key)
#     # Print values -----------------------------------------------------------------------------------------
#         grid.PrintBoard(Screen)
#         grid.CheckBoard(Screen, Fonts["Message"], Colors["Message"])
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================