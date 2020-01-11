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
    menu = True
    # if button is selected
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
        # Puzzle Image
            PuzzleInfo.Image(Images + '\Sudoku.jpg', 115, 115)
            """
        # Puzzle info
            MultilineText("Fill a 9×9 grid.\nEach column, row and 3×3 grid should contain all digits from 1 to 9.", ButtonFont, black, (420, Submenu_Y + 180), 650, 250)
        # Play button
            Button("PLAY", (Submenu_X + 15, Submenu_Y + 270), 100, 40, Playbutton, PlayHighlight, mouse)
            if Submenu_X + 15 + 100 > mouse[0] > Submenu_X + 15 and Submenu_Y + 270 + 40 > mouse[1] > Submenu_Y + 270 and click[0] == 1:
                return ActivateGameLoop("SudokuPlay")

        # solve button
            Button("SOLVE", (Submenu_X + 135, Submenu_Y + 270), 100, 40, Playbutton, PlayHighlight, mouse)
            if Submenu_X + 135 + 100 > mouse[0] > Submenu_X + 135 and Submenu_Y + 270 + 40 > mouse[1] > Submenu_Y + 270 and click[0] == 1:
                return ActivateGameLoop("SudokuSolve")
            """
# [SUBMENU] PUZZLE INFO: BINAIRO ---------------------------------------------------------------------------
    # Submenu - Binairo info
        """
        if (Button_X + ButtonWidth > mouse[0] > Button_X and Button_Y + 50 + ButtonHeight > mouse[1] > Button_Y + 50) or Binairo:
            # Activate & decativate the correct info screen
            if click[0] == 1: Binairo = True
            Sudoku = False

            # Puzzle image
            image = pygame.image.load(Images + '\Binairo.png')
            Screen.blit(image, (Submenu_X + 65, Submenu_Y + 25))
            # Puzzle info
            MultilineText("Each column/ row needs to have te same ammount of 1 and 0.\nMax 2 times the same number next to eachother.\nNo identical rows/ columns alowed.", ButtonFont, black, (420, Submenu_Y + 150), 650, 250)
            # Play button
            Button("PLAY", (Submenu_X + 15, Submenu_Y + 270), 100, 40, Playbutton, PlayHighlight, mouse)
            if Submenu_X + 15 + 100 > mouse[0] > Submenu_X + 15 and Submenu_Y + 270 + 40 > mouse[1] > Submenu_Y + 270 and click[0] == 1:
                SelectedGame = ActivateGameLoop("BinairoPlay")
                return SelectedGame
            # solve button
            Button("SOLVE", (Submenu_X + 135, Submenu_Y + 270), 100, 40, Playbutton, PlayHighlight, mouse)
            if Submenu_X + 135 + 100 > mouse[0] > Submenu_X + 135 and Submenu_Y + 270 + 40 > mouse[1] > Submenu_Y + 270 and click[0] == 1:
                SelectedGame = ActivateGameLoop("BinairoSolve")
                return SelectedGame
        """
    # EXIT Button ------------------------------------------------------------------------------------------
        """
        Button("EXIT", (ScreenWidth / 2 - 50, ScreenHeight - 75), 100, 40, (255, 69, 0), (139, 0, 0), mouse)
        if ((ScreenWidth / 2 - 50) + 100 > mouse[0] > (ScreenWidth / 2 - 50) and (ScreenHeight - 75) + 40 > mouse[1] > (ScreenHeight - 75)):
            if click[0] == 1:
                #quitgame()
                return ActivateGameLoop("Quit")
        """
    # Update Display ---------------------------------------------------------------------------------------
        pygame.display.update()
    
    return ActivateGameLoop("Quit")
# ==========================================================================================================

# GAME LOOP: Sudoku ========================================================================================
def Sudoku_GameLoop():
    running = True

# IMPORT SUDOKU SCRIPTS ------------------------------------------------------------------------------------
    from Sudoku import board

# MAIN LOOP ------------------------------------------------------------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # Wheter or not to return to menu when leaving the sudoku window
        BackToMenu = False
    # Set background color
        Screen.fill((BackgroundColor))
    # Display title
        TextObject("Sudoku", TitleFont, black, int(ScreenWidth / 2), 50)
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
        Button("MENU", (ScreenWidth / 2 - 110, ScreenHeight - 75), 100, 40, NavigationColor, NavigationHighlight, mouse)
        if (ScreenWidth / 2 - 110) + 100 > mouse[0] > (ScreenWidth / 2 - 110) and (ScreenHeight - 75) + 40 > mouse[1] > (ScreenHeight - 75) and click[0] == 1:
            return ActivateGameLoop("Menu")
            # BackToMenu = True
            # running = False
    # EXIT Button 
        Button("EXIT", (ScreenWidth / 2 + 10, ScreenHeight - 75), 100, 40, NavigationColor, NavigationHighlight, mouse)
        if (ScreenWidth / 2 + 10) + 100 > mouse[0] > (ScreenWidth / 2 + 10) and (ScreenHeight - 75) + 40 > mouse[1] > (ScreenHeight - 75) and click[0] == 1:
            return ActivateGameLoop("Quit")

# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()

# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
    # if not BackToMenu:
    #     quitgame()    
# ==========================================================================================================

# GAME LOOP: Binairo =======================================================================================
def Binairo_GameLoop():
    running = True

# MAIN LOOP ------------------------------------------------------------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Wheter or not to return to menu when leaving the sudoku window
        BackToMenu = False
    # Set background color
        Screen.fill(BackgroundColor)
    # Display title
        TextObject("Binairo", TitleFont, black, int(ScreenWidth / 2), 50)
    # Get mouse position & track mouse-clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

# NAVIGATION BUTTONS ---------------------------------------------------------------------------------------
    # Menu button
        Button("MENU", (ScreenWidth / 2 - 110, ScreenHeight - 75), 100, 40, NavigationColor, NavigationHighlight, mouse)
        if (ScreenWidth / 2 - 110) + 100 > mouse[0] > (ScreenWidth / 2 - 110) and (ScreenHeight - 75) + 40 > mouse[1] > (ScreenHeight - 75) and click[0] == 1:
            BackToMenu = True
            running = False
    # EXIT Button 
        Button("EXIT", (ScreenWidth / 2 + 10, ScreenHeight - 75), 100, 40, NavigationColor, NavigationHighlight, mouse)
        if (ScreenWidth / 2 + 10) + 100 > mouse[0] > (ScreenWidth / 2 + 10) and (ScreenHeight - 75) + 40 > mouse[1] > (ScreenHeight - 75) and click[0] == 1:
            quitgame()

# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()

# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    if not BackToMenu:
        quitgame()    
# ==========================================================================================================

# Start game
SelectedGame = ActivateGameLoop("Menu")

while True:
    for game in SelectedGame:
        if game[0] == "Menu" and game[1] == True:
            SelectedGame = MainMenu()
            print(SelectedGame)
        elif game[0] == "SudokuPlay" and game[1] == True:
            SelectedGame = Sudoku_GameLoop()
        elif game[0] == "SudokuSolve" and game[1] == True:
            SelectedGame = Sudoku_GameLoop()
        elif game[0] == "BinairoPlay" and game[1] == True:
            Binairo_GameLoop()
        elif game[0] == "BinairoSolve" and game[1] == True:
            Binairo_GameLoop()
        elif game[0] == "Quit" and game[1] == True:
            quitgame()

#quitgame()

