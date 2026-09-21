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
class Ground(pygame.sprite.Sprite) :
    def __init__(self, width : int, height : int, x : int, y : int) :
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)

        # Load image assets for ground
        self.image = pygame.image.load("pngtree-illustration-of-ground-png-image_5027670.png").convert_alpha() # Change with ground assets!

        # Resize the image
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, 0) # Rotate the image if necessary
                                                            # Must only be used with properly implemented Rect objects

        # Get the rectangle of the image for collision detection
        self.rect = self.image.get_rect()

        # Place the ground at the bottom of the screen
        self.rect.center = (x, y)

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

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
class Player(pygame.sprite.Sprite) :
    # We took most of this class's design from AI
    # because we weren't sure how to change the player
    # character's vertical position to simulate jumping.
    
    def __init__(self, floor : Ground) :
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

        # Movement speed and jump mechanics
        self.move_speed = 6
        self.jump_height = -17.5 # Negative because the y-axis is inverted in Pygame
        self.is_on_ground = False

        # Floor
        self.floor = floor.rect.top

        # Physics variables
        self.position = pygame.math.Vector2((50, self.floor))
        self.velocity = pygame.math.Vector2()
        self.gravity = pygame.math.Vector2((0, 0.8))

        # Set the center to the ground
        self.rect.midbottom = (50, self.floor)
        self.position.x = self.rect.x
        self.position.y = self.rect.y

    def move(self) :
        # Get all keys' statuses
        keys = pygame.key.get_pressed()

        # Cease the player's horizontal movement by default
        self.velocity.x = 0

        # If the player presses the left/A key
        if keys[pygame.K_LEFT] or keys[pygame.K_a] :
            # Move leftward
            self.velocity.x = -self.move_speed

        # If the player presses the right/D key
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] :
            # Move rightward
            self.velocity.x = self.move_speed

    def jump(self) :
        # Get all keys' statuses
        keys = pygame.key.get_pressed()

        # If the player presses the space key and is on the ground
        if keys[pygame.K_SPACE] and self.is_on_ground :
            # Give the player upward velocity
            self.velocity.y = self.jump_height

            # Flag the player as not on the ground
            self.is_on_ground = False

    def check_collision_x(self, grounds) :
        # If the player is touching the left wall
        if self.rect.left < 0 :
            self.rect.left = 0
            self.position.x = self.rect.x
        
        # Go through each ground in the level
        for ground in grounds :
            # If the player is touching the ground
            if self.rect.colliderect(ground) :
                # If the player is moving right
                if self.velocity.x > 0 :
                    self.rect.right = ground.rect.left

                # If the player is moving left
                elif self.velocity.x < 0 :
                    self.rect.left = ground.rect.right

                # Adjust the player's position based on changes to x
                self.position.x = self.rect.x

    def check_collision_y(self, grounds) :
        # Assume the player is not on the ground
        self.is_on_ground = False

        # Go through each ground in the level
        for ground in grounds :
            # If the player is touching the ground
            if self.rect.colliderect(ground) :
                # If the player is moving down
                if self.velocity.y > 0 :
                    self.rect.bottom = ground.rect.top
                    self.velocity.y = 0
                    self.is_on_ground = True

                # If the player is moving up
                elif self.velocity.y < 0 :
                    self.rect.top = ground.rect.bottom
                    self.velocity.y = 0

                # Update position
                self.position.y = self.rect.y

    def move_collide(self, grounds) :
        self.position.x += self.velocity.x
        self.rect.x = round(self.position.x)
        self.check_collision_x(grounds)

        self.position.y += self.velocity.y
        self.rect.y = round(self.position.y)
        self.check_collision_y(grounds)

    def update(self) :
        # Allow the player to move
        self.move()
        self.move_collide(ground_group)

        # Apply gravity to the vertical velocity
        self.velocity += self.gravity

        # Death collision
        if self.rect.bottom >= 1000 :
            print("You fell. Into a hole. How sad.")
            pygame.quit(); sys.exit()

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 255, 255), self.rect) # Update for player assets!

player = Player(ground1)
player_group = pygame.sprite.GroupSingle(player)

# Enemy character assets
class Enemy(pygame.sprite.Sprite) :
    def __init__(self, floor : Ground, x : int) :
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

        # Movement speed and gravity mechanics
        self.move_speed = 3
        self.direction = -1 # Start moving left
        self.is_on_ground = False

        # Floor
        self.floor = floor.rect.top

        # Physics variables
        self.position = pygame.math.Vector2((x, self.floor))
        self.velocity = pygame.math.Vector2()
        self.gravity = pygame.math.Vector2((0, 0.8))

        # Set the center to the ground
        self.rect.midbottom = (x, self.floor)
        self.position.x = self.rect.x
        self.position.y = self.rect.y

    def move(self) :        
        # Set enemy's horizontal velocity
        self.velocity.x = self.move_speed * self.direction # For future implementation of walls

    def check_collision_x(self, grounds) :
        # If the enemy is touching the left wall
        if self.rect.left <= 0 :
            self.rect.left = 0
            self.position.x = self.rect.x
            self.direction = 1 # Change direction to right
        
        # Go through each ground in the level
        for ground in grounds :
            # If the enemy is touching the ground
            if self.rect.colliderect(ground) :
                # If the enemy is moving right
                if self.velocity.x > 0 :
                    self.rect.right = ground.rect.left
                    self.direction = -1 # Change direction to left

                # If the enemy is moving left
                elif self.velocity.x < 0 :
                    self.rect.left = ground.rect.right
                    self.direction = 1 # Change direction to right

                # Adjust the enemy's position based on changes to x
                self.position.x = self.rect.x

    def check_collision_y(self, grounds) :
        # Assume the enemy is not on the ground
        self.is_on_ground = False

        # Go through each ground in the level
        for ground in grounds :
            # If the enemy is touching the ground
            if self.rect.colliderect(ground) :
                # If the enemy is moving down
                if self.velocity.y > 0 :
                    self.rect.bottom = ground.rect.top
                    self.velocity.y = 0
                    self.is_on_ground = True

                # If the enemy is moving up
                elif self.velocity.y < 0 :
                    self.rect.top = ground.rect.bottom
                    self.velocity.y = 0

                # Update position
                self.position.y = self.rect.y

    def move_collide(self, grounds) :
        self.position.x += self.velocity.x
        self.rect.x = round(self.position.x)
        self.check_collision_x(grounds)

        self.position.y += self.velocity.y
        self.rect.y = round(self.position.y)
        self.check_collision_y(grounds)

    def update(self, player : Player) :
        # Make the enemy move
        self.move()
        self.move_collide(ground_group)

        # Vertical adjustment
        self.velocity += self.gravity

        ### IMPORTANT: The enemy's height is defined by the top of its body.
        
        if abs(self.rect.x - player.rect.x) <= self.width and player.rect.y + player.height > self.rect.y and player.rect.y + player.height <= self.rect.y + self.height :
            print("NYEH HEH HEH!") if SystemRandom().randint(0, 99) == 0 else print("As you draw your final breath, you feel it leaking into your brain, stealing away your life just like the others. Was it ever an escape, or was it delaying the inevitable?") # Easter egg
            pygame.quit(); sys.exit()

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 0, 0), self.rect) # Update for enemy assets!

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
