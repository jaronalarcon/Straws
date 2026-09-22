# Straws
# Level sets

# Imports
import pygame
from collectible import Collectible
from enemy import Enemy
from goal import Goal
from ground import Ground
from player import Player

class Level :
    @staticmethod
    def level1() -> tuple :
        # Grounds in the level
        ground1 = Ground(800, 50, 400, 750)
        ground2 = Ground(1100, 50, 1600, 750)
        ground3 = Ground(400, 50, 1600, 575)
        ground4 = Ground(400, 50, 2100, 375)
        ground5 = Ground(1000, 50, 3100, 700)
        ground_group = pygame.sprite.Group(ground1, ground2, ground3, ground4, ground5)

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
        coin_group = pygame.sprite.Group(coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
                                         coin11, coin12)

        # Goal in the level
        goalpost = Goal(3150, 500)

        # Return the assets for the level
        return (ground_group, player, enemy_group, coin_group, goalpost)

    @staticmethod
    def level2() -> tuple :
        # Grounds in the level
        ground1 = Ground(600, 50, 300, 425)
        ground2 = Ground(600, 50, 1000, 625)
        ground3 = Ground(600, 50, 300, 825)
        ground4 = Ground(400, 50, 1600, 775)
        ground5 = Ground(400, 50, 2100, 575)
        ground6 = Ground(200, 50, 1700, 375)
        ground7 = Ground(200, 50, 1400, 175)
        ground8 = Ground(200, 50, 1050, 0)
        ground_group = pygame.sprite.Group(ground1, ground2, ground3, ground4, ground5, ground6, ground7, ground8)

        # Player in the level
        player = Player(ground1)

        # Enemies in the level
        enemy1 = Enemy(ground1, 400)
        enemy2 = Enemy(ground3, 400)
        enemy3 = Enemy(ground2, 1200)
        enemy4 = Enemy(ground5, 2100)
        enemy5 = Enemy(ground6, 1800)
        enemy6 = Enemy(ground7, 1500)
        enemy7 = Enemy(ground8, 1100)
        enemy_group = pygame.sprite.Group(enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7)

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
        coin_group = pygame.sprite.Group(coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
                                         coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19)

        # Goal in the level
        goalpost = Goal(1100, -75)

        # Return the assets for the level
        return (ground_group, player, enemy_group, coin_group, goalpost)

    @staticmethod
    def get_all_levels() :
        return [Level.level1, Level.level2]
