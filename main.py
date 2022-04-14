import pygame
import sys
from gun import RPG
import controls
from pygame.sprite import Group
from  bullet import Bullet
def showdown():
    screen = pygame.display.set_mode((800, 600))
    gun = RPG(screen)
    bullY = Bullet(screen,gun)
    print('пуля х',bullY.update())
    # print('x:', gun.rect.centerx)
    # print('y:', gun.rect.centery)
    # print('x2:', gun.rect2.centerx)
    # print('y2:', gun.rect2.centery)
    #if gun.rect.centerx == gun.rect2.centerx and gun.rect.centery == gun.rect2.centery:
        #print('oops')


def run():
    pygame.init()
    screen = pygame.display.set_mode((800,600))   #sizes
    pygame.display.set_caption('Battlefild 6')  #tite
    bg_color = (0, 120, 120)
    gun = RPG(screen)
    bullets = Group()
    bg = pygame.image.load('images/back.png')
    rect = bg.get_rect()
    screen_rect = screen.get_rect()

    while True:
        screen.blit(bg, rect)
        controls.events(screen, gun, bullets)
        # screen.fill(bg_color)
        gun.output()
        gun.update_gun()
        gun.update_gun2()
        controls.update(bg_color, screen, gun, bullets)
        controls.update2(bg_color, screen, gun, bullets)
        controls.delete(bullets)
#        gun.py.mit()
        pygame.display.flip()
        showdown()
        # print(bullet.speed)

        # if gun.rect2.centery == bullet.Bullet.rect.centery and gun.rect2.centerx == bullet.Bullet.rect.centerx:
        #     print('ПОПАЛ')



run()
