############################################################################################################
# NAME: Main Menu
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Main Menu for the Pygame apllication
# USAGE python MainMenu.py
############################################################################################################

# PACKAGES =================================================================================================
import os
import pygame
from Menu import Button, CenteredText, MultiLineText, Submenu
import time
# ==========================================================================================================

# FUNCTIONS ================================================================================================
# Quit the game --------------------------------------------------------------------------------------------
def quitgame():
    pygame.quit()
    quit()
# Activate correct gameloop --------------------------------------------------------------------------------
def ActivateGameLoop(gametype):
    gameloop = []
    for game in ["Menu", "Quit", "SudokuPlay", "SudokuSolve", "BinairoPlay", "BinairoSolve"]:
        if game == gametype:
            gameloop.append((game, True))
        else:
            gameloop.append((game, False))
    return gameloop
# ==========================================================================================================

# GENERAL INFO =============================================================================================
# Image folder ---------------------------------------------------------------------------------------------
Images = os.path.dirname(os.path.realpath(__file__)) + '\Images'

# Colors ---------------------------------------------------------------------------------------------------
black               = (0, 0, 0)
BackgroundColor     = (220,220,220)     #grey (grainsboro)
ButtonColor         = (192, 192, 192)   #grey (silver)
HighlightColor      = (135,206,235)     #skyblue
Playbutton          = (0,255,127)       #springgreen 
PlayHighlight       = (50, 205, 50)     #limegreen
NavigationColor     = (255,69,0)
NavigationHighlight = (139,0,0)

# Initialize game ------------------------------------------------------------------------------------------
pygame.init()

# Display size ---------------------------------------------------------------------------------------------
ScreenWidth = 800
ScreenHeight = 600
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.DOUBLEBUF, 32)

# Caption & logo -------------------------------------------------------------------------------------------
pygame.display.set_caption('Puzzle solver')
icon = pygame.image.load(Images + '\logo.png')
pygame.display.set_icon(icon)

# Fonts -----------------------------------------------------------------------------------------------------
TitleFont = pygame.font.Font('freesansbold.ttf', 60)
ButtonFont = pygame.font.Font('freesansbold.ttf', 15)
# ===========================================================================================================

# MAIN MENU =================================================================================================
def MainMenu():
    time.sleep(0.1)
    menu = True
    # if button was Pressed
    SudokuSelected = False
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
        Screen.fill(BackgroundColor)
    # Title
        MenuTitle = CenteredText("Puzzle Solver", TitleFont, black, ScreenWidth/2, ScreenHeight/7)
        MenuTitle.render(Screen)
# [SUBMENU] CHOOSE PUZZLE ----------------------------------------------------------------------------------
    # Title
        PuzzleType = Submenu(Screen, 140, ScreenHeight/7 + 70, 250, 325, black, BackgroundColor)
        PuzzleType.Outline()
        PuzzleType.Title("CHOOSE PUZZLE", ButtonFont, black)
    # Select Sudoku button
        Sudoku = Button(Screen, 155, ScreenHeight / 7 + 95, 218, 40, ButtonColor, HighlightColor, SudokuSelected)
        Sudoku.render(mouse)
        Sudoku.text(ButtonFont, black, "Sudoku")
    # Select Binairo button
        Binairo = Button(Screen, 155, ScreenHeight / 7 + 145, 218, 40, ButtonColor, HighlightColor, BinairoSelected)
        Binairo.render(mouse)
        Binairo.text(ButtonFont, black, "Binairo")        
# [SUBMENU] PUZZLE INFO ------------------------------------------------------------------------------------
    # GENERAL ----------------------------------------------------------------------------------------------
        PuzzleInfo = Submenu(Screen, 140 + 270, ScreenHeight/7 + 70, 250, 325, black, BackgroundColor)
        PuzzleInfo.Outline()
        PuzzleInfo.Title("PUZZLE INFO", ButtonFont, black)
    # PUZZLE INFO: SUDOKU ----------------------------------------------------------------------------------
        # Sudoku button activation
        if (Sudoku.X + Sudoku.Width > mouse[0] > Sudoku.X and Sudoku.Y + Sudoku.Height > mouse[1] > Sudoku.Y) or SudokuSelected:
            if click[0] == 1:
                SudokuSelected = True
            BinairoSelected = False
        # Puzzle image & text
            PuzzleInfo.Image(Images + '\Sudoku.jpg')
            PuzzleInfo.MultiLineText("Fill a 9×9 grid.\nEach column, row and 3×3 grid should contain all digits from 1 to 9.", ButtonFont, black)
        # Play button
            Play = Button(Screen, PuzzleInfo.X + 15, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Playbutton, PlayHighlight)
            Play.render(mouse)
            Play.text(ButtonFont, black, "PLAY")
            SelectedGame = Play.functionality(mouse, click, ActivateGameLoop("SudokuPlay"))
            if SelectedGame: return SelectedGame
        # Solve button
            Solve = Button(Screen, PuzzleInfo.X + 135, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Playbutton, PlayHighlight)
            Solve.render(mouse)
            Solve.text(ButtonFont, black, "SOLVE")
            SelectedGame = Solve.functionality(mouse, click, ActivateGameLoop("SudokuSolve"))
            if SelectedGame: return SelectedGame
    # PUZZLE INFO: BINAIRO ---------------------------------------------------------------------------------
        # Sudoku button activation
        if (Binairo.X + Binairo.Width > mouse[0] > Binairo.X and Binairo.Y + Binairo.Height > mouse[1] > Binairo.Y) or BinairoSelected:
            if click[0] == 1:
                BinairoSelected = True
            SudokuSelected = False
        # Puzzle image & text
            PuzzleInfo.Image(Images + '\Binairo.png')
            PuzzleInfo.MultiLineText("Each column/ row needs to have te same ammount of 1 and 0.\nMax 2 times the same number next to eachother.\nNo identical rows/ columns alowed.", ButtonFont, black)
        # Play button
            Play = Button(Screen, PuzzleInfo.X + 15, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Playbutton, PlayHighlight)
            Play.render(mouse)
            Play.text(ButtonFont, black, "PLAY")
            SelectedGame = Play.functionality(mouse, click, ActivateGameLoop("BinairoPlay"))
            if SelectedGame: return SelectedGame
        # Solve button
            Solve = Button(Screen, PuzzleInfo.X + 135, PuzzleInfo.Y + PuzzleInfo.Height - 50, 100, 40, Playbutton, PlayHighlight)
            Solve.render(mouse)
            Solve.text(ButtonFont, black, "SOLVE")
            SelectedGame = Solve.functionality(mouse, click, ActivateGameLoop("BinairoSolve"))
            if SelectedGame: return SelectedGame
