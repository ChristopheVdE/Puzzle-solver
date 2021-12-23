############################################################################################################
# NAME: Sudoku: Solve
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Solve player made sudoku
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
from Games.Functions.GetHint import GetHint
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
    Status = ''
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
        Screen.Options.OptionButtons(mouse, 'Solve')
    # Navigation -------------------------------------------------------------------------------------------
        SelectedGame = Screen.Options.NavigationButtons(mouse, click)
        if SelectedGame: return SelectedGame
# BOARD ----------------------------------------------------------------------------------------------------
    # Initiate board ---------------------------------------------------------------------------------------
        if not Screen.Board or not Game or Screen.Options.New.functionality(mouse, click, True):
            Status =''
            # Create board
            Game = Board(9,9)
            Game.CreateEmptyBoard()
            Empty = Game.FindEmpty()
            # Delete StartBoard
            StartBoard = None
            # Start render
            pygame.display.update()
            Screen.RenderGameBoard(9, 9 ,40, 1)
            Screen.RenderValueSummary()             # not active yet
            Screen.Board.CalcBoardSize('Sudoku')
            Screen.Board.CalcBoardCenter()
    # Reset Board ------------------------------------------------------------------------------------------
        elif Screen.Options.Reset.functionality(mouse, click, True):
            if StartBoard: 
                Game = copy.deepcopy(StartBoard)
                Status = ''
    # Hint -------------------------------------------------------------------------------------------------
        elif Status != 'Solving' and Screen.Options.Hint.functionality(mouse, click, True):
            if not StartBoard: 
                Game.SetPlayerValuesCorrect()
                StartBoard = copy.deepcopy(Game)
            Empty = Game.FindEmpty()
            Game = GetHint(Game, 'Sudoku')
    # Solve Board ------------------------------------------------------------------------------------------
        elif Status == 'Solving' or Screen.Options.Solve.functionality(mouse, click, True):
            if Status != 'Solving': Status = 'Solving'
            if not StartBoard: 
                Game.SetPlayerValuesCorrect()
                StartBoard = copy.deepcopy(Game)
            Empty = Game.FindEmpty()
            Game = GetHint(Game, 'Sudoku')
    # Render board -----------------------------------------------------------------------------------------
        Screen.Board.BoardBackground()
        Screen.Board.DrawCubes(Game, Colors['Cube'], Colors['Correct'])
        if StartBoard:
            Screen.Board.RenderValues(Game, 'System')
        else:
            Screen.Board.RenderValues(Game, 'User')
        if Status != 'Solved': Screen.Board.HiglightLines(Colors["Navigation"], mouse)   
    # Update Value -----------------------------------------------------------------------------------------
        if not StartBoard:
            SelectedCube = Screen.Board.GetSelectedCube(mouse, click, SelectedCube)
            if SelectedCube:
                if key:
                    ClickType = SelectedCube[0]
                    Position = SelectedCube[1]
                    if ClickType == 'L':
                        Game.GetRow(Position[0])[Position[1]].UpdateValue(key, Game, Position)
                    key = None
            else:
                key = None
    # Check Board Solved -----------------------------------------------------------------------------------
        if Status == 'Solved' and StartBoard:
            Screen.RenderMessageSolved(Game)   
        elif Status != 'Solved' and StartBoard:
            if len(Empty)==0:
                Status == 'Solved'
                Screen.RenderMessageSolved(Game)
            elif Empty == Game.FindEmpty():
                Status = 'Solved'
                Screen.RenderMessageSolved(Game)
        Screen.Board.Rendersurface()
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================