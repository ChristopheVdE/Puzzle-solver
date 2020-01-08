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
# Text area (for renderign) (centered) ---------------------------------------------------------------------
def TextObject(Text, Font, Color, X, Y):
    TextSurface = Font.render(Text, True, Color)
    TextArea = TextSurface.get_rect()
    TextArea.center  = (int(X), int(Y))
    Screen.blit(TextSurface, TextArea)

# Multi line text area (for renderign) (not centered) ------------------------------------------------------
def MultilineText(Text, Font, Color, pos, MaxWidth, MaxHeight):
    
    space = Font.size(' ')[0]  # The width of a space.
    X, Y = pos

    for Sentence in Text.splitlines():
        for Word in Sentence.split(' '):
            WordSurface = Font.render(Word, True, Color)
            WordWidth, WordHeight = WordSurface.get_size()

            if X + WordWidth >= MaxWidth:
                X = pos[0]          # reset X
                Y += WordHeight     # jump to next line
            Screen.blit(WordSurface, (X, Y))
            X += WordWidth + space
        X = pos[0]
        Y += WordHeight

# Create INteractive buttons -------------------------------------------------------------------------------
def Button(Text, TopLeft, ButtonWidth, ButtonHeight, NormalColor, HighlightColor, mouse, Selected = False):
    # Draw Button & Highlight button if slected & Perform action if pressed
    if (TopLeft[0] + ButtonWidth > mouse[0] > TopLeft[0] and TopLeft[1] + ButtonHeight > mouse[1] > TopLeft[1]) or Selected:
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
black               = (0, 0, 0)
BackgroundColor     = (220,220,220)     #grey (grainsboro)
ButtonColor         = (192, 192, 192)   #grey (silver)
HighlightColor      = (135,206,235)     #skyblue
Playbutton          = (0,255,127)       #springgreen 
PlayHighlight       = (50, 205, 50)     #limegreen
NavigationColor     = (255,69,0)
NavigationHighlight = (139,0,0)

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

# MAIN LOOP ------------------------------------------------------------------------------------------------
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
        
# [SUBMENU] CHOOSE PUZZLE ----------------------------------------------------------------------------------
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
        Button("Sudoku", (Button_X, Button_Y), ButtonWidth, ButtonHeight, ButtonColor, HighlightColor, mouse, Sudoku)
        Button("Binairo", (Button_X, Button_Y + 50), ButtonWidth, ButtonHeight, ButtonColor, HighlightColor, mouse, Binairo)

# [SUBMENU] 2) Puzzle info ---------------------------------------------------------------------------------
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

            # Puzzle image
            image = pygame.image.load(Images + '\Sudoku.jpg')
            Screen.blit(image, (Submenu_X + 65, Submenu_Y + 25))
            # Puzzle info
            MultilineText("Fill a 9×9 grid.\nEach column, row and 3×3 grid should contain all digits from 1 to 9.", ButtonFont, black, (420, Submenu_Y + 180), 650, 250)
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

            # Puzzle image
            image = pygame.image.load(Images + '\Binairo.png')
            Screen.blit(image, (Submenu_X + 65, Submenu_Y + 25))
            # Puzzle info
            MultilineText("Each column/ row needs to have te same ammount of 1 and 0.\nMax 2 times the same number next to eachother.\nNo identical rows/ columns alowed.", ButtonFont, black, (420, Submenu_Y + 150), 650, 250)
            # Play button
            Button("PLAY", (Submenu_X + 15, Submenu_Y + 270), 100, 40, Playbutton, PlayHighlight, mouse)
            if Submenu_X + 15 + 100 > mouse[0] > Submenu_X + 15 and Submenu_Y + 270 + 40 > mouse[1] > Submenu_Y + 270 and click[0] == 1:
                Binairo_GameLoop()

            # solve button
            Button("SOLVE", (Submenu_X + 135, Submenu_Y + 270), 100, 40, Playbutton, PlayHighlight, mouse)
            if Submenu_X + 135 + 100 > mouse[0] > Submenu_X + 135 and Submenu_Y + 270 + 40 > mouse[1] > Submenu_Y + 270 and click[0] == 1:
                Binairo_GameLoop()
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

# MAIN LOOP ------------------------------------------------------------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # Set background color
        Screen.fill((BackgroundColor))
    # Display title
        TextObject("Sudoku", TitleFont, black, int(ScreenWidth / 2), 50)
    # Get mouse position & track mouse-clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

# NAVIGATION BUTTONS ---------------------------------------------------------------------------------------
    # Menu button
        Button("MENU", (ScreenWidth / 2 - 110, ScreenHeight - 75), 100, 40, NavigationColor, NavigationHighlight, mouse)
        if (ScreenWidth / 2 - 110) + 100 > mouse[0] > (ScreenWidth / 2 - 110) and (ScreenHeight - 75) + 40 > mouse[1] > (ScreenHeight - 75) and click[0] == 1:
            Menu = True
            running = False
    # EXIT Button 
        Button("EXIT", (ScreenWidth / 2 + 10, ScreenHeight - 75), 100, 40, NavigationColor, NavigationHighlight, mouse)
        if (ScreenWidth / 2 + 10) + 100 > mouse[0] > (ScreenWidth / 2 + 10) and (ScreenHeight - 75) + 40 > mouse[1] > (ScreenHeight - 75) and click[0] == 1:
            quitgame()

# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
# ==========================================================================================================

# GAME LOOP: Binairo =======================================================================================
def Binairo_GameLoop():
    running = True

# MAIN LOOP ------------------------------------------------------------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
            Menu = True
            running = False
    # EXIT Button 
        Button("EXIT", (ScreenWidth / 2 + 10, ScreenHeight - 75), 100, 40, NavigationColor, NavigationHighlight, mouse)
        if (ScreenWidth / 2 + 10) + 100 > mouse[0] > (ScreenWidth / 2 + 10) and (ScreenHeight - 75) + 40 > mouse[1] > (ScreenHeight - 75) and click[0] == 1:
            quitgame()

# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
# ==========================================================================================================

# Start game
MainMenu()