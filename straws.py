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
class Player :
    # We took most of this class's design from AI
    # because we weren't sure how to change the player
    # character's vertical position to simulate jumping.
    
    def __init__(self) :
        # Character dimensions
        self.width = 25
        self.height = 25
        self.body = pygame.Rect(50, SCREEN_HEIGHT - self.height - 50, self.width, self.height) # Must change with player assets!

        # Movement speed
        self.speed = 5
        self.jump_height = -10

        # Physics variables
        self.velocity_y = 0
        self.gravity = 0.4
        self.is_jumping = False

        # Floor
        self.floor = SCREEN_HEIGHT - self.height - 50

    def move(self) :
        # (AI taught us that all key presses must come outside of the event loop)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a] :
            print("walk backwards") # Filler code; please remove when done
            self.body.x -= player.speed
        
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] :
            print("walk forwards") # Filler code; please remove when done
            self.body.x += player.speed

    def jump(self) :
        if not self.is_jumping :
            self.velocity_y = self.jump_height
            self.is_jumping = True

    def update(self) :
        # Apply gravity to the vertical velocity
        self.velocity_y += self.gravity
        self.body.y += self.velocity_y

        # Floor collision check
        if self.body.y >= self.floor :
            self.body.y = self.floor
            self.velocity_y = 0
            self.is_jumping = False

        # Keep player within screen bounds horizontally
        if self.body.left < 0 :
            self.body.left = 0
        if self.body.right > SCREEN_WIDTH :
            self.body.right = SCREEN_WIDTH

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 255, 255), self.body) # Update for player assets!

player = Player()

# Enemy character assets
class Enemy :
    def __init__(self) :
        # Character dimensions
        self.width = 25
        self.height = 25
        self.body = pygame.Rect(SCREEN_WIDTH - 75, SCREEN_HEIGHT - self.height - 50, self.width, self.height) # Must change with enemy assets!

        # Movement speed
        self.speed = 3

    def move(self) :
        # Move left across the screen
        self.body.x -= self.speed

    def update(self, player : Player) :
        # If the enemy goes off-screen, reset its position to the right side of the screen
        if self.body.right < 0 :
            self.body.left = SCREEN_WIDTH
        if self.body.x == player.x and self.body.y == player.y :
            print("enemy collided with player") # Filler code; please remove when done

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 0, 0), self.body) # Update for enemy assets!

enemy = Enemy()

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

        # Check if the 
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                print("jump")
                player.jump()
                player.update()

    # Player movement
    player.move()
    player.update()
    enemy.update(player)
    screen.fill((40, 40, 40))
    player.draw(screen)

    # Update the entire screen
    pygame.display.flip()

    # Update the game clock
    clock.tick(50)

# Quit game
pygame.quit()
sys.exit()
