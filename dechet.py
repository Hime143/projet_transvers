# class dechet (taille, nb_point)

import random
import pygame




class dechet_poub :

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.screen = pygame.Surface((50,50),pygame.SRCALPHA)
        self.type_d = random.choice(["plastic", "verre", "papier"])
        if self.type_d == "plastic":
            self.image = random.choice([pygame.image.load('Images/plastique_1.png'),pygame.image.load('Images/plastique_2.png'),pygame.image.load('Images/plastique_3.png')])
        if self.type_d == "verre":
            self.image = random.choice([pygame.image.load('Images/papier_1.png'),pygame.image.load('Images/papier_2.png'),pygame.image.load('Images/papier_3.png')])
        if self.type_d == "papier":
            self.image = random.choice([pygame.image.load('Images/verre_1.png'),pygame.image.load('Images/verre_2.png'),pygame.image.load('Images/verre_3.png')])
        self.rect = self.image.get_rect(x=x, y=y)


    def collision(self,x,y):
        return self.pygame.Rect.colliderect(x, y)


    def collecter_dechet(self,inventaire):
       # if self.collision(100,789) :
       inventaire.append(self.type_d)

    def draw(self):
        pass

#ev = []
#d = dechet_poub(0,0,"plastic")
#emplacement = []
#for i in range(5):
 #   emplacement.append(d.Spawn())
#print(emplacement)
#for i in range (3) :
 #   d.Type_ale()
  #  d.collecter_dechet(ev)
   # print(ev)
    #print(d.type_d)
#methode :
#spawn (avec random)
#collision_collecte#
#disparition()

#sous class part type