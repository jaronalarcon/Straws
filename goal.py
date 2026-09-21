# Straws
# Goal class

# Imports
import pygame

class Goal(pygame.sprite.Sprite) :
    def __init__(self, x : int, y : int) :
        # Call parent class constructor
        pygame.sprite.Sprite.__init__(self)

        # Load image assets
        self.image = pygame.image.load("red-triangular-pennant-flag-on-pole-isolated-on-transparent-background-png.png").convert_alpha() # Replace with actual goalpost assets

        # Resize image
        self.width = 50
        self.height = 50
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Get the collision rectangle
        self.rect = self.image.get_rect()

        # Place the image at the specified coordinates
        self.rect.center = (x, y)

    def draw(self, surface) :
        pygame.draw.rect(surface, (200, 200, 0), self.rect)
