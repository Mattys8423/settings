import pygame
from spaceship import Spaceship
from enemy import Enemy

#créer une classe qui va représenter notre jeu
class Game:

    def __init__(self):
        #définir si notre jeu a commencé ou non
        self.is_playing = False
        self.mode_is_choose = False

        #générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Spaceship(self, 200,15,15)
        self.all_players.add(self.player)

        self.pressed = {}

        #groupe de monstres
        self.all_enemy = pygame.sprite.Group()

        #mettre le score a 0
        self.score = 0
        self.font = pygame.font.Font("Roboto/Roboto-Bold.ttf", 25)
        #gérer le son
        # self.sound_manager = SoundManager()

    def create_player(self, difficulty):
        #générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Spaceship(self, 200/difficulty, 10, 30/difficulty)
        self.all_players.add(self.player)

    def show_game_modes(self):
        self.mode_is_choose = True
        
    def start(self):
        self.is_playing = True
        self.spawn_monster()
        # self.spawn_monster(Enemy)
        # self.spawn_monster(Enemy)


    def game_over(self):
        #remettre le jeu à neuf, retirer les monstres, remettre les joueurs à 100 de vie, jeu en attente
        self.all_enemy = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0

    def add_score(self, points = 10):
        self.score += points

    def update(self, screen):

        #afficher le score sur l'écran  
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        #appliquer l'image de notre joueur
        screen.blit(self.player.image, self.player.rect)

        # #actualiser la barre de vie du joueur
        # self.player.update_health_bar(screen)

        # #actualiser la barre d'évenement du jeu
        # self.comet_event.update_bar(screen)

        # #animer joueurs
        # self.player.update_animation()
        

        # #récuperer les projectiles du joueurs
        # for projectile in self.player.all_projectiles:
        #     projectile.move()

        # #récuperer les monstres du jeu
        # for monster in self.all_monsters:
        #     monster.forward()
        #     monster.update_health_bar(screen)
        #     monster.update_animation()

        #récuperer les comètes du jeu
        # for comet in self.comet_event.all_comets:
        #     comet.fall()

        # #appliquer l'ensemble des images de mon groupe de projectiles
        # self.player.all_projectiles.draw(screen)

        # #appliquer l'ensemble des images de mon groupe de monstres
        # self.all_monsters.draw(screen)

        # #appliquer l'ensemble des images de mon groupe de comètes
        # self.comet_event.all_comets.draw(screen)

        #vérifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width<= screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >= 0 :
            self.player.move_left()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height<= screen.get_height():
            self.player.move_down()
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y >= 0 :
            self.player.move_up()



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self):
        enemy = Enemy(self)
        self.all_enemy.add(enemy)