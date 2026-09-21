# Straws
# Goal class

# Imports
import pygame

class Goal :
    def __init__(self) :
        # This is the only asset that can be made out of pygame.Rect

        # Make shape
        self.rect = pygame.Rect()

    def draw(self, surface) :
        pygame.draw.rect(surface, (200, 200, 0), self.rect)
