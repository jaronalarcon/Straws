# Straws
# Text class

# Imports
import pygame

class Text(pygame.sprite.Sprite) :
    def __init__(self, text : str, pos : tuple[int],
                 font : str = "Baloo 2", size : int = 24, color : tuple[int] = (255, 255, 255)) :
        # ChatGPT suggested condensing each of the necessary attributes into the constructor for camera manipulation
        # I previously tried to refactor this class to be a subclass of pygame.sprite.Sprite, but I overlooked some details.

        # Call the parent class constructor
        super().__init__()

        # Specific attributes
        self.text = text
        self.font = font
        self.size = size
        self.color = color

        # Create the text surface
        font = pygame.font.SysFont(self.font, self.size)
        self.image = font.render(str(self.text), True, self.color)

        # Create the position rectangle
        self.rect = self.image.get_rect(center = pos)
