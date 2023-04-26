import pygame

#créer une classe qui va représenter nos settings
class Settings:

    def __init__(self):
        #définir nos settings
        self.is_settings = False
        self.is_commandes = False
        self.is_gameplay = False

    def go_settings(self):
        self.is_settings = True
        self.is_commandes = False
        self.is_gameplay = False
        
    def start_commandes(self):
        self.is_settings = False
        self.is_commandes = True
        self.is_gameplay = False

    def start_gameplay(self):
        self.is_settings = False
        self.is_commandes = False
        self.is_gameplay = True
        
    def back_settings(self):
        self.is_settings = False
        self.is_commandes = False
        self.is_gameplay = False
        
    #audio
    #pygame.mixer_music.set_volume()

