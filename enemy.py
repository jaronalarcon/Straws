# Straws
# Enemy class

# Imports
from ground import Ground
from player import Player
import pygame, sys
from random import SystemRandom

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
                # If the enemy is moving down (inverted y-direction)
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
        # Update x position and check for collision
        self.position.x += self.velocity.x
        self.rect.x = round(self.position.x)
        self.check_collision_x(grounds)

        # Update y position and check for collision
        self.position.y += self.velocity.y
        self.rect.y = round(self.position.y)
        self.check_collision_y(grounds)

    def update(self, ground_group, player : Player) :
        # Make the enemy move
        self.move()
        self.move_collide(ground_group)

        # Vertical adjustment
        self.velocity += self.gravity

        ### IMPORTANT: The enemy's height is defined by the top of its body.
        
        # Kill the player if the player character collides with an enemy
        if abs(self.rect.x - player.rect.x) <= self.width and player.rect.y + player.height > self.rect.y and player.rect.y + player.height <= self.rect.y + self.height :
            print("NYEH HEH HEH!") if SystemRandom().randint(0, 99) == 0 else print("As you draw your final breath, you feel it leaking into your brain, stealing away your life just like the others. Was it ever an escape, or was it delaying the inevitable?") # Easter egg
            pygame.quit(); sys.exit()

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 0, 0), self.rect) # Update for enemy assets!
