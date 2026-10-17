# Straws
# Cutscene screens

# Imports
import pygame
from time import sleep

# Screen dimension constants for reference
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

class Cutscene :
    @staticmethod
    def title_screen(surface) :
        pass
    
    @staticmethod
    def end_screen(surface) :
        # Clear screen
        surface.fill((255, 255, 255))
        pygame.display.flip()

        # Font and text to display
        end_font = pygame.font.SysFont("Baloo 2", 36)
        end_text1 = end_font.render("As the sun sets on the final day, you close your eyes", True, (0, 0, 0))
        end_text2 = end_font.render("and let yourself be embraced by the land.", True, (0, 0, 0))
        end_text3 = end_font.render("The world which you were once promised,", True, (0, 0, 0))
        end_text4 = end_font.render("some world once forsaken,", True, (0, 0, 0))
        end_text5 = end_font.render("is now a world reborn.", True, (0, 0, 0))

        # Draw text on screen
        surface.blit(end_text1, (SCREEN_WIDTH // 2 - end_text1.get_width() // 2, 100))
        surface.blit(end_text2, (SCREEN_WIDTH // 2 - end_text2.get_width() // 2, 150))
        surface.blit(end_text3, (200, 400))
        surface.blit(end_text4, (500, 450))
        surface.blit(end_text5, (700, 500))

        # Update the screen to show text
        pygame.display.flip()

        sleep(5) # Pause to let the player read the ending
