import pygame
from projectile import Projectile
#Classe du vaiseau du joueur
class Spaceship(pygame.sprite.Sprite):

    
    def __init__(self, game, max_hp, velocity, attack):
        super().__init__()
        self.game = game
        self.hp = max_hp
        self.max_hp = max_hp
        self.velocity = velocity
        self.attack = attack
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('PygameAssets/Spaceship2.png')
        self.image = pygame.transform.scale(self.image, (200, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

    def launch_projectile(self):
        self.all_projectile.add(Projectile(self))
                    
    def get_health(hp, max_hp, heal):
        if hp+heal <= max_hp:
            hp += heal
        else:
            hp = max_hp 

    def damage(self, amount):
        if (self.health - amount > amount) :
            self.health -= amount
        else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()

    
    def move_right(self):

        #si le joueur n'est pas en collision avec les monstres
        if not self.game.check_collision(self, self.game.all_enemy):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
    
    def move_down(self):
        self.rect.y += self.velocity

    def move_up(self):
        self.rect.y -= self.velocity