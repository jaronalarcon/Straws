# Straws
# Cutscene screens

# Imports
from background import Background
from buttons import Button
import pygame
from time import sleep

# Screen dimension constants for reference
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

class Cutscene :
    @staticmethod
    def title_screen() -> tuple :
        """ Ayaka made most of the functionality for this screen. """
        # Background image
        bg = Background("lyon_arboretum_bg.png", SCREEN_WIDTH, SCREEN_HEIGHT)

        # Text
        title_font = pygame.font.SysFont("Baloo 2", 80)
        title_text = title_font.render("Straws", True, (46, 121, 43))

        # Button images
        start_img = pygame.image.load("StartButton.png").convert_alpha()
        end_img = pygame.image.load("EndButton.png").convert_alpha()

        # Buttons
        start_button = Button(160, 205, start_img)
        end_button = Button(205, 320, end_img)

        return (bg, title_text, start_button, end_button)

    @staticmethod
    def end_screen(surface, score : int) :
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
        end_text6 = end_font.render(f"Score: {score}", True, (0, 0, 0))

        # Draw text on screen
        surface.blit(end_text1, (SCREEN_WIDTH // 2 - end_text1.get_width() // 2, 100))
        surface.blit(end_text2, (SCREEN_WIDTH // 2 - end_text2.get_width() // 2, 150))
        surface.blit(end_text3, (200, 400))
        surface.blit(end_text4, (500, 450))
        surface.blit(end_text5, (700, 500))
        surface.blit(end_text6, (SCREEN_WIDTH // 2 - end_text6.get_width() // 2, 700))

        # Update the screen to show text
        pygame.display.flip()

        sleep(5) # Pause to let the player read the ending
