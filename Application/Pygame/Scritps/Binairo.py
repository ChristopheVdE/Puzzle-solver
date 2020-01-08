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