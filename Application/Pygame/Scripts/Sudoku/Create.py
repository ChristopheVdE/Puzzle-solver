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
        SelectedGame = Exit.functionality(mouse, click, ActivateGameLoop("Quit"))
        if SelectedGame: return SelectedGame
# UPDATE DISPLAY -------------------------------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)
# COMPLETELY CLOSE THE GAME WHEN SCREEN IS CLOSED ----------------------------------------------------------
    return ActivateGameLoop("Quit")
# ==========================================================================================================