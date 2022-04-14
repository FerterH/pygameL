# import main
import sys
import pygame
import time
from gun import RPG
import goEvil
from pygame.sprite import Group
from bullet import Bullet
from about import INFO
pygame.init()
res = (800, 600)
screen = pygame.display.set_mode(res)
# white color
color = (255, 255, 255)
# light shade of the button
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (100, 100, 100)
# stores the width of the
# screen into a variable
width = screen.get_width()
# stores the height of the
# screen into a variable
height = screen.get_height()
# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)
smallfont2 = pygame.font.SysFont('Corbel', 32)
# rendering a text written in
# this font
text = smallfont.render('Start', True, color)
text2 = smallfont2.render('Quit', True, color)
text3 = smallfont2.render('О разработчике', True, color)

def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # sizes
    pygame.display.set_caption('Battlefild 6')  # tite
    bg_color = (0, 120, 120)
    gun = RPG(screen)
    bullets = Group()
    bg = pygame.image.load('images/back.png')
    rect = bg.get_rect()
    screen_rect = screen.get_rect()
    pygame.mixer.music.load('sounds/music.mp3')
    pygame.mixer.music.play(0)
    while True:
        bullX = Bullet(screen, gun)
        bullY = Bullet(screen, gun)

        print('пуля х', bullY.update())
        print('пуля y', bullY.update_y())
        if bullX.update() == bullY.update_y():
            print('----------------------------------------')

        screen.blit(bg, rect)
        goEvil.events(screen, gun, bullets)
        # screen.fill(bg_color)
        gun.output()
        gun.update_gun()
        gun.update_gun2()
        goEvil.update(bg_color, screen, gun, bullets)
        #goEvil.update2(bg_color, screen, gun, bullets)
        goEvil.delete(bullets)
        pygame.display.flip()
while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if 277 <= mouse[0] <= 521 and 231 <= mouse[1] <= 231 + 32:
                run()
            if 404 <= mouse[0] <= 521 and 374 <= mouse[1] <= 399:
                pygame.quit()
            if 277 <= mouse[0] <= 521 and 312 <= mouse[1] <= 399:
                print('ошибки, ошибки!, ОШИБКИ!!!')

                # about = INFO(screen)
                # INFO.info_output()
    bg = pygame.image.load('images/mine.png')
    rect = bg.get_rect()
    screen.blit(bg, rect)

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if 277 <= mouse[0] <=521 and 231 <= mouse[1] <= 259:

        pygame.draw.rect(screen, color_light, [276,  231, 248, 32])
        pygame.mixer.music.load('sounds/click.mp3')
        pygame.mixer.music.play(0)
        time.sleep(0.1)
    else:

        pygame.draw.rect(screen, color_dark, [276, 231, 248, 32])

    if 404 <= mouse[0] <= 521 and 374 <= mouse[1] <= 399:
        pygame.draw.rect(screen, color_light, [404, 374, 120, 28])

    else:
        pygame.mixer.music.load('sounds/click.mp3')
        pygame.mixer.music.play(0)
        pygame.draw.rect(screen, color_dark, [404, 374, 120, 28])
    if 277 <= mouse[0] <= 521 and 311 <= mouse[1] <= 340:

        pygame.draw.rect(screen, color_light, [276, 311, 248, 32])
        pygame.mixer.music.load('sounds/click.mp3')
        pygame.mixer.music.play(0)
        time.sleep(0.1)
    else:

        pygame.draw.rect(screen, color_dark, [276, 311, 248, 32])
        # superimposing the text onto our button
    screen.blit(text, (360, 230))
    screen.blit(text2, (430, 375))
    screen.blit(text3, (290, 312))

    print('x',mouse[0])
    print('y', mouse[1])
    # updates the frames of the game
    pygame.display.update()