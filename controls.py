import pygame
import sys
from bullet import Bullet
from bullet2 import Bullet2

def events(screen,gun,bullets):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    gun.keyUP_a = True
                    pygame.mixer.music.load('sounds/steps.mp3')
                    pygame.mixer.music.play(0)
                elif event.key == pygame.K_w:
                    gun.keyUP_w = True
                    pygame.mixer.music.load('sounds/steps.mp3')
                    pygame.mixer.music.play(0)
                elif event.key == pygame.K_s:
                    gun.keyUP_s = True
                    pygame.mixer.music.load('sounds/steps.mp3')
                    pygame.mixer.music.play(0)
                elif event.key == pygame.K_d:
                    gun.keyUP_d = True
                    pygame.mixer.music.load('sounds/steps.mp3')
                    pygame.mixer.music.play(0)
                elif event.key == pygame.K_UP:
                    gun.keyUP_up = True
                    pygame.mixer.music.load('sounds/STEPS2.mp3')
                    pygame.mixer.music.play(0)
                elif event.key == pygame.K_x:
                    gun.keyUP_x = True
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.load('sounds/hee.mp3')
                    pygame.mixer.music.play(0)
                    pygame.mixer.music.set_volume(1)

                elif event.key == pygame.K_DOWN:
                    gun.keyUP_down = True
                    pygame.mixer.music.load('sounds/STEPS2.mp3')
                    pygame.mixer.music.play(0)
                elif event.key == pygame.K_LEFT:
                    gun.keyUP_left = True
                    pygame.mixer.music.load('sounds/STEPS2.mp3')
                    pygame.mixer.music.play(0)
                elif event.key == pygame.K_RIGHT:
                    gun.keyUP_right = True
                    pygame.mixer.music.load('sounds/STEPS2.mp3')
                    pygame.mixer.music.play(0)
                elif event.key == pygame.K_f:
                    gun.keyUP_f = 1
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen,gun)
                    bullets.add(new_bullet)
                    pygame.mixer.music.load('sounds/pew2.mp3')
                    pygame.mixer.music.play(0,)


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    gun.keyUP_a = False
                elif event.key == pygame.K_s:
                    gun.keyUP_s = False
                elif event.key == pygame.K_d:
                    gun.keyUP_d = False
                elif event.key == pygame.K_w:
                    gun.keyUP_w = False
                elif event.key == pygame.K_x:
                    gun.keyUP_x = False
                elif event.key == pygame.K_UP:
                    gun.keyUP_up = False
                elif event.key == pygame.K_DOWN:
                    gun.keyUP_down = False
                elif event.key == pygame.K_LEFT:
                    gun.keyUP_left = False
                elif event.key == pygame.K_RIGHT:
                    gun.keyUP_right = False
                # elif event.key == pygame.K_f:
                #     gun.keyUP_f = 0
                elif event.key == pygame.K_e:
                    new_bullet2 = Bullet2(screen,gun)
                    bullets.add(new_bullet2)


def update(bg_color, screen, gun, bullets):
    # screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    gun.output()
    pygame.display.flip()




def update2(bg_color, screen, gun, bullets):
    # screen.fill(bg_color)
    for bullet2 in bullets.sprites():
        bullet2.drawBullet()
    gun.output()
    pygame.display.flip()


def delete(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

