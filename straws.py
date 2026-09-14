# STRAWS: THE GAME
# ----------------
# 
# Copyright pending
# 
# Check the README.md file for more information about this project.

# Imports and initialization
import pygame, sys
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

# Background assets

# Terrain assets

# Player character assets
class Player(pygame.sprite.Sprite) :
    # We took most of this class's design from AI
    # because we weren't sure how to change the player
    # character's vertical position to simulate jumping.
    
    def __init__(self) :
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)

        # Load image assets for player character
        self.image = pygame.image.load("handsome-young-man-in-suit-standing-with-hands-in-pockets-over-isolated-on-transparent-background-png.png").convert_alpha() # Please change with player assets!

        # Resize the image
        self.width = 50
        self.height = 1.5 * self.width
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Get the rectangle of the image for collision detection
        self.rect = self.image.get_rect()

        # Movement speed and jump height
        self.speed = 5
        self.jump_height = -10

        # Physics variables
        self.velocity_y = 0
        self.gravity = 0.4
        self.is_jumping = False

        # Floor
        self.floor = GROUND_Y - self.height

        # Place the player character at the bottom of the screen
        self.rect.center = (GROUND_X, self.floor)

    def move(self) :
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a] :
            self.rect.x -= player.speed
        
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] :
            self.rect.x += player.speed

    def jump(self) :
        if not self.is_jumping :
            self.velocity_y = self.jump_height
            self.is_jumping = True

    def update(self) :
        # Allow the player to move
        self.move()

        # Apply gravity to the vertical velocity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Floor collision check
        if self.rect.y >= self.floor :
            self.rect.y = self.floor
            self.velocity_y = 0
            self.is_jumping = False

        # Keep player within screen bounds horizontally
        if self.rect.left < 0 :
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH :
            self.rect.right = SCREEN_WIDTH

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 255, 255), self.rect) # Update for player assets!

player = Player()
player_group = pygame.sprite.GroupSingle(player)

# Enemy character assets
class Enemy(pygame.sprite.Sprite) :
    def __init__(self) :
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)

        # Load image assets for enemy character
        self.image = pygame.image.load("pngtree-full-black-trash-bag-png-image_14333046.png").convert_alpha() # Please change with enemy assets!

        # Resize the image
        self.width = 50
        self.height = 50
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Initialize rectangle collision
        self.rect = self.image.get_rect()

        # Movement speed
        self.speed = 3

        # Floor
        self.floor = GROUND_Y - self.height

        # Set the center to the ground
        self.rect.center = (GROUND_X + 250, self.floor)

    def move(self) :
        # Move left across the screen
        self.rect.x -= self.speed

    def update(self, player : Player) :
        # Make the enemy move
        self.move()

        """ IMPORTANT: The enemy's height is defined by the top of its body. """
        # If the enemy goes off-screen, invert the enemy's movement
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH :
            self.speed *= -1
        if abs(self.rect.x - player.rect.x) <= self.width and player.rect.y + player.height > self.rect.y and player.rect.y + player.height <= self.rect.y + self.height :
            print("NYEH HEH HEH!") if SystemRandom().randint(0, 99) == 0 else print("As you draw your final breath, you feel it leaking into your brain, stealing away your life just like the others. Was it ever an escape, or was it delaying the inevitable?") # Easter egg
            pygame.quit(); sys.exit()

    def die(self, player : Player) :
        if player.rect.y == self.rect.y and abs(player.rect.x - self.rect.x) <= self.width :
            print("enemy killed")

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 0, 0), self.rect) # Update for enemy assets!

enemy = Enemy()
enemy_group = pygame.sprite.GroupSingle(enemy)

# Item/collectible assets

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Game loop
# (Basic frame of loop, event handling logic were borrowed from GeeksForGeeks)
is_running = True
while is_running :
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
    player_group.draw(screen)
    enemy_group.draw(screen)

    # Update the entire screen
    pygame.display.flip()

    # Update the game clock
    clock.tick(50)

# Quit game
pygame.quit()
sys.exit()
