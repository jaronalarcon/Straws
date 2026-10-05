# Straws
# Background class

import pygame

class Background :
    def __init__(self, file : str, width : int, height : int) :
        # Retrieve background image
        self.image = pygame.image.load(file).convert_alpha()

        # Scale background image to screen dimensions
        self.image = pygame.transform.scale(self.image, (width, height))
