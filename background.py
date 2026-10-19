# Straws
# Background class

# Imports
import pygame

class Background : # This class is the only non-subclass because it
                   # requires screen coordinates, not game coordinates
    def __init__(self, file : str, width : int, height : int) :
        # Retrieve background image
        self.image = pygame.image.load(file).convert_alpha()

        # Scale background image to screen dimensions
        self.image = pygame.transform.scale(self.image, (width, height))
