# STRAWS: THE GAME
# ----------------
# 
# Copyright pending
# 
# Check the README.md file for more information about this project.

# Version number
version = "Beta 1.2.40"

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

        # Camera boundary
        self.UPPER_BOUND = self.LOWER_BOUND = 0.5 # vertical axis is flipped in pygame

        # Scroll speed
        self.PAN_SPEED = 1

    def update(self, grounds, target : Player) :
        # Define player camera borders
        player_screen_x = target.rect.centerx - self.x
        player_screen_y = target.rect.centery - self.y

        # Check if the player is almost outside horizontal range of vision
        if player_screen_x < SCREEN_WIDTH * self.UPPER_BOUND and target.rect.centerx > SCREEN_WIDTH // 2 :
            dx = target.rect.centerx - SCREEN_WIDTH * self.UPPER_BOUND
            self.x += (dx - self.x) * self.PAN_SPEED

        elif (player_screen_x > SCREEN_WIDTH * self.LOWER_BOUND and
              target.rect.centerx < grounds.sprites()[len(grounds.sprites()) - 1].rect.right) :
            dx = target.rect.centerx - SCREEN_WIDTH * self.LOWER_BOUND
            self.x += (dx - self.x) * self.PAN_SPEED

        # Check if the player is almost outside vertical range of vision
        if target.rect.centery < SCREEN_HEIGHT // 2 :
            dy = target.rect.centery - SCREEN_HEIGHT * self.UPPER_BOUND
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

# Loop control variable
running = True

# Main game loop
while running :
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
    
    # End screen procedure
    Cutscene.end_screen(screen)

    running = False # End the game loop

# Quit game
print("Thank you for playing our game! We hope you enjoyed playing this demo as much as we did making it.\n--Straws Development Team")
pygame.quit()
sys.exit()