# EXIT BUTTON ----------------------------------------------------------------------------------------------
        Exit = Button(Screen, ScreenWidth/2 - 50, ScreenHeight - 75, 100, 40, NavigationColor, NavigationHighlight)
        Exit.render(mouse)
        Exit.text(ButtonFont, black, "EXIT")
        SelectedGame = Exit.functionality(mouse, click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
    
    return ActivateGameLoop("Quit")
# ==========================================================================================================

# GAME LOOP: Sudoku ========================================================================================
def Sudoku_GameLoop():
# IMPORT SUDOKU SCRIPTS ------------------------------------------------------------------------------------
    from Sudoku import board
# MAIN LOOP ------------------------------------------------------------------------------------------------
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # Set background color
        Screen.fill((BackgroundColor))
    # Display title
        Title = CenteredText("Sudoku", TitleFont, black, int(ScreenWidth / 2), 50)
        Title.render(Screen)
    # Get mouse position & track mouse-clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
# BOARD ----------------------------------------------------------------------------------------------------
        grid = board(Screen, 9, (140,100))
        grid.DarwBoardBackground(black)
        grid.DrawCubes((255, 255, 255))
        grid.HiglightLines(NavigationColor, mouse)     
# NAVIGATION BUTTONS ---------------------------------------------------------------------------------------
    # Menu button
        Menu = Button(Screen, ScreenWidth / 2 - 110, ScreenHeight - 75, 100, 40, NavigationColor, NavigationHighlight)
        Menu.render(mouse)
        Menu.text(ButtonFont, black, "MENU")
        SelectedGame = Menu.functionality(mouse, click, ActivateGameLoop("Menu"))
        if SelectedGame: return SelectedGame
    # EXIT Button
        Exit = Button(Screen, ScreenWidth / 2 +10, ScreenHeight - 75, 100, 40, NavigationColor, NavigationHighlight)
        Exit.render(mouse)
        Exit.text(ButtonFont, black, "QUIT")
        SelectedGame = Menu.functionality(mouse, click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================

# GAME LOOP: Binairo =======================================================================================
def Binairo_GameLoop():
# IMPORT SUDOKU SCRIPTS ------------------------------------------------------------------------------------
# MAIN LOOP ------------------------------------------------------------------------------------------------
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Wheter or not to return to menu when leaving the sudoku window
        BackToMenu = False
    # Set background color
        Screen.fill(BackgroundColor)
    # Display title
        Title = CenteredText("Binairo", TitleFont, black, int(ScreenWidth / 2), 50)
        Title.render(Screen)
    # Get mouse position & track mouse-clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
# BOARD ----------------------------------------------------------------------------------------------------
# NAVIGATION BUTTONS ---------------------------------------------------------------------------------------
    # Menu button
        Menu = Button(Screen, ScreenWidth / 2 - 110, ScreenHeight - 75, 100, 40, NavigationColor, NavigationHighlight)
        Menu.render(mouse)
        Menu.text(ButtonFont, black, "MENU")
        SelectedGame = Menu.functionality(mouse, click, ActivateGameLoop("Menu"))
        if SelectedGame: return SelectedGame
    # EXIT Button
        Exit = Button(Screen, ScreenWidth / 2 +10, ScreenHeight - 75, 100, 40, NavigationColor, NavigationHighlight)
        Exit.render(mouse)
        Exit.text(ButtonFont, black, "QUIT")
        SelectedGame = Menu.functionality(mouse, click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================

# MAIN GAME LOOP ===========================================================================================
# Set Start-screen to Menu ---------------------------------------------------------------------------------
SelectedGame = ActivateGameLoop("Menu")
# MAIN LOOP ------------------------------------------------------------------------------------------------
while True:
    for game in SelectedGame:
        if game[0] == "Menu" and game[1] == True:
            SelectedGame = MainMenu()
        elif game[0] == "SudokuPlay" and game[1] == True:
            SelectedGame = Sudoku_GameLoop()
        elif game[0] == "SudokuSolve" and game[1] == True:
            SelectedGame = Sudoku_GameLoop()
        elif game[0] == "BinairoPlay" and game[1] == True:
            SelectedGame = Binairo_GameLoop()
        elif game[0] == "BinairoSolve" and game[1] == True:
            SelectedGame = Binairo_GameLoop()
        elif game[0] == "Quit" and game[1] == True:
            quitgame()
# ==========================================================================================================

