############################################################################################################
# NAME: Default.py
# AUTHOR: Christophe Van den Eynde
# FUNCTION: Default settings for the Puzle sover pygame apllication (colors & fonts)
############################################################################################################

import pygame

# Colors ---------------------------------------------------------------------------------------------------
Colors = {
    # Screen background
    "Background":           (220,220,220),      # grey (grainsboro)
    # Button colors: Main menu - Puzle selection
    "PuzzleSelector":       (192, 192, 192),    # grey (silver)
    "PuzzleHighlight":      (135,206,235),      # skyblue
    # Button colors: Main menu - Play & Solve
    "Play":                 (0,255,127),        # springgreen 
    "PlayHighlight":        (50, 205, 50),      # limegreen
    # Button colors: Navigation buttons (menu & quit)
    "Navigation":           (255,69,0),
    "NavigationHighlight":  (139, 0, 0),
    # Button colors: Puzzle Option (new, reset, check, hint...)
    "Options":              (255, 0, 0),        # red
    "OptionsHighlight":     (255, 255, 0),      # yellow
    # Text colors
    "black":                (0, 0, 0),
    "white":                (255,255,255),
    # Board
    "Cube":                 (255,255,255),      # white
    "Correct":              (220, 220, 220),    # grey (grainsboro)
    "Hudoku_H":             (255, 0, 0),        # red 
    # Messages (solved - impossible)
    "Message":              (255, 0, 0)         # red       
}       

# Fonts -----------------------------------------------------------------------------------------------------
Fonts = {
    "TitleFont": pygame.font.Font('freesansbold.ttf', 60),
    "ButtonFont": pygame.font.Font('freesansbold.ttf', 15)
}
