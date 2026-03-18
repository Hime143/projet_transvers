import pygame

#BACKGROUND
background = pygame.image.load("Images/Banquise.png").convert_alpha()
background = pygame.transform.scale(background, (1280,700))

#COLISION
collision_map = pygame.image.load("Images/collision_map.png").convert_alpha()
collision_map = pygame.transform.scale(collision_map, (1280,700))

#STANDING IMG
img_up = pygame.image.load("Images/BOUBOUHAUT.png").convert_alpha()
img_up = pygame.transform.scale(img_up, (80,138))

img_down = pygame.image.load("Images/BOUBOUVERSNOUS.png").convert_alpha()
img_down = pygame.transform.scale(img_down, (80,138))

img_left = pygame.image.load("Images/BOUBOUGAUCHE.png").convert_alpha()
img_left = pygame.transform.scale(img_left, (80,138))

img_right = pygame.image.load("Images/BOUBOUDROITE.png").convert_alpha()
img_right = pygame.transform.scale(img_right, (80,138))

boubou_img = img_down

#WALKING
img_up1 = pygame.image.load("Images/BOUBOUDERRIERE1.png").convert_alpha()
img_up1 = pygame.transform.scale(img_up1, (80,138))

img_up2 = pygame.image.load("Images/BOUBOUDERRIERE2.png").convert_alpha()
img_up2 = pygame.transform.scale(img_up2, (80,138))

img_down1 = pygame.image.load("Images/BOUBOUDEVANT1.png").convert_alpha()
img_down1 = pygame.transform.scale(img_down1, (80,138))

img_down2 = pygame.image.load("Images/BOUBOUDEVANT2.png").convert_alpha()
img_down2 = pygame.transform.scale(img_down2, (80,138))

img_left1 = pygame.image.load("Images/BOUBOUGAUCHE1.png").convert_alpha()
img_left1 = pygame.transform.scale(img_left1, (80,138))

img_left2 = pygame.image.load("Images/BOUBOUGAUCHE2.png").convert_alpha()
img_left2 = pygame.transform.scale(img_left2, (80,138))

img_right1 = pygame.image.load("Images/BOUBOUDROITE1.png").convert_alpha()
img_right1 = pygame.transform.scale(img_right1, (80,138))

img_right2 = pygame.image.load("Images/BOUBOUDROITE2.png").convert_alpha()
img_right2 = pygame.transform.scale(img_right2, (80,138))

#ICONE
maison = pygame.image.load("Images/maison_icone.png").convert_alpha()
maison = pygame.transform.scale(maison, (60,60))

musique = pygame.image.load("Images/musique_icone.png").convert_alpha()
musique = pygame.transform.scale(musique, (60,60))

parametre = pygame.image.load("Images/parametre_icone.png").convert_alpha()
parametre = pygame.transform.scale(parametre, (60,60))

peche = pygame.image.load("Images/peche_icone.png").convert_alpha()
peche = pygame.transform.scale(peche, (60,60))

poubelle = pygame.image.load("Images/poubelle_icone.png").convert_alpha()
poubelle = pygame.transform.scale(poubelle, (60,60))

#POUBELLE

poubelle_bleu = pygame.image.load("Images/poubelle_bleu.png").convert_alpha()
poubelle_bleu = pygame.transform.scale(poubelle_bleu, (65,120))

poubelle_jaune = pygame.image.load("Images/poubelle_jaune.png").convert_alpha()
poubelle_jaune = pygame.transform.scale(poubelle_jaune, (65,120))

poubelle_verte = pygame.image.load("Images/poubelle_verte.png").convert_alpha()
poubelle_verte = pygame.transform.scale(poubelle_verte, (65,120))
