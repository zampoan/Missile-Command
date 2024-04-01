import pygame

class City(pygame.sprite.Sprite):
    def __init__(self, imgPath):
        super().__init__()

        self.img = pygame.image.load(imgPath)
        self.rect = self.img.get_rect()



