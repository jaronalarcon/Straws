# STRAWS: THE GAME
# ----------------
# 
# Copyright pending
# 
# Check the README.md file for more information about this project.

# Imports and initialization
import pygame, sys
from json import load
pygame.init()

# Window and in-game clock
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create window
pygame.display.set_caption("Straws") # Title of window
clock = pygame.time.Clock() # Set game clock

# Background assets

# Terrain assets

# Player character assets
player = pygame.Rect(0, 800, 25, 25)
PLAYER_SPEED = 3

# Enemy character assets

# Item/collectible assets

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Game loop
# (Basic frame of loop, event handling logic were borrowed from GeeksForGeeks)
is_running = True
while is_running :
    # Add background image(s)
    # Please import background image and add it here

    # Event loop to check for game quit
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            is_running = False
            break
    
    # Key event tracing
    # (AI taught us that all key presses must come outside of the event loop)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] :
        print("walk backwards") # Filler code; please change
        player.x -= PLAYER_SPEED
    
    if keys[pygame.K_RIGHT] :
        print("walk forwards") # Filler code; please change
        player.x += PLAYER_SPEED

    # If the space bar is pressed
    if keys[pygame.K_SPACE] :
        # Make the character jump
        print("jump") # Filler code; please change
        player.y += PLAYER_SPEED

    # Player movement
    player.clamp_ip(screen.get_rect())
    screen.fill((40, 40, 40))
    pygame.draw.rect(screen, (255, 255, 255), player)

    # Update the entire screen
    pygame.display.flip()

    # Update the game clock
    clock.tick(30)

# Quit game
pygame.quit()
sys.exit()
