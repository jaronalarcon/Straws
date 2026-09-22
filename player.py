# Straws
# Player class

# Imports
from ground import Ground
from random import SystemRandom
import pygame, sys

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

        # Physics variables (implemented with the help of AI)
        self.position = pygame.math.Vector2((50, self.floor))
        self.velocity = pygame.math.Vector2()
        self.gravity = pygame.math.Vector2((0, 0.8))

        # Set the center to the ground
        self.rect.midbottom = (50, self.floor)
        self.position.x = self.rect.x
        self.position.y = self.rect.y

        # Score
        self.score = 0

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
        """ Horizontal velocity collision detection.
            Written with the help of AI. """
        # If the player is touching the left wall
        if self.rect.left < 0 :
            self.rect.left = 0
            self.position.x = self.rect.x
        
        # Go through each ground in the level
        for ground in grounds :
            # If the player is touching the ground
            if self.rect.colliderect(ground.rect) :
                # If the player is moving right
                if self.velocity.x > 0 :
                    self.rect.right = ground.rect.left

                # If the player is moving left
                elif self.velocity.x < 0 :
                    self.rect.left = ground.rect.right

                # Adjust the player's position based on changes to x
                self.position.x = self.rect.x

    def check_collision_y(self, grounds) :
        """ Vertical velocity collision detection.
            Written with the help of AI. """
        # Assume the player is not on the ground
        self.is_on_ground = False

        # Go through each ground in the level
        for ground in grounds :
            # If the player is touching the ground
            if self.rect.colliderect(ground.rect) :
                # If the player is moving down (inverted y-direction)
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
        # Update x position and check for collision
        self.position.x += self.velocity.x
        self.rect.x = round(self.position.x)
        self.check_collision_x(grounds)

        # Update y position and check for collision
        self.position.y += self.velocity.y
        self.rect.y = round(self.position.y)
        self.check_collision_y(grounds)

    def update(self, ground_group) :
        # Player movement
        self.move()
        self.move_collide(ground_group)

        # Apply gravity to the vertical velocity
        self.velocity += self.gravity

        # Death collision
        if self.rect.bottom >= 1000 :
            print("You fell. Into a hole. How sad.\n") if SystemRandom().randint(0, 9) >= 1 else print("You hear her whisper in your ear: Come on, get up! They're waiting for you!")
            pygame.quit(); sys.exit()

    def set_score(self, amount : int) -> None :
        """ Method to set former player's score to this player's score
            to ensure the user's points remain consistent between each
            level. """

        self.score = amount

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 255, 255), self.rect) # Update for player assets!
