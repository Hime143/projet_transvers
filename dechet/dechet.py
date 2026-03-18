import pygame
import random


class dechet_poub:

    def __init__(self, collision_map, zones_interdites=[]):  # ← ajout ici

        # on choisit aléatoirement le type de déchet
        self.type_d = random.choice(["plastique", "verre", "papier"])

        # on charge l'image selon le type
        if self.type_d == "plastique":
            self.image = random.choice([
                pygame.image.load("Images/plastique_1.png").convert_alpha(),
                pygame.image.load("Images/plastique_2.png").convert_alpha(),
                pygame.image.load("Images/plastique_3.png").convert_alpha(),
            ])

        elif self.type_d == "verre":
            self.image = random.choice([
                pygame.image.load("Images/verre_1.png").convert_alpha(),
                pygame.image.load("Images/verre_2.png").convert_alpha(),
                pygame.image.load("Images/verre_3.png").convert_alpha(),
            ])

        elif self.type_d == "papier":
            self.image = random.choice([
                pygame.image.load("Images/papier_1.png").convert_alpha(),
                pygame.image.load("Images/papier_2.png").convert_alpha(),
                pygame.image.load("Images/papier_3.png").convert_alpha(),
            ])

        # on redimensionne l'image à 60x60 pixels
        self.image = pygame.transform.smoothscale(self.image, (60, 60))

        # on trouve une position valide sur la banquise
        self.x, self.y = self._spawn_valide(collision_map, zones_interdites)

        # le rect sert pour l'affichage et les collisions
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def _spawn_valide(self, collision_map, zones_interdites=[]):
        """Cherche une position valide sur la banquise loin des obstacles"""
        while True:
            x = random.randint(50, 1230)
            y = random.randint(50, 620)
            # pas dans l'eau
            if collision_map.get_at((x, y))[:3] == (0, 0, 0):
                continue
            # pas sur les zones interdites
            point = pygame.Rect(x, y, 1, 1)
            trop_proche = False
            for zone in zones_interdites:
                if point.colliderect(zone):
                    trop_proche = True
                    break
            if not trop_proche:
                return x, y

    def draw(self, screen):
        # on affiche le déchet sur l'écran
        screen.blit(self.image, self.rect)