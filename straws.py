# STRAWS: THE GAME
# ----------------
# 
# Copyright 2026 Jaron Alarcon, Ayaka Brown, Danielle Harrell
# 
# someone pls finish this

# Imports and initialization
import pygame, sys
pygame.init()

# Window and in-game clock
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create window
pygame.display.set_caption("Straws") # Title of window
clock = pygame.time.Clock() # Set game clock

# Game loop
# (Basic frame of loop, event handling logic were borrowed from GeeksForGeeks)

is_running = True
while is_running :
    # Event loop to check for quit
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            is_running = False
            break
    
    # Key event tracing
    # (AI taught us that all key presses must come outside of the event loop)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        print("walk backwards") # Filler code. please change
    
    if keys[pygame.K_RIGHT] :
        print("walk forwards") # Filler code; please change

    # If the space bar is pressed
    if keys[pygame.K_SPACE] :
        # Make the character jump
        print("jump") # Filler code; please change

    # Update the entire screen
    pygame.display.flip()

    # Update the game clock
    clock.tick(60)

# Quit game
pygame.quit()
sys.exit()
