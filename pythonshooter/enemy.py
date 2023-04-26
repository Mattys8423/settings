# #Classe des ennemis
# class Enemy:
#     def __init__(self,pv_max,speed):
#         self.pv = pv_max
#         self.max_pv = pv_max
#         self.speed = speed

#     def get_health(pv, damage):
#         if pv-damage >0:
#             pv = pv - damage
#         else:
#             pv = 0
    

import pygame

#Classe des ennemis
class Enemy(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.pv = 100
        self.speed = 2
        self.max_pv = 100
        self.attack = 5
        self.image = pygame.image.load('PygameAssets/button-settings.png')
        # self.image = pygame.transform.scale(self.image, (1200,1200))
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()

        self.rect.x = 1900
        self.rect.y = 500

        self.origine_image = self.image
        self.angle = 0

    def remove(self):
        self.game.all_enemy.remove(self)

    def rotation(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def forward(self):
        self.rotation()
        #le deplacement s'arrete si collision
        if self.game.check_collision(self, self.game.all_players):
            self.remove()
        else:
            self.rect.x -= self.speed