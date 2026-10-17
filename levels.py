# Straws
# Level sets

# Imports
import pygame
from json import load
from random import SystemRandom
from background import Background
from collectible import Collectible
from enemy import Enemy
from goal import Goal
from ground import Ground
from player import Player
from text import Text

# Screen dimension constants for reference
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

class Level :
    @staticmethod
    def level1() -> tuple :
        """ Introductory level of the demo.
            Based on Waiāhole Beach Park on the island of O‘ahu."""

        # Get information for level
        with open("research.json", "r") as r :
            info = load(r)["waiahole_beach_park"]

        # Background for the level
        background = Background("waiahole_beach_park_bg.png", SCREEN_WIDTH, SCREEN_HEIGHT)

        # Text for the level
        text1 = Text(SystemRandom().choice(info), (2600, 50), color = (0, 0, 0))
        text2 = Text("Hold D to move right!", (300, 700), color = (0, 0, 0))
        text3 = Text("Avoid touching the enemies!", (500, 600))
        text4 = Text("Press SPACE to jump!", (925, 550))
        text5 = Text("Hold A to move left!", (2100, 600))
        text6 = Text("Touch the goal marker to complete the level!", (5100, 600))
        text_group = pygame.sprite.Group(text1, text2, text3, text4, text5, text6)
        
        # Grounds in the level
        ground1 = Ground(800, 50, 400, 750, "waiahole_beach_park_ground.png")
        ground2 = Ground(1100, 50, 1600, 750, "waiahole_beach_park_ground.png")
        ground3 = Ground(400, 50, 1600, 575, "waiahole_beach_park_ground.png")
        ground4 = Ground(400, 50, 2100, 375, "waiahole_beach_park_ground.png")
        ground5 = Ground(1000, 50, 3100, 700, "waiahole_beach_park_ground.png")
        ground6 = Ground(200, 50, 3900, 550, "waiahole_beach_park_ground.png")
        ground7 = Ground(200, 50, 4300, 400, "waiahole_beach_park_ground.png")
        ground8 = Ground(500, 50, 4950, 750, "waiahole_beach_park_ground.png")
        ground_group = pygame.sprite.Group(ground1, ground2, ground3, ground4, ground5, ground6, ground7, ground8)

        # Player in the level
        player = Player(ground1)

        # Enemies in the level
        enemy1 = Enemy(ground1, 400)
        enemy2 = Enemy(ground2, 1600)
        enemy3 = Enemy(ground3, 1900)
        enemy4 = Enemy(ground4, 2100)
        enemy5 = Enemy(ground5, 3400)
        enemy_group = pygame.sprite.Group(enemy1, enemy2, enemy3, enemy4, enemy5)

        # Collectibles in the level
        coin1 = Collectible(650, 725)
        coin2 = Collectible(700, 725)
        coin3 = Collectible(750, 725)
        coin4 = Collectible(1550, 550)
        coin5 = Collectible(1600, 550)
        coin6 = Collectible(1650, 550)
        coin7 = Collectible(1800, 475)
        coin8 = Collectible(1875, 400)
        coin9 = Collectible(2500, 300)
        coin10 = Collectible(2550, 400)
        coin11 = Collectible(2600, 500)
        coin12 = Collectible(2650, 600)
        coin13 = Collectible(2100, 725)
        coin14 = Collectible(2900, 650)
        coin15 = Collectible(3000, 550)
        coin16 = Collectible(3100, 450)
        coin17 = Collectible(3200, 550)
        coin18 = Collectible(3300, 650)
        coin19 = Collectible(3950, 525)
        coin20 = Collectible(4050, 450)
        coin21 = Collectible(4150, 375)
        coin22 = Collectible(4750, 725)
        coin23 = Collectible(4850, 725)
        coin24 = Collectible(4950, 725)
        coin_group = pygame.sprite.Group(coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
                                         coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20,
                                         coin21, coin22, coin23, coin24)

        # Goal in the level
        goalpost = Goal(5100, 700)

        # Return the assets for the level
        return (background, ground_group, player, enemy_group, coin_group, goalpost, text_group) # Tuple suggested by AI

    @staticmethod
    def level2() -> tuple :
        """ Intermediate level of the demo.
            Based on Lyon Arboretum on the island of O‘ahu. """

        # Get information for level
        with open("research.json", "r") as r :
            info = load(r)["lyon_arboretum"]

        # Background for the level
        background = Background("lyon_arboretum_bg.png", SCREEN_WIDTH, SCREEN_HEIGHT)

        # Text for the level
        text1 = Text(SystemRandom().choice(info), (1600, -525), color = (0, 0, 0))
        text_group = pygame.sprite.Group(text1)

        # Grounds in the level
        ground1 = Ground(600, 50, 300, 425)
        ground2 = Ground(600, 50, 1000, 625)
        ground3 = Ground(600, 50, 300, 825)
        ground4 = Ground(400, 50, 1600, 775)
        ground5 = Ground(200, 50, 1050, 0)
        ground6 = Ground(200, 50, 1700, 375)
        ground7 = Ground(200, 50, 1400, 175)
        ground8 = Ground(100, 50, 400, -25)
        ground9 = Ground(100, 50, 1425, -125)
        ground10 = Ground(200, 50, 1825, -105)
        ground11 = Ground(100, 50, 700, 0)
        ground12 = Ground(400, 50, 2100, 575)
        ground_group = pygame.sprite.Group(ground1, ground2, ground3, ground4, ground5, ground6, ground7, ground8, ground9, ground10,
                                           ground11, ground12)

        # Player in the level
        player = Player(ground1)

        # Enemies in the level
        enemy1 = Enemy(ground1, 400)
        enemy2 = Enemy(ground3, 400)
        enemy3 = Enemy(ground2, 1200)
        enemy4 = Enemy(ground8, 2100)
        enemy5 = Enemy(ground6, 1800)
        enemy6 = Enemy(ground7, 1500)
        enemy7 = Enemy(ground5, 1100)
        enemy8 = Enemy(ground10, 1900)
        enemy_group = pygame.sprite.Group(enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8)

        # Collectibles in the level
        coin1 = Collectible(550, 400)
        coin2 = Collectible(200, 700)
        coin3 = Collectible(300, 700)
        coin4 = Collectible(400, 700)
        coin5 = Collectible(200, 750)
        coin6 = Collectible(300, 750)
        coin7 = Collectible(400, 750)
        coin8 = Collectible(200, 800)
        coin9 = Collectible(300, 800)
        coin10 = Collectible(400, 800)
        coin11 = Collectible(900, 600)
        coin12 = Collectible(1000, 600)
        coin13 = Collectible(1100, 600)
        coin14 = Collectible(1500, 750)
        coin15 = Collectible(1600, 750)
        coin16 = Collectible(1700, 750)
        coin17 = Collectible(2200, 550)
        coin18 = Collectible(1700, 350)
        coin19 = Collectible(1400, 150)
        coin20 = Collectible(1000, -25)
        coin21 = Collectible(1100, -25)
        coin22 = Collectible(1425, -150)
        coin23 = Collectible(1425, -200)
        coin24 = Collectible(1425, -250)
        coin25 = Collectible(1800, -130)
        coin26 = Collectible(1875, -130)
        coin_group = pygame.sprite.Group(coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
                                         coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20,
                                         coin21, coin22, coin23, coin24, coin25, coin26)

        # Goal in the level
        goalpost = Goal(400, -75)

        # Return the assets for the level
        return (background, ground_group, player, enemy_group, coin_group, goalpost, text_group)

    @staticmethod
    def level3() -> tuple :
        """ Final level of the demo.
            Based on Kapolei on the island of O‘ahu. """

        # Get information for level
        with open("research.json", "r") as r :
            info = load(r)["kapolei"]

        # Background for the level
        background = Background("kapolei_bg.png", SCREEN_WIDTH, SCREEN_HEIGHT)

        # Text for the level
        text1 = Text(SystemRandom().choice(info), (3000, 200), color = (0, 0, 0))
        text_group = pygame.sprite.Group(text1)

        # Grounds in the level
        ground1 = Ground(900, 50, 450, 100, "kapolei_ground.png") # x: 0 - 900
        ground2 = Ground(600, 50, 1300, 250, "kapolei_ground.png") # x: 1000 - 1600
        ground3 = Ground(500, 50, 1950, 400, "kapolei_ground.png") # x: 1700 - 2200
        ground4 = Ground(200, 50, 2500, 400, "kapolei_ground.png") # x: 2400 - 2600
        # Floating islands
        ground5 = Ground(50, 50, 2825, 450, "kapolei_ground.png") # x: 2800 - 2850
        ground6 = Ground(50, 50, 3075, 500, "kapolei_ground.png") # x: 3050 - 3100
        ground7 = Ground(50, 50, 3325, 550, "kapolei_ground.png") # x: 3300 - 3350
        ground8 = Ground(50, 50, 3575, 600, "kapolei_ground.png") # x: 3550 - 3600
        # Final goal
        ground9 = Ground(400, 50, 4050, 800, "kapolei_ground.png") # x: 3850 - 4250
        ground_group = pygame.sprite.Group(ground1, ground2, ground3, ground4, ground5, ground6, ground7, ground8, ground9)

        # Player in the level
        player = Player(ground1)

        # Enemies in the level
        enemy1 = Enemy(ground1, 400)
        enemy2 = Enemy(ground1, 600)
        enemy3 = Enemy(ground1, 800)
        enemy4 = Enemy(ground2, 1500)
        enemy5 = Enemy(ground2, 1600)
        enemy6 = Enemy(ground3, 2200)
        enemy7 = Enemy(ground4, 2600)
        enemy8 = Enemy(ground9, 4250)
        enemy_group = pygame.sprite.Group(enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8)

        # Collectibles in the level
        coin1 = Collectible(725, 75)
        coin2 = Collectible(1200, 225)
        coin3 = Collectible(1300, 225)
        coin4 = Collectible(1400, 225)
        coin5 = Collectible(2450, 375)
        coin6 = Collectible(2550, 375)
        coin7 = Collectible(2500, 375)
        coin8 = Collectible(2825, 425)
        coin9 = Collectible(3075, 475)
        coin10 = Collectible(3325, 525)
        coin11 = Collectible(3575, 575)
        # Coin arch
        coin12 = Collectible(3650, 450)
        coin13 = Collectible(3710, 425)
        coin14 = Collectible(3770, 475)
        coin15 = Collectible(3830, 525)
        coin16 = Collectible(3890, 625)
        coin_group = pygame.sprite.Group(coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
                                         coin11, coin12, coin13, coin14, coin15, coin16)

        # Goal in the level
        goalpost = Goal(4050, 750)

        # Return the assets for the level
        return (background, ground_group, player, enemy_group, coin_group, goalpost, text_group)

    @staticmethod
    def get_all_levels() :
        # Return all of the level methods
        return [Level.level1, Level.level2, Level.level3] # AI suggested returning the methods
                                                          # rather than method calls
