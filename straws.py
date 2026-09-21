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
from enemy import Enemy
from ground import Ground
from player import Player

# Window and in-game clock
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create window
pygame.display.set_caption("Straws") # Title of window
clock = pygame.time.Clock() # Set game clock

# Ground assets
ground1 = Ground(800, 50, 400, 750)
ground2 = Ground(1100, 50, 1600, 750)
ground3 = Ground(400, 50, 1600, 575)
ground4 = Ground(400, 50, 2100, 375)
ground5 = Ground(1000, 50, 3100, 700)
ground_group_1 = pygame.sprite.Group(ground1, ground2, ground3, ground4, ground5)

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

# Player character assets
player = Player(ground1)
player_group = pygame.sprite.GroupSingle(player)

# Enemy character assets
enemy1 = Enemy(ground1, 400)
enemy2 = Enemy(ground2, 1600)
enemy3 = Enemy(ground3, 1750)
enemy4 = Enemy(ground4, 2200)
enemy_group_1 = pygame.sprite.Group(enemy1, enemy2, enemy3, enemy4)

# Camera assets
class Camera :
    def __init__(self) :
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.x = 0
        self.y = 0

    def update(self, target : Player) :
        if target.rect.x >= SCREEN_WIDTH // 2 :
            self.x = target.rect.centerx - self.width // 2

    def apply(self, entity) :
        return entity.rect.move(-self.x, -self.y)

camera = Camera()

# Item/collectible assets

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Game loop
# (Basic frame of loop, event handling logic were borrowed from GeeksForGeeks)
is_running = True
while is_running :
    # Show text
    screen.blit(background, (0, 0))

    # Get sprites to draw
    sprites = list(ground_group_1) + list(player_group) + list(enemy_group_1)

    # Add background image(s)
    # Please import background image and add it here

    # General event loop
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            is_running = False
            break

        # Jump event
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                player.jump()
                player_group.update(ground_group_1)

    # Player movement
    player_group.update(ground_group_1)
    enemy_group_1.update(ground_group_1, player)
    screen.fill((40, 40, 40))
    ground_group_1.draw(screen)
    player_group.draw(screen)
    enemy_group_1.draw(screen)

    # Update camera
    camera.update(player)
    screen.fill((40, 40, 40))
    for sprite in sprites :
        screen.blit(sprite.image, camera.apply(sprite))

    # Update the entire screen
    pygame.display.flip()

    # Update the game clock
    clock.tick(50)

# Quit game
pygame.quit()
sys.exit()
