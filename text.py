# Straws
# Text class

# Imports
import pygame

class Text :
    def __init__(self, text : str, pos : tuple[int], size : int = 48) :
        # Specific attributes
        self.text = text
        self.font = "Baloo 2"
        self.size = size
        self.pos = pos

    def get_text(self, color : tuple[int]) -> pygame.Surface :
        font = pygame.font.SysFont(self.font, self.size)
        text_surface = font.render(str(self.text), True, (255, 255, 255))
        return text_surface
