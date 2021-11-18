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
from Settings.Default import Colors
# ==========================================================================================================

# GAME LOOP: Sudoku ========================================================================================
def Sudoku_GameLoop(clock):
# VARIABLES ------------------------------------------------------------------------------------------------
    running = True
    Solution = None
    StartBoard = None
    Game = None
    key = None
    SelectedCube = None
# INITITIALIZE SCREEN --------------------------------------------------------------------------------------
    Screen = GameScreen()
# MAIN LOOP ------------------------------------------------------------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                key = GetPressedKey(event)
                break
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
        SelectedCube = Screen.Board.GetSelectedCube(mouse, click, SelectedCube)
        if SelectedCube and key:
            ClickType = SelectedCube[0]
            Position = SelectedCube[1]
            if ClickType == 'L':
                Game.GetRow(Position[0])[Position[1]].UpdateValue(key, Game, Position)
            elif ClickType == 'R' and key !=0:
                Game.GetRow(Position[0])[Position[1]].UpdatePencil(key)
            key = None
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================