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
# Image folder
Images = os.path.dirname(os.path.realpath(__file__)) + '\Images'

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
def TextObject(Text, Font, Color):
    Text = Font.render(Text, True, Color)
    return Text, Text.get_rect()

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
    ButtonText, ButtonTextArea = TextObject(Text, ButtonFont, (0, 0, 0))
    ButtonTextArea.center = (int(TopLeft[0] + (ButtonWidth / 2)), int(TopLeft[1] + (ButtonHeight / 2)))
    Screen.blit(ButtonText, ButtonTextArea)
# ===========================================================================================================


# MAIN MENU ================================================================================================
def MainMenu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
        
        # Set background color
        Screen.fill(backgroundcolor)

        # Display title
        Title, TitleArea = TextObject("Puzzle Solver", TitleFont, (0, 0, 0))
        TitleArea.center  = (int(ScreenWidth / 2), int(ScreenHeight / 3))
        Screen.blit(Title, TitleArea)
        
        # Buttons
        Button("Sudoku", (ScreenWidth / 2 - 75, 300), 150, 40, (192, 192, 192), (135, 135, 135), Sudoku_GameLoop)
        Button("Binairo", (ScreenWidth / 2 - 75, 350), 150, 40, (192, 192, 192), (135, 135, 135), Binairo_GameLoop)
        
        # Update Display
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
        Title, TitleArea = TextObject("Sudoku", TitleFont, (0, 0, 0))
        TitleArea.center  = (int(ScreenWidth / 2), 50)
        Screen.blit(Title, TitleArea)

        # Update Display
        pygame.display.update()

    # Completely close the game (if this code isn't here, it closes the loop but not the app. The app would go back to the main menu.
    pygame.quit()
    quit()
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
        Title, TitleArea = TextObject("Binairo", TitleFont, (0, 0, 0))
        TitleArea.center  = (int(ScreenWidth / 2), 50)
        Screen.blit(Title, TitleArea)

        # Update Display
        pygame.display.update()

    # Completely close the game (if this code isn't here, it closes the loop but not the app. The app would go back to the main menu.
    pygame.quit()
    quit()
# ==========================================================================================================

# Start game
MainMenu()