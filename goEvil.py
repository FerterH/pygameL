import sys
import pygame

from bullet import Bullet

from random import randint



def events(screen,gun, bullets):
    # управление случайными числами 2м героем
    random_number = randint(1, 20)
    if random_number > 17 and random_number < 20:
        gun.kright2 = True
    elif random_number > 15 and random_number < 17:
        gun.kleft2 = True
    elif random_number > 12 and random_number < 15:
        gun.kup2 = True
    elif random_number > 10 and random_number < 12:
        gun.kdown2 = True

    elif random_number > 7 and random_number < 10:
        gun.kright2 = False
    elif random_number > 5 and random_number < 7:
        gun.kleft2 = False
    elif random_number > 3 and random_number < 5:
        gun.kup2 = False
    elif random_number > 0 and random_number < 3:
        gun.kdown2 = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.kright = True
            elif event.key == pygame.K_a:
                gun.kleft = True
            elif event.key == pygame.K_w:
                gun.kup = True
            elif event.key == pygame.K_s:
                gun.kdown = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_d:
                gun.kright = False
            elif event.key == pygame.K_a:
                gun.kleft = False
            elif event.key == pygame.K_w:
                gun.kup = False
            elif event.key == pygame.K_s:
                gun.kdown = False



def update(bg_color, screen, gun, bullets):
    #screen.fill(bg_color)
    #screen.blit(bg_color, rect5)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    gun.output()
    pygame.display.flip()

def delete(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))import sys
import pygame
from bullet import Bullet

from random import randint



def events(screen,gun, bullets):
    music = pygame.mixer.Sound('sounds/steps.mp3')
    pew = pygame.mixer.Sound('sounds/pew2.mp3')

    # управление случайными числами 2м героем
    random_number = randint(0, 20)
    if random_number >= 16 and random_number <= 20:
        gun.keyUP_right = True
    elif random_number >= 15 and random_number < 17:
        gun.keyUP_left = True
    elif random_number > 12 and random_number < 15:
        gun.keyUP_up = True
    elif random_number >= 10 and random_number < 12:
        gun.keyUP_down = True

    elif random_number > 7 and random_number < 10:
        gun.keyUP_right = False
    elif random_number > 5 and random_number < 7:
        gun.keyUP_left = False
    elif random_number > 3 and random_number < 5:
        gun.keyUP_up = False
    elif random_number > 0 and random_number < 3:
        gun.keyUP_down = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.keyUP_d = True
                music.play()

            elif event.key == pygame.K_a:
                gun.keyUP_a = True
                music.play()
            elif event.key == pygame.K_w:
                gun.keyUP_w = True
                music.play()
            elif event.key == pygame.K_s:
                gun.keyUP_s = True
                music.play()

            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
                pew.play()
        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_d:
                gun.keyUP_d = False
            elif event.key == pygame.K_a:
                gun.keyUP_a = False
            elif event.key == pygame.K_w:
                gun.keyUP_w = False
            elif event.key == pygame.K_s:
                gun.keyUP_s = False



def update(bg_color, screen, gun, bullets):
    #screen.fill(bg_color)
    #screen.blit(bg_color, rect5)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    gun.output()
    pygame.display.flip()

def delete(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))