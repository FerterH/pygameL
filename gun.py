import pygame
import time

class RPG():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/army.png')
        self.image2 = pygame.image.load('images/megaknite.png')
        self.rect = self.image.get_rect()
        self.rect2 = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.screen_rect2 = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect2.centerx = self.screen_rect.centerx
        self.rect2.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom  # bottom
        self.rect2.bottom = self.screen_rect.bottom  # bottom2

        self.keyUP_a = False
        self.keyUP_w = False
        self.keyUP_d = False
        self.keyUP_s = False

        self.keyUP_left = False
        self.keyUP_up = False
        self.keyUP_right = False
        self.keyUP_down = False
        self.timer = 0
        self.keyUP_f = 0

            #вывод
    def output(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect2)





            #движение
    def update_gun(self):
        if self.keyUP_a == True:
            self.rect.centerx -=1
            if self.rect.centerx<1:
                self.rect.centerx += 1
        elif self.keyUP_d == True:
            self.rect.centerx +=1
            if self.rect.centerx>1920:
                self.rect.centerx -= 2
        elif self.keyUP_w == True:
            self.rect.centery -=1
            if self.rect.centery<1:
                self.rect.centery += 1
        elif self.keyUP_s == True:
            self.rect.centery +=1
            if self.rect.centery>1080:
                self.rect.centery -= 1

    def update_gun2(self):
        if self.keyUP_left == True:
            self.rect2.centerx -=1
            if self.rect2.centerx<1:
                for i in range(300):
                    self.rect2.centerx += 1
        elif self.keyUP_right == True:
            self.rect2.centerx +=1
            if self.rect2.centerx>1920:
                for i in range(50):
                    self.rect2.centerx -= 1
        elif self.keyUP_up == True:
            self.rect2.centery -=1
            if self.rect2.centery<1:
                for i in range(150):
                    self.rect2.centery += 1
        elif self.keyUP_down == True:
            self.rect2.centery +=1
            if self.rect2.centery>1080:
                for i in range(50):
                    self.rect2.centery -= 1



 #   def mit(self):
  #      if self.rect.centery == self.rect2.centery:
   #         self.rect.centery += 1
    #        self.rect2.centery += 2
     #   elif self.rect2.centerx == self.rect.centerx:
      #      self.rect2.centerx -= 2
       #     self.rect.centerx -= 1
        #if self.rect.centery == self.rect2.centery:
         #   self.rect.centery -= 1
          #  self.rect2.centery -= 2
        #elif self.rect2.centerx == self.rect.centerx:
         #   self.rect2.centerx -= 2
          #  self.rect.centerx -= 1
