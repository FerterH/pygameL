import pygame
class INFO():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/top1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
    def info_output(self):
        self.screen.blit(self.image, self.rect)
