############################################################################################################
# Name: ActivateGameLoop.py
# Function: Activates or ends the correct gameloop
############################################################################################################

# Activate correct gameloop ================================================================================
def ActivateGameLoop(gametype: str) -> list:
    gameloop = []
    for game in ["Menu", "Quit", "SudokuPlay", "SudokuSolve", "BinairoPlay", "BinairoSolve", "HudokuPlay", "HudokuSolve"]:
        if game == gametype:
            gameloop.append((game, True))
        else:
            gameloop.append((game, False))
    return gameloop
# ==========================================================================================================