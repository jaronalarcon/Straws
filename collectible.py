# Straws
# Collectible class

# Imports
import pygame

class Collectible(pygame.sprite.Sprite) :
    def __init__(self, x : int, y : int) :
        # Call the parent class constructor
        super().__init__()

        # Load image assets
        self.image = pygame.image.load("hd-soda-bottle-yellow-lid-crown-cap-png-704081695126642ekq0ebhace.png").convert_alpha()
        self.show_image = True

        # Resize the image
        self.width = 40
        self.height = 40
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Generate the collision shape of the image
        self.rect = self.image.get_rect()

        # Set the center to the ground
        self.rect.midbottom = (x, y)

    def update(self) :
        pass

    def draw(self, surface) :
        # Show image while on screen
        if self.show_image :
            pygame.draw.rect(surface, (255, 0, 0), self.rect)
