import pygame


class Bullet2(pygame.sprite.Sprite):

    def __init__(self,screen,gun):

        super(Bullet2, self).__init__()
        self.screen = screen
        self.rect2 = pygame.Rect(0,0,2,13)
        self.color = 255,0, 0
        self.speed = 3
        self.rect2.centerx = gun.rect2.centerx
        self.rect2.top = gun.rect2.top
        self.y = float(self.rect2.y)

    def update2(self):
        self.y -= self.speed
        self.rect2.y = self.y

    def drawBullet2(self):
        pygame.draw.rect2(self.screen, self.color, self.rect2)
