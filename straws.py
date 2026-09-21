# STRAWS: THE GAME
# ----------------
# 
# Copyright pending
# 
# Check the README.md file for more information about this project.

# Imports and initialization
import pygame, sys
from ground import Ground
from player import Player
from enemy import Enemy
from json import load
from random import SystemRandom # Just for fun
pygame.init()

# Window and in-game clock
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create window
pygame.display.set_caption("Straws") # Title of window
clock = pygame.time.Clock() # Set game clock

# Ground coordinates
GROUND_X = 50
GROUND_Y = 700

ground1 = Ground(SCREEN_WIDTH, 50, SCREEN_WIDTH // 2, 750)
ground_group = pygame.sprite.GroupSingle(ground1)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Pygame rect documentation

# .x
# .y
# .top
# .bottom
# .left
# .right

# ---------------------------------------------------------------------------------------------------------------------------------------------------

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

enemy = Enemy(ground1, 300)
enemy_group = pygame.sprite.GroupSingle(enemy)

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
    sprites = [ground1, player, enemy]

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
                player.update()

    # Player movement
    player_group.update()
    enemy_group.update(player)
    screen.fill((40, 40, 40))
    ground_group.draw(screen)
    player_group.draw(screen)
    enemy_group.draw(screen)

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
