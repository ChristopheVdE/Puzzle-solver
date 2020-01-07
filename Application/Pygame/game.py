############################################################################################################
# NAME: BINAIRO Creator
# AUTHOR: Christophe Van den Eynde
# FUNCTION: creates a random solvable Binairo-type puzzle
# USAGE python binairo_creator.py
############################################################################################################

# PACKAGES =================================================================================================
import os
import pygame
# ==========================================================================================================

# GENERAL INFO =============================================================================================
# Image folder ---------------------------------------------------------------------------------------------
Images = os.path.dirname(os.path.realpath(__file__)) + '\Images'

# colors ---------------------------------------------------------------------------------------------------
black = (0,0,0)
ButtonColor = (192, 192, 192)
HighlightColor = (135, 135, 135)

# Initialize game ------------------------------------------------------------------------------------------
pygame.init()

# Display size & background --------------------------------------------------------------------------------
ScreenWidth = 800
ScreenHeight = 600
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
backgroundcolor = (220,220,220) #gray (grainsboro)

# Caption & logo -------------------------------------------------------------------------------------------
pygame.display.set_caption('Puzzle solver')
icon = pygame.image.load(Images + '\main.png')
pygame.display.set_icon(icon)

# Fonts ----------------------------------------------------------------------------------------------------
TitleFont = pygame.font.Font('freesansbold.ttf', 60)
ButtonFont = pygame.font.Font('freesansbold.ttf', 15)
# ==========================================================================================================

# FUNCTIONS ================================================================================================
# Text area (for renderign) --------------------------------------------------------------------------------
def TextObject(Text, Font, Color, X, Y):
    Text = Font.render(Text, True, Color)
    TextArea = Text.get_rect()
    TextArea.center  = (int(X), int(Y))
    Screen.blit(Text, TextArea)

# Create INteractive buttons -------------------------------------------------------------------------------
def Button(Text, TopLeft, ButtonWidth, ButtonHeight, NormalColor, HighlightColor, Action = None):
    # Get mouse position & track mouse-clicks
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Draw Button & Highlight button if slected & Perform action if pressed
    if TopLeft[0] + ButtonWidth > mouse[0] > TopLeft[0] and TopLeft[1] + ButtonHeight > mouse[1] > TopLeft[1]:
        pygame.draw.rect(Screen, HighlightColor, (int(TopLeft[0]), int(TopLeft[1]), ButtonWidth, ButtonHeight))
        if click[0] == 1 and Action != None:
            Action()
    else:
        pygame.draw.rect(Screen, NormalColor, (int(TopLeft[0]), int(TopLeft[1]), ButtonWidth, ButtonHeight))

    # Add Text to Button
    TextObject(Text, ButtonFont, black, TopLeft[0] + (ButtonWidth / 2), TopLeft[1] + (ButtonHeight / 2))

# Quit the game ---------------------------------------------------------------------------------------------
def quitgame():
    pygame.quit()
    quit()
# ===========================================================================================================


# MAIN MENU =================================================================================================
def MainMenu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
        # Set background color
        Screen.fill(backgroundcolor)
        # Display title
        TextObject("Puzzle Solver", TitleFont, black, ScreenWidth / 2, ScreenHeight / 4)
        
    # [SUBMENU] 1) Play a random board ------------------------------------------------------------------------
        Submenu_X = 140
        Submenu_Y = int(ScreenHeight / 4 + 75)
        Button_X = int((Submenu_X + 170) / 2)
        Button_Y = int(Submenu_Y + 35)

        # Submenu - outline
        pygame.draw.rect(Screen, black, (Submenu_X - 2, Submenu_Y - 2, 250 + 4, 250 + 4))
        # Submenu - color
        pygame.draw.rect(Screen, backgroundcolor, (Submenu_X, Submenu_Y, 250, 250))
        # Submenu - title
        Button("PLAY", (Button_X + 73, Submenu_Y - 15), 75, 30, backgroundcolor, backgroundcolor)
        # Submenu - buttons
        Button("Sudoku", (Button_X, Button_Y), 218, 40, ButtonColor, HighlightColor, Sudoku_GameLoop)
        Button("Binairo", (Button_X, Button_Y + 50), 218, 40, ButtonColor, HighlightColor, Binairo_GameLoop)

    # [SUBMENU] 2) Solve an existing board --------------------------------------------------------------------
        Submenu_X = 150 + 260
        Submenu_Y = int(ScreenHeight / 4 + 75)
        Button_X = int((Submenu_X + 443) / 2)
        Button_Y = int(Submenu_Y + 35)

        # Submenu - outline
        pygame.draw.rect(Screen, black, (Submenu_X - 2, Submenu_Y - 2, 250 + 4, 250 + 4))
        # Submenu - color
        pygame.draw.rect(Screen, backgroundcolor, (Submenu_X, Submenu_Y, 250, 250))
        # Submenu - title
        Button("SOLVE", (Button_X + 73, Submenu_Y - 15), 75, 30, backgroundcolor, backgroundcolor)
        # Submenu - buttons
        Button("Sudoku", (Button_X, Button_Y), 218, 40, ButtonColor, HighlightColor, Sudoku_GameLoop)
        Button("Binairo", (Button_X, Button_Y + 50), 218, 40, ButtonColor, HighlightColor, Binairo_GameLoop)

    # EXIT Button ------------------------------------------------------------------------------------------
        Button("EXIT", (ScreenWidth /2 - 50, ScreenHeight - 75), 100, 40, (255,69,0), (139,0,0), quitgame)

    # Update Display ---------------------------------------------------------------------------------------
        pygame.display.update()
