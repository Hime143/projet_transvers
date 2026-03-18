import pygame
import random
import math

WIDTH = 1280
HEIGHT = 700


class Poisson:

    def __init__(self):

        # tailles augmentées : 60, 80, 100 au lieu de 20, 30, 40
        self.taille = random.choice([60, 80, 100])
        self.nb_point = self.taille // 20

        self.spawn()

        # hitbox centrée sur le poisson
        self.rect = pygame.Rect(0, 0, self.taille * 2, self.taille)
        self.rect.center = (int(self.x), int(self.y))
        self.couleur = random.choice([
            (0, 200, 255),
            (255, 140, 0),
            (100, 220, 100),
            (220, 80, 180),
            (255, 80, 80),
            (255, 220, 50),
        ])

        self.couleur_sombre = tuple(max(0, c - 60) for c in self.couleur)

    def spawn(self):
        self.x = -120.0
        self.y = float(random.randint(200, HEIGHT - 80))
        self.vitesse = random.uniform(1.0, 2.5)

    def deplacement(self):
        self.x += self.vitesse
        self.rect.center = (int(self.x), int(self.y))

    def collision_collecte(self, x, y):
        return self.rect.collidepoint(x, y)

    def disparition(self):
        return self.x > WIDTH + 150

    def draw(self, screen):

        #petit poisson
        if self.taille == 60 :
            if self.couleur == (255, 140, 0):
                pp1 = pygame.image.load("Images/pet_poisson_bleu.png").convert_alpha()
                pp1 = pygame.transform.scale(pp1, (self.taille, 50))
                screen.blit(pp1, self.rect)
            if self.couleur == (100, 220, 100):
                pp2 = pygame.image.load("Images/pet_poisson_jaune.png").convert_alpha()
                pp2 = pygame.transform.scale(pp2, (self.taille, 50))
                screen.blit(pp2, self.rect)
            if self.couleur == (220, 80, 180):
                pp3 = pygame.image.load("Images/pet_poisson_orange.png").convert_alpha()
                pp3 = pygame.transform.scale(pp3, (self.taille, 50))
                screen.blit(pp3, self.rect)
            if self.couleur == (255, 80, 80):
                pp4 = pygame.image.load("Images/pet_poisson_rose.png").convert_alpha()
                pp4 = pygame.transform.scale(pp4, (self.taille, 50))
                screen.blit(pp4, self.rect)
            if self.couleur == (255, 220, 50):
                pp5 = pygame.image.load("Images/pet_poisson_rouge.png").convert_alpha()
                pp5 = pygame.transform.scale(pp5, (self.taille, 50))
                screen.blit(pp5, self.rect)
            if self.couleur == (0, 200, 255):
                pp6 = pygame.image.load("Images/pet_poisson_vert.png").convert_alpha()
                pp6 = pygame.transform.scale(pp6, (self.taille, 50))
                screen.blit(pp6, self.rect)
         # moyen
        if self.taille == 80:
            if self.couleur == (0, 200, 255):
                pm1 = pygame.image.load("Images/moy_poissons_bleu.png").convert_alpha()
                pm1 = pygame.transform.scale(pm1, (self.taille, 50))
                screen.blit(pm1, self.rect)
            if self.couleur == (100, 220, 100):
                pm2 = pygame.image.load("Images/moy_poissons_jaune.png").convert_alpha()
                pm2 = pygame.transform.scale(pm2, (self.taille, 50))
                screen.blit(pm2, self.rect)
            if self.couleur == (220, 80, 180):
                pm3 = pygame.image.load("Images/moy_poissons_orange.png").convert_alpha()
                pm3 = pygame.transform.scale(pm3, (self.taille, 50))
                screen.blit(pm3, self.rect)
            if self.couleur == (255, 220, 50):
                pm4 = pygame.image.load("Images/moy_poissons_rose.png").convert_alpha()
                pm4 = pygame.transform.scale(pm4, (self.taille, 50))
                screen.blit(pm4, self.rect)
            if self.couleur == (255, 140, 0):
                pm5 = pygame.image.load("Images/moy_poissons_rouge.png").convert_alpha()
                pm5 = pygame.transform.scale(pm5, (self.taille, 50))
                screen.blit(pm5, self.rect)
            if self.couleur == (255, 80, 80):
                pm6 = pygame.image.load("Images/moy_poissons_vert.png").convert_alpha()
                pm6 = pygame.transform.scale(pm6, (self.taille, 50))
                screen.blit(pm6, self.rect)

        if self.taille == 100:
            if self.couleur == (255, 140, 0):
                pg1 = pygame.image.load("Images/gr_poissons_bleu.png").convert_alpha()
                pg1 = pygame.transform.scale(pg1, (self.taille, 50))
                screen.blit(pg1, self.rect)
            if self.couleur == (0, 200, 255):
                pg2 = pygame.image.load("Images/gr_poissons_jaune.png").convert_alpha()
                pg2 = pygame.transform.scale(pg2, (self.taille, 50))
                screen.blit(pg2, self.rect)

            if self.couleur == (255, 80, 80):
                pg6 = pygame.image.load("Images/gr_poissons_vert.png").convert_alpha()
                pg6 = pygame.transform.scale(pg6, (self.taille, 50))
                screen.blit(pg6, self.rect)
            if self.couleur == (220, 80, 180):
                pg3 = pygame.image.load("Images/gr_poissons_orangepng.png").convert_alpha()
                pg3 = pygame.transform.scale(pg3, (self.taille, 50))
                screen.blit(pg3, self.rect)
            if self.couleur == (255, 220, 50):
                pg4 = pygame.image.load("Images/gr_poissons_rose.png").convert_alpha()
                pg4 = pygame.transform.scale(pg4, (self.taille, 50))
                screen.blit(pg4, self.rect)
            if self.couleur == (100, 220, 100):
                pg3 = pygame.image.load("Images/gr_poissons_rouge.png").convert_alpha()
                pg3 = pygame.transform.scale(pg3, (self.taille, 50))
                screen.blit(pg3, self.rect)