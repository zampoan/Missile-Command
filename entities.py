import pygame
import random

RESIZE_FACTOR = 0.7

class City(pygame.sprite.Sprite):
    def __init__(self, imgPath, x, y):
        super().__init__()

        image = pygame.image.load(imgPath)

        # Get the image width and height
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * RESIZE_FACTOR), int(height * RESIZE_FACTOR)))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass


class EnemyMissile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        spriteList = ['missile-command-assets/2D/missile_small.png',
                      'missile-command-assets/2D/missile_medium.png',
                      'missile-command-assets/2D/missile_large.png']

        # select random choice 
        image = pygame.image.load(random.choice(spriteList))

        # Get the image width and height
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * RESIZE_FACTOR), int(height * RESIZE_FACTOR)))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        pass

class PlayerMissile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # select random choice 
        image = pygame.image.load('missile-command-assets/2D/anti_missile.png')

        # Get the image width and height
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * RESIZE_FACTOR), int(height * RESIZE_FACTOR)))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y -= 1
        # pass


        


