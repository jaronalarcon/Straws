# Straws
# Goal class

# Imports
import pygame

class Goal :
    def __init__(self, x : int, y : int) :
        # Make shape
        self.width = self.height = 50 # Will be a square
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, surface) :
        pygame.draw.rect(surface, (200, 200, 0), self.rect)
