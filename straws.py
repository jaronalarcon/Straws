# STRAWS: THE GAME
# ----------------
# 
# Copyright pending
# 
# Check the README.md file for more information about this project.

# Version number
version = "Beta 1.2.62"

# Module imports
import pygame, sys
from random import SystemRandom # Just for fun
from time import sleep

# Initialize pygame
pygame.init()

# Game asset imports
from cutscene import Cutscene
from levels import Level
from player import Player

# Window and in-game clock
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create window
pygame.display.set_caption(f"Straws - {version}") # Title of window
clock = pygame.time.Clock() # Set game clock

# Camera assets
class Camera :
    """ In-game camera.
        Class developed with the help of AI. """
    def __init__(self) :
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.x = 0
        self.y = 0

        # Scroll speed
        self.PAN_SPEED = 1

    def update(self, grounds, target : Player) :
        # Check if the player is almost outside horizontal range of vision from the left
        if target.rect.centerx - self.x < SCREEN_WIDTH * 0.5 and target.rect.centerx > SCREEN_WIDTH // 2 :
            # Adjust the camera's position by the displacement of the player from the center of the screen
            dx = target.rect.centerx - SCREEN_WIDTH * 0.5
            self.x += (dx - self.x) * self.PAN_SPEED

        # Check if the player is almost outside horizontal range of vision from the right
        elif (target.rect.centerx - self.x > SCREEN_WIDTH * 0.5 and
              target.rect.centerx < grounds.sprites()[len(grounds.sprites()) - 1].rect.right) :
            dx = target.rect.centerx - SCREEN_WIDTH * 0.5
            self.x += (dx - self.x) * self.PAN_SPEED

        # Check if the player is almost outside vertical range of vision
        if target.rect.centery < SCREEN_HEIGHT // 2 :
            dy = target.rect.centery - SCREEN_HEIGHT * 0.5
            self.y += (dy - self.y) * self.PAN_SPEED

    def apply(self, entity) :
        return entity.rect.move(-self.x, -self.y)

    def reset(self) :
        self.x = 0
        self.y = 0

camera = Camera()

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Get levels
levels = Level.get_all_levels()

# Player score consistency tracker variable
total_score = 0

# Overall loop control variable
running = True

# Main game loop
while running :
    # Title screen procedure
    bg, title_text, start_button, end_button = Cutscene.title_screen()

    # Inner game loop for title screen
    is_not_started = True
    while is_not_started :
        # Standard exit event check
        for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    pygame.quit(); sys.exit()

                # Check if the mouse is left-clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 :
                        # Check if the mouse clicked on the start button
                        # Collision method suggested by AI
                        if start_button.rect.collidepoint(event.pos) :
                            # Exit the title screen procedure
                            is_not_started = False

                        # Check if the mouse clicked on the end button
                        elif end_button.rect.collidepoint(event.pos) :
                            # Close the window, exit the program
                            pygame.quit(); sys.exit()

        # Draw assets
        screen.blit(bg.image, (0, 0))
        screen.blit(title_text, (500, 100))
        screen.blit(start_button.image, start_button.rect.topleft)
        screen.blit(end_button.image, end_button.rect.topleft)

        # Update game display
        pygame.display.flip() # Can't believe I forgot to add this here

    # ---------------------------------------------------------------------------------------------

    # Leveled game loop
    for level in levels : # Body of loop debugged by AI, individual lines of code written by us
        # Get the assets for this level
        background, ground_group, player, enemy_group, coin_group, goalpost, text_group = level()

        # Reset camera for the current level's player
        camera.reset()

        # Get the player's score thus far
        player.set_score(total_score)

        # Set the next level as incomplete
        is_incomplete = True
        while is_incomplete :
            # Player updates and general event loop
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.quit(); sys.exit()

                # Jump event
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                    player.jump()

            # Set background image
            screen.blit(background.image, (0, 0))

            # Write player score on the background
            score_font = pygame.font.SysFont("Baloo 2", 48)
            screen.blit(score_font.render(f"Score: {player.score}", True, (25, 25, 150)), (10, 10))

            # Player, enemy, collectible updates
            player.update(ground_group)
            enemy_group.update(ground_group, player)
            coin_group.update()

            # Check collected items
            if pygame.sprite.spritecollide(player, coin_group, True) :
                player.score += 1
                print(f"Each cap reminds you of what can be. Of what will be.") # Do we need this?

            # Check goalpost interaction
            if pygame.sprite.collide_rect(player, goalpost) :
                # Store player's score for this level externally
                total_score = player.score

                # Break the game loop for this level
                is_incomplete = False

            # Draw assets on screen
            camera.update(ground_group, player)
            sprites = list(ground_group) + list(text_group) + list(enemy_group) + list(coin_group) + [player, goalpost]
            for sprite in sprites :
                screen.blit(sprite.image, camera.apply(sprite))

            # Update the entire screen
            pygame.display.flip()

            # Update the game clock
            clock.tick(50)

    # ---------------------------------------------------------------------------------------------
    
    # End screen procedure
    Cutscene.end_screen(screen, total_score)

    running = False # End the game loop

# Quit game
print("\nThank you for playing our game! We hope you enjoyed playing this demo as much as we did making it.\n--Straws Development Team") # Thank-you message from us
pygame.quit()
sys.exit()
