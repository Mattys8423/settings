import pygame
import sys
import math
import time

from game import Game
from settings import Settings
#import the class Enemy from the file enemy.py
from enemy import Enemy
#import the class Spaceship from the file spaceship.py
from spaceship import Spaceship
from screen import *
from affichage import *
from pygame import mixer
from tools import *

#définir une clock
clock = pygame.time.Clock()
FPS = 100


# Define game varibales
scroll = 0
tiles = math.ceil(largeur/bg_largeur) + 1
seconde = time.time()

game = Game()
settings = Settings()

#Boucle de jeu

running = True

while running:

    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(background, (i * bg_largeur + scroll, 0))

    #Scroll background
    scroll -= 5

    # reset scroll
    if abs(scroll) > bg_largeur:
        scroll = 0


    #  ------------------------------------------- Projectiles -------------------------------------------
    #recuperer les projectiles
    for projectile in game.player.all_projectile:
        projectile.move()

    # appliquer l'ensemble des image de mon groupe de projectile
    game.player.all_projectile.draw(screen)

    #  ------------------------------------------- Enemy -------------------------------------------
    #recuperer les ennemy
    for enemy in game.all_enemy:
        enemy.forward()
        enemy.update_health_bar(screen) 
        # while enemy.rect.x != 1600:
        #     enemy.spawn()

    # appliquer l'ensemble des image de mon groupe de mosntres
    game.all_enemy.draw(screen)


     #  ------------------------------------------- Game Related -------------------------------------------
    #vérifier si le jeu a commencé ou non
    if (game.is_playing and game.mode_is_choose):
        #déclencher les isntructions de la partie
        game.update(screen, seconde)
    #---------settings--------#
    elif(settings.is_settings):
        show_settings()
    #verifier quelles sont les settings lancés
    elif(settings.is_gameplay):
        show_gameplay()
        volume_choisi = slider.getValue() // 100
        text.setText(slider.getValue())
    elif(settings.is_commandes):
        show_commandes()
        
    #Show the screen with the difficulties
    elif(not game.is_playing and not game.mode_is_choose and game.planete_is_choose):
        show_planetes()

    #vérifier si notre jeu n'a pas commencé
    #Show the screen with the difficulties
    elif(not game.is_playing and game.mode_is_choose):
        show_difficulty()
    #vérifier si notre jeu n'a pas commencé
    else:
        show_menu()

    #Dessin de la fenêtre
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Fermeture du jeu")
            sys.exit()
            
            
        # Faire spawn des ennemis
        if game.is_playing == True:
            
            if time.time() > seconde + 3:
                game.spawn_monster()
                seconde = time.time()

        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #détecter si la touche espace est enclenchée pour lance notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif (event.type == pygame.MOUSEBUTTONDOWN):

            #vérification pour svaoir si la souris est en collision avec le bouton
            if (play_button_rect.collidepoint(event.pos)):

                game.show_planetes()

            #vérification pour svaoir si la souris est en collision avec le bouton
            elif (settings_button_rect.collidepoint(event.pos)):
                settings.go_settings()
            elif(Gameplay_button_rect.collidepoint(event.pos)):
                settings.start_gameplay()
            elif(controle_button_rect.collidepoint(event.pos)):
                settings.start_commandes()
            elif(return_button_rect.collidepoint(event.pos)):
                settings.back_settings()
            
            elif (terre_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete1_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete2_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete3_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete4_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete5_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete6_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            
            elif (easy_button_rect.collidepoint(event.pos)):
                game.create_player(1)
                game.start()

            elif (medium_button_rect.collidepoint(event.pos)):
                game.create_player(1.5)

                game.start()
            elif (hard_button_rect.collidepoint(event.pos)):
                game.create_player(2)

                game.start()
            elif (nightmare_button_rect.collidepoint(event.pos)):
                game.create_player(3)

                game.start()
                
                #mettre le jeu en monde "lancé"
                
    
    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)  
