import sys

# FUNCTIONS ================================================================================================
# Quit the game --------------------------------------------------------------------------------------------
def quitgame():
    pygame.quit()
    sys.exit()
# Activate correct gameloop --------------------------------------------------------------------------------
def ActivateGameLoop(gametype):
    gameloop = []
    for game in ["Menu", "Quit", "SudokuPlay", "SudokuSolve", "BinairoPlay", "BinairoSolve", "HudokuPlay", "HudokuSolve"]:
        if game == gametype:
            gameloop.append((game, True))
        else:
            gameloop.append((game, False))
    return gameloop
# ==========================================================================================================