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

        cx = int(self.x)
        cy = int(self.y)
        r = self.taille // 2

        # corps
        pygame.draw.ellipse(
            screen,
            self.couleur,
            pygame.Rect(cx - r, cy - r // 2, r * 2, r)
        )

        # queue
        queue_pts = [
            (cx - r,         cy),
            (cx - r - r,     cy - r // 2),
            (cx - r - r,     cy + r // 2),
        ]
        pygame.draw.polygon(screen, self.couleur_sombre, queue_pts)

        # nageoire dorsale
        nageoire_pts = [
            (cx - r // 4,  cy - r // 2),
            (cx + r // 4,  cy - r // 2),
            (cx,           cy - r),
        ]
        pygame.draw.polygon(screen, self.couleur_sombre, nageoire_pts)

        # œil
        oeil_x = cx + r // 3
        oeil_y = cy - r // 6
        pygame.draw.circle(screen, (0, 0, 60),      (oeil_x, oeil_y), max(4, r // 4))
        pygame.draw.circle(screen, (255, 255, 255),  (oeil_x - 2, oeil_y - 2), max(2, r // 8))

        # bouche
        pygame.draw.arc(
            screen,
            (0, 0, 40),
            pygame.Rect(cx + r // 2, cy - r // 8, r // 4, r // 6),
            0, math.pi,
            2
        )