import pygame
import random
import math

WIDTH = 1280
HEIGHT = 700

class Poisson:

    def __init__(self):

        self.taille = random.choice([60, 80, 100])
        self.nb_point = self.taille // 20

        self.spawn()

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

        # on charge l'image une seule fois ici
        self.image = self._charger_image()

    def _charger_image(self):
        """Charge la bonne image selon la taille et la couleur"""

        # petit poisson
        if self.taille == 60:
            if self.couleur == (255, 140, 0):
                nom = "pet_poisson_bleu.png"
            elif self.couleur == (100, 220, 100):
                nom = "pet_poisson_jaune.png"
            elif self.couleur == (220, 80, 180):
                nom = "pet_poisson_orange.png"
            elif self.couleur == (255, 80, 80):
                nom = "pet_poisson_rose.png"
            elif self.couleur == (255, 220, 50):
                nom = "pet_poisson_rouge.png"
            else:
                nom = "pet_poisson_vert.png"

        # moyen poisson
        elif self.taille == 80:
            if self.couleur == (0, 200, 255):
                nom = "moy_poissons_bleu.png"
            elif self.couleur == (100, 220, 100):
                nom = "moy_poissons_jaune.png"
            elif self.couleur == (220, 80, 180):
                nom = "moy_poissons_orange.png"
            elif self.couleur == (255, 220, 50):
                nom = "moy_poissons_rose.png"
            elif self.couleur == (255, 140, 0):
                nom = "moy_poissons_rouge.png"
            else:
                nom = "moy_poissons_vert.png"

        # grand poisson
        else:
            if self.couleur == (255, 140, 0):
                nom = "gr_poissons_bleu.png"
            elif self.couleur == (0, 200, 255):
                nom = "gr_poissons_jaune.png"
            elif self.couleur == (255, 80, 80):
                nom = "gr_poissons_vert.png"
            elif self.couleur == (220, 80, 180):
                nom = "gr_poissons_orangepng.png"
            elif self.couleur == (255, 220, 50):
                nom = "gr_poissons_rose.png"
            else:
                nom = "gr_poissons_rouge.png"

        # on charge et redimensionne une seule fois
        img = pygame.image.load(f"Images/{nom}").convert_alpha()
        return pygame.transform.smoothscale(img, (self.taille, 50))

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
        # on affiche juste l'image déjà chargée
        screen.blit(self.image, self.rect)