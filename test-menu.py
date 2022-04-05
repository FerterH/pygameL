import pygame
# import main
import sys
import pygame
import sys
from gun import RPG
import controls
from pygame.sprite import Group
from  bullet import Bullet
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

# rendering a text written in
# this font
text = smallfont.render('Start', True, color)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
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
                        # showdown()
                        # print(bullet.speed)

                        # if gun.rect2.centery == bullet.Bullet.rect.centery and gun.rect2.centerx == bullet.Bullet.rect.centerx:
                        #     print('ПОПАЛ')


                run()


                # fills the screen with a color
    bg =
    screen.blit()

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

        # superimposing the text onto our button
    screen.blit(text, (width / 2 + 50, height / 2))

    # updates the frames of the game
    pygame.display.update()