# ==========================================================================================================


# GAME LOOP: Sudoku ========================================================================================
def Sudoku_GameLoop():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # Set background color
        Screen.fill((backgroundcolor))

        # Display title
        TextObject("Sudoku", TitleFont, black, int(ScreenWidth / 2), 50)


    # BACK TO MAIN MENU Button (Action cant be passed through Button function so full code is used here) -
        TopLeft = (ScreenWidth / 2 - 110, ScreenHeight - 75)

        # Get mouse position & track mouse-clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Draw Button & Highlight button if slected & Perform action if pressed
        if TopLeft[0] + 100 > mouse[0] > TopLeft[0] and TopLeft[1] + 40 > mouse[1] > TopLeft[1]:
            pygame.draw.rect(Screen, (139,0,0), (int(TopLeft[0]), int(TopLeft[1]), 100, 40))
            if click[0] == 1:
                Menu = True
                running = False
        else:
            pygame.draw.rect(Screen, (255,69,0), (int(TopLeft[0]), int(TopLeft[1]), 100, 40))
        # Add Text to Button
        TextObject("MENU", ButtonFont, black, TopLeft[0] + (100 / 2), TopLeft[1] + (40 / 2))

    # EXIT Button ------------------------------------------------------------------------------------------
        Button("EXIT", (ScreenWidth /2 + 10, ScreenHeight - 75), 100, 40, (255,69,0), (139,0,0), quitgame)

        # Update Display
        pygame.display.update()

    # Completely close the game (if this code isn't here, it closes the loop but not the app. The app would go back to the main menu.
    if not Menu:
        quitgame()
# ==========================================================================================================

# GAME LOOP: Binairo =======================================================================================
def Binairo_GameLoop():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Set background color
        Screen.fill(backgroundcolor)

        # Display title
        TextObject("Binairo", TitleFont, black, int(ScreenWidth / 2), 50)

    # BACK TO MAIN MENU Button (Action cant be passed through Button function so full code is used here) -
        TopLeft = (ScreenWidth / 2 - 110, ScreenHeight - 75)

        # Get mouse position & track mouse-clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Draw Button & Highlight button if slected & Perform action if pressed
        if TopLeft[0] + 100 > mouse[0] > TopLeft[0] and TopLeft[1] + 40 > mouse[1] > TopLeft[1]:
            pygame.draw.rect(Screen, (139,0,0), (int(TopLeft[0]), int(TopLeft[1]), 100, 40))
            if click[0] == 1:
                Menu = True
                running = False
        else:
            pygame.draw.rect(Screen, (255,69,0), (int(TopLeft[0]), int(TopLeft[1]), 100, 40))
        # Add Text to Button
        TextObject("MENU", ButtonFont, black, TopLeft[0] + (100 / 2), TopLeft[1] + (40 / 2))

    # EXIT Button ------------------------------------------------------------------------------------------
        Button("EXIT", (ScreenWidth /2 + 10, ScreenHeight - 75), 100, 40, (255,69,0), (139,0,0), quitgame)

        # Update Display
        pygame.display.update()

    # Completely close the game (if this code isn't here, it closes the loop but not the app. The app would go back to the main menu.
    if not Menu:
        quitgame()
# ==========================================================================================================

# Start game
MainMenu()