############################################################################################################
# Name: GetPressedKey.py
# Function: Return the pressed key
############################################################################################################

# Imports ==================================================================================================
import pygame
# ==========================================================================================================

def GetPressedKey(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_0 or event.key == pygame.K_KP0 or event.key == pygame.K_DELETE:
            return '0'
        if event.key == pygame.K_1 or event.key == pygame.K_KP1:
            return '1'
        if event.key == pygame.K_2 or event.key == pygame.K_KP2:
            return '2'
        if event.key == pygame.K_3 or event.key == pygame.K_KP3:
            return '3'
        if event.key == pygame.K_4 or event.key == pygame.K_KP4:
            return '4'
        if event.key == pygame.K_5 or event.key == pygame.K_KP5:
            return '5'
        if event.key == pygame.K_6 or event.key == pygame.K_KP6:
            return '6'
        if event.key == pygame.K_7 or event.key == pygame.K_KP7:
            return '7'
        if event.key == pygame.K_8 or event.key == pygame.K_KP8:
            return '8'
        if event.key == pygame.K_9 or event.key == pygame.K_KP9:
            return '9'
    else:
        return None