############################################################################################################
# NAME: Binairo: create
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Create playable boards
############################################################################################################

# GAME LOOP: Binairo =======================================================================================
def Binairo_GameLoop():
# IMPORT SUDOKU SCRIPTS ------------------------------------------------------------------------------------
    from Binairo import board
# MAIN LOOP ------------------------------------------------------------------------------------------------
    running = True
    key = None
    Cube = None
    CreatedBoard = None
    FirstIteration = True
    UpdateBoard = None
    grid = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_KP0: # cheks for keypress --> combing keypress check with selected cube to update value in cube
                    key = '0'
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = '1'
            #if event.key == pygame.K_DELETE:

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
# SETTINGS WINDOW ------------------------------------------------------------------------------------------
    # number of cubes
        # show current number of cubes per row/col
        # increase by 2
        # decrease by 2
    # Turn of higlighting?
    # Reset board
    # Get Hint
    # Check current (partial) board
    # Create new board
    # Navigation Buttons --> move nav buttons to this submenu
# BOARD ----------------------------------------------------------------------------------------------------
    # inititialize board class    
        if not grid:
            grid = board(Screen, 10, (140, 100))
    # Print board, values ...
        grid.DarwBoardBackground(black)
        grid.DrawCubes((255, 255, 255))
        grid.HiglightLines(NavigationColor, mouse)
        grid.CreateBoard(FirstIteration)
        grid.Immutable()
        Cube = grid.SelectCube(mouse, click, Cube)
        UpdateBoard = grid.Updatecube(key, UpdateBoard, Cube)
        grid.PrintBoard()
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
        SelectedGame = Exit.functionality(mouse, click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)
# ITERATION COUNT ------------------------------------------------------------------------------------------
        FirstIteration = False
        key = None
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================