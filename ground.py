# Straws
# Ground class

# Imports
import pygame

class Ground(pygame.sprite.Sprite) :
    def __init__(self, width : int, height : int, x : int, y : int,
                 image : str = "lyon_arboretum_ground.png") :
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)

        # Load image assets for ground
        self.image = pygame.image.load(image).convert_alpha() # Filler image is Lyon Arboretum ground

        # Resize the image
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, 0) # Rotate the image if necessary
                                                            # Must only be used with properly implemented Rect objects

        # Get the rectangle of the image for collision detection
        self.rect = self.image.get_rect()

        # Place the ground at the bottom of the screen
        self.rect.center = (x, y) # Therefore, left edge = x - (width // 2)
                                  #            right edge = x + (width // 2)

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
