from pygame.math import Vector2
import pygame
import random
import core



class Creep :

    def __int__(self,largeur = 400,hauteur = 400):
        self.position =Vector2(random.roudint(0,largeur),random.roudint(0,hauteur))
        self.taille = 10
        self.couleur = (random.roudint(0,255),random.roudint(0,255),random.roudint(0,255))
        self.masse = 10


    def show (self,screen) :

        pygame.draw.circle(screen,self.couleur,[int(self.position.x),int(self.position.y)],self.taille)

    """def update (self) :
        if self.couleur(0)>0 and self.couleur(1)>0 and self.couleur(2)>0 :
            self.couleur = self.couleur-(0)-1,self.couleur-(0)-1,self.couleur-(0)-1
        else :
            self.couleur(0,0,0)"""

