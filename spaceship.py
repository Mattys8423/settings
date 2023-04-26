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


    def update_health_bar(self, surface):
        #definir la couleur de la jauge de vie
        bar_color = (0, 255, 0) #vert
        #definir une couleur pour l'arriere plan de la jauge
        back_bar_color = (60, 60, 60)

        #definir la position de la jauge de vie + largeur+ epaisseur
        hp = (self.hp / self.max_hp) * 200
        bar_position = [self.rect.x, self.rect.y - 20, hp, 10]
        #definir la positiond e l'arrere plan de la jauge
        back_bar_position = [self.rect.x, self.rect.y - 20, 200, 10]

        #dessine la bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)



    def launch_projectile(self):
        self.all_projectile.add(Projectile(self))
                    
    def get_health(hp, max_hp, heal):
        if hp+heal <= max_hp:
            hp += heal
        else:
            hp = max_hp 

    def damage(self, amount):
        if (self.hp - amount <= 0) :
            #si le joueur n'a plus de point de vie
            self.game.game_over()
        else:
            self.hp -= amount
            
            

    
    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
    
    def move_down(self):
        self.rect.y += self.velocity

    def move_up(self):
        self.rect.y -= self.velocity