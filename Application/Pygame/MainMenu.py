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

# FUNCTIONS ================================================================================================
# Text area (for renderign) --------------------------------------------------------------------------------
def TextObject(Text, Font, Color, X, Y):
    Text = Font.render(Text, True, Color)
    TextArea = Text.get_rect()
    TextArea.center  = (int(X), int(Y))
    Screen.blit(Text, TextArea)

# Create INteractive buttons -------------------------------------------------------------------------------
def Button(Text, TopLeft, ButtonWidth, ButtonHeight, NormalColor, HighlightColor, mouse):
    # Draw Button & Highlight button if slected & Perform action if pressed
    if TopLeft[0] + ButtonWidth > mouse[0] > TopLeft[0] and TopLeft[1] + ButtonHeight > mouse[1] > TopLeft[1]:
        pygame.draw.rect(Screen, HighlightColor, (int(TopLeft[0]), int(TopLeft[1]), ButtonWidth, ButtonHeight))
    else:
        pygame.draw.rect(Screen, NormalColor, (int(TopLeft[0]), int(TopLeft[1]), ButtonWidth, ButtonHeight))

    # Add Text to Button
    TextObject(Text, ButtonFont, black, TopLeft[0] + (ButtonWidth / 2), TopLeft[1] + (ButtonHeight / 2))

# Quit the game ---------------------------------------------------------------------------------------------
def quitgame():
    pygame.quit()
    quit()
# ===========================================================================================================

# GENERAL INFO ==============================================================================================
# Image folder ----------------------------------------------------------------------------------------------
Images = os.path.dirname(os.path.realpath(__file__)) + '\Images'

# Colors ----------------------------------------------------------------------------------------------------
black           = (0, 0, 0)
BackgroundColor = (220,220,220)     #grey (grainsboro)
ButtonColor     = (192, 192, 192)   #grey (silver)
HighlightColor  = (135, 135, 135)   #grey (slightly lighter grey)
Playbutton      = (0,255,127)       #springgreen 
PlayHighlight   = (50,205,50)       #limegreen

# Initialize game -------------------------------------------------------------------------------------------
pygame.init()

# Display size ----------------------------------------------------------------------------------------------
ScreenWidth = 800
ScreenHeight = 600
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

# Caption & logo --------------------------------------------------------------------------------------------
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
    Sudoku = False
    Binairo = False

# MAIN LOOP -------------------------------------------------------------------------------------------------
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
    # Set background color
        Screen.fill(BackgroundColor)
    # Display title
        TextObject("Puzzle Solver", TitleFont, black, ScreenWidth / 2, ScreenHeight / 7)
    # Get mouse position & track mouse-clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
# [SUBMENU] CHOOSE PUZZLE ------------------------------------------------------------------------------------
    # Submenu settings
        Submenu_X = 140
        Submenu_Y = int(ScreenHeight / 7 + 70)
        Submenu_Width = 250
        Submenu_height = 325
    # Button settings
        Button_X = int((Submenu_X + 170) / 2)
        Button_Y = int(Submenu_Y + 25)
        ButtonWidth = 218
        ButtonHeight = 40

    # Submenu - outline
        pygame.draw.rect(Screen, black, (Submenu_X - 2, Submenu_Y - 2, Submenu_Width + 4, Submenu_height + 4))
    # Submenu - color
        pygame.draw.rect(Screen, BackgroundColor, (Submenu_X, Submenu_Y, Submenu_Width, Submenu_height))
    # Submenu - title
        Button("CHOOSE PUZZLE", (Button_X + 35, Submenu_Y - 16), 150, 30, BackgroundColor, BackgroundColor, mouse)
    # Submenu - buttons
        Button("Sudoku", (Button_X, Button_Y), ButtonWidth, ButtonHeight, ButtonColor, HighlightColor, mouse)
        Button("Binairo", (Button_X, Button_Y + 50), ButtonWidth, ButtonHeight, ButtonColor, HighlightColor, mouse)

# [SUBMENU] 2) Puzzle info -----------------------------------------------------------------------------
    # Submenu settings
        Submenu_X = Submenu_X + 260 + 10  # start column 1 + width column 1 + space between columns

    # Submenu - outline
        pygame.draw.rect(Screen, black, (Submenu_X - 2, Submenu_Y - 2, Submenu_Width + 4, Submenu_height + 4))
    # Submenu - color
        pygame.draw.rect(Screen, BackgroundColor, (Submenu_X, Submenu_Y, Submenu_Width, Submenu_height))
    # Submenu - title
        Button("PUZZLE INFO", (int((Submenu_X + 443) / 2) + 35, Submenu_Y - 16), 150, 30, BackgroundColor, BackgroundColor, mouse)

    # Submenu - Sudoku info
        # Sudoku button activation
        if (Button_X + ButtonWidth > mouse[0] > Button_X and Button_Y + ButtonHeight > mouse[1] > Button_Y) or Sudoku:
            # Activate & decativate the correct info screen
            if click[0] == 1: Sudoku = True
            Binairo = False

            # Title
            TextObject("Sudoku", ButtonFont, black, 535, Submenu_Y + 25)
            # Puzzle image
            image = pygame.image.load(Images + '\Sudoku.jpg')
            Screen.blit(image, (Submenu_X + 65, Submenu_Y + 45))
            # Puzzle info
            TextObject("Fill a 9×9 grid.", ButtonFont, black, 535, Submenu_Y + 200)
            TextObject("Each column, row and 3×3 grid", ButtonFont, black, 535, Submenu_Y + 220)
            TextObject("should contain all digits from 1 to 9.", ButtonFont, black, 535, Submenu_Y + 235)
            # Play button
            Button("PLAY", (Submenu_X + 15, Submenu_Y + 270), 100, 40, Playbutton, PlayHighlight, mouse)
            if Submenu_X + 15 + 100 > mouse[0] > Submenu_X + 15 and Submenu_Y + 270 + 40 > mouse[1] > Submenu_Y + 270 and click[0] == 1:
                Sudoku_GameLoop()

            # solve button
            Button("SOLVE", (Submenu_X + 135, Submenu_Y + 270), 100, 40, Playbutton, PlayHighlight, mouse)
            if Submenu_X + 135 + 100 > mouse[0] > Submenu_X + 135 and Submenu_Y + 270 + 40 > mouse[1] > Submenu_Y + 270 and click[0] == 1:
                Sudoku_GameLoop()

    # Submenu - Binairo info
        if (Button_X + ButtonWidth > mouse[0] > Button_X and Button_Y + 50 + ButtonHeight > mouse[1] > Button_Y + 50) or Binairo:
            # Activate & decativate the correct info screen
            if click[0] == 1: Binairo = True
            Sudoku = False

            # Title
            TextObject("Binairo", ButtonFont, black, 535, Submenu_Y + 25)
            # Puzzle image
            image = pygame.image.load(Images + '\Binairo.png')
            Screen.blit(image, (Submenu_X + 65, Submenu_Y + 45))
            # Puzzle info
            # Play button
            # solve button

    # EXIT Button ------------------------------------------------------------------------------------------
        Button("EXIT", (ScreenWidth / 2 - 50, ScreenHeight - 75), 100, 40, (255, 69, 0), (139, 0, 0), mouse)
        if ((ScreenWidth / 2 - 50) + 100 > mouse[0] > (ScreenWidth / 2 - 50) and (ScreenHeight - 75) + 40 > mouse[1] > (ScreenHeight - 75)):
            if click[0] == 1:
                quitgame()

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
        Screen.fill((BackgroundColor))

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
        # Button("EXIT", (ScreenWidth /2 + 10, ScreenHeight - 75), 100, 40, (255,69,0), (139,0,0), quitgame)

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
        Screen.fill(BackgroundColor)

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
        # Button("EXIT", (ScreenWidth /2 + 10, ScreenHeight - 75), 100, 40, (255,69,0), (139,0,0), quitgame)

        # Update Display
        pygame.display.update()

    # Completely close the game (if this code isn't here, it closes the loop but not the app. The app would go back to the main menu.
    if not Menu:
        quitgame()
# ==========================================================================================================

# Start game
MainMenu()