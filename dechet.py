# class dechet (taille, nb_point)

import random
import pygame
import math
from main import boubou_rect

class dechet_poub :

    def __init__(self,x,y,type_d):
        self.x = x
        self.y = y
        self.type_d = None

    def Spawn(self):
        self.x.random.randint(0,1281)
        self.y.random.randint(0, 701)
        self.Type_ale()
        self.draw((1280,700))


    def Type_ale(self):
        self.type_d = random.choice(["plastic", "verre", "papier"])

    def collision(self,x,y):
        return self.rect.collidepoint(x, y)


    def collecter_dechet(self,inventaire):
        if self.collision(boubou_rect.x,boubou_rect.y) :
            inventaire.append(self)

    def draw(self,screen):
        pygame.draw.circle(screen,(150,255,255),self.x,self.y,2)

ev = []
d = dechet_poub(0,0,"plastic")
d.collecter_dechet(ev)
d.Type_ale()

print(ev)
print(d.type_d)
#methode :
#spawn (avec random)
#collision_collecte
#disparition()

#sous class part type