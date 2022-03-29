import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self,screen,gun):

        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,2,12)
        self.color = 255,0, 0
        self.speed = 3
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    def drawBullet2(self):
        pygame.draw.rect2(self.screen, self.color, self.rect2)