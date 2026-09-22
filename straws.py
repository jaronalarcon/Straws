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
from collectible import Collectible
from enemy import Enemy
from ground import Ground
from levels import Level
from player import Player

# Window and in-game clock
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create window
pygame.display.set_caption("Straws") # Title of window
clock = pygame.time.Clock() # Set game clock

# Background (currently does not work, but may be used in future updates)
background = pygame.Surface(screen.get_size())
background = background.convert()

if pygame.font :
    font = pygame.font.Font(None, 64)
    text = font.render("Score: ", True, (140, 140, 140))
    textpos = text.get_rect(centerx = 100, centery = 50)
    background.blit(text, textpos)

# Character superclass (currently unused, but may be used in future updates)
class Character(pygame.sprite.Sprite) :
    def __init__(self, image : str, width : int, height : int,
                 move_speed : int | float, jump_height : int | float, floor : Ground,
                 starting_x : int) :
        # Call the parent class constructor
        super().__init__(self)

        # Load image assets
        self.image = pygame.image.load(image).convert_alpha()

        # Resize the image
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Generate the collision shape of the image
        self.rect = self.image.get_rect()

        # Movement speed and jump mechanics
        self.move_speed = move_speed
        self.jump_height = jump_height
        self.is_on_ground = False

        # Calculate character floor
        self.floor = floor.rect.top

        # Physics variables
        self.position = pygame.math.Vector2((int, self.floor))
        self.velocity = pygame.math.Vector2()
        self.gravity = pygame.math.Vector2((0, 0.8))

# Camera assets
class Camera :
    def __init__(self) :
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.x = 0
        self.y = 0

    def update(self, target : Player) :
        # Check if the player is almost outside range of vision
        if target.rect.x >= SCREEN_WIDTH // 2 :
            self.x = target.rect.centerx - self.width // 2

        # Maintain original position on screen whenever possible
        else :
            self.x = 0

    def apply(self, entity) :
        return entity.rect.move(-self.x, -self.y)

    def reset(self) :
        self.x = 0
        self.y = 0

camera = Camera()

# Goal assets

# ---------------------------------------------------------------------------------------------------------------------------------------------------

levels = Level.get_all_levels()

# Player score consistency tracker variable
total_score = 0

# Leveled game loop
for level in levels :
    # Get the assets for this level
    ground_group, player, enemy_group, coin_group, goalpost = level()

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
        screen.fill((40, 40, 40))
        camera.update(player)
        sprites = list(ground_group) + list(enemy_group) + list(coin_group) + [player, goalpost]
        for sprite in sprites :
            screen.blit(sprite.image, camera.apply(sprite))

        # Update the entire screen
        pygame.display.flip()

        # Update the game clock
        clock.tick(50)

# Quit game
pygame.quit()
sys.exit()
