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
    def level1() -> list :
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
        coin_group = pygame.sprite.Group(coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12)

        # Goal in the level
        goalpost = Goal(3150, 500)

        # Return the assets for the level
        return [ground_group, player, enemy_group, coin_group, goalpost]

    @staticmethod
    def level2() -> list :
        # Grounds in the level
        ground1 = Ground(800, 50, 400, 350)
        ground2 = Ground(800, 50, 800, 500)
        ground_group = pygame.sprite.Sprite(ground1, ground2)

        # Player in the level
        player = Player(ground1)

        # Enemies in the level
        enemy1 = Enemy(ground1, 400)
        enemy_group = pygame.sprite.Ground(enemy1)

        # Collectibles in the level
        coin1 = Collectible(650, 325)
        coin_group = pygame.sprite.Group(coin1)

        # Goal in the level
        goalpost = Goal(1000, 100)

        # Return the assets for the level
        return [ground_group, player, enemy_group, coin_group, goalpost]

    @staticmethod
    def get_all_levels() :
        return [Level.level2()]
