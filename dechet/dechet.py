import pygame
import random


class dechet_poub:

    def __init__(self, collision_map):

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
        self.x, self.y = self._spawn_valide(collision_map)

        # le rect sert pour l'affichage et les collisions
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def _spawn_valide(self, collision_map):
        # on cherche une position blanche sur la map (pas dans l'eau)
        while True:
            x = random.randint(50, 1230)
            y = random.randint(50, 620)
            # si le pixel n'est pas noir c'est la banquise
            if collision_map.get_at((x, y))[:3] != (0, 0, 0):
                return x, y

    def draw(self, screen):
        # on affiche le déchet sur l'écran
        screen.blit(self.image, self.rect)