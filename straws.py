# STRAWS: THE GAME
# ----------------
# 
# Copyright pending
# 
# Check the README.md file for more information about this project.

# Module imports
import pygame, sys
from json import load
from random import SystemRandom # Just for fun

# Initialize pygame
pygame.init()

# Game asset imports
from background import Background
from collectible import Collectible
from enemy import Enemy
from ground import Ground
from levels import Level
from player import Player
from text import Text

# Window and in-game clock
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create window
pygame.display.set_caption("Straws") # Title of window
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

# Level number tracker
level_number = 0

# Player score consistency tracker variable
total_score = 0

# Open research file
with open("research.json", "r") as i :
    research = load(i)

# Dictionary matching levels to research
levels_to_locations = {1 : "waiahole_beach_park",
                       2 : "lyon_arboretum",
                       3 : "kapolei"}

# Leveled game loop
for level in levels : # Body of loop debugged by AI, individual lines of code written by us
    # Increment level number
    level_number += 1

    # Introduce level
    print(f"\033[4mLevel {level_number}\033[0m")
    print(f"Fun fact: {SystemRandom().choice(research[levels_to_locations[level_number]])}\n") # Get a fun fact about the location
                                                                                               # (This is how we will sneak in the fifth must-have for this demo)

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
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    player.jump()

        # Set background image
        screen.blit(background.image, (0, 0))

        # Player, enemy, collectible updates
        player.update(ground_group)
        enemy_group.update(ground_group, player)
        coin_group.update()

        # Check collected items
        collected = pygame.sprite.spritecollide(player, coin_group, True)
        if collected :
            player.score += 1
            print(f"Each cap reminds you of what can be. Of what will be.\nScore: {player.score}\n") # Debugging... with LORE

        # Check goalpost interaction
        if pygame.sprite.collide_rect(player, goalpost) :
            # Store player's score for this level externally
            total_score = player.score

            # Break the game loop for this level
            is_incomplete = False

        # Draw assets on screen
        #screen.fill((40, 40, 40)) # This line is quite important but will implement later
        camera.update(ground_group, player)
        sprites = list(ground_group) + list(text_group) + list(enemy_group) + list(coin_group) + [player, goalpost]
        for sprite in sprites :
            screen.blit(sprite.image, camera.apply(sprite))

        # Update the entire screen
        pygame.display.flip()

        # Update the game clock
        clock.tick(50)

# Quit game
print("As the sun sets on the final day, you close your eyes and let yourself be embraced by this world, the world which you were once promised, some world once forsaken, now a world of rebirth.\n")
print("Thank you for playing our game! We hope you enjoyed playing this demo as much as we did making it.\n--Operation Straws Team")
pygame.quit()
sys.exit()
