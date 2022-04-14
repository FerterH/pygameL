import pygame
import gun



class Bullet(pygame.sprite.Sprite):

    def __init__(self,screen,gun):

        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,2,10)
        self.color = 255,0, 0
        self.speed = 3
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

        #print('пуля x', self.rect.x)


        #print('пуля у', self.rect.y)
        return self.rect.y
    def update_y(self):
        self.rect.x = self.x
        return self.rect.y

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    def drawBullet2(self):
        pygame.draw.rect2(self.screen, self.color, self.rect2)
    # def target(self):
    #     if gun.rect2.centery == self.rect.centery and gun.rect2.centerx == self.rect.centerx:
    #         print('ПОПАЛ')