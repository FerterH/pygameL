import pygame
import sys
from gun import RPG
import controls
from pygame.sprite import Group

def run():
    pygame.init()
    screen = pygame.display.set_mode((1920,1080))   #sizes
    pygame.display.set_caption('Battlefild 6')  #tite
    bg_color = (0, 120, 120)
    gun = RPG(screen)
    bullets = Group()

    while True:
        controls.events(screen, gun, bullets)
        screen.fill(bg_color)
        gun.output()
        gun.update_gun()
        gun.update_gun2()
        controls.update(bg_color, screen, gun, bullets)
        controls.update2(bg_color, screen, gun, bullets)
        controls.delete(bullets)
#        gun.py.mit()

        pygame.display.flip()



run()
