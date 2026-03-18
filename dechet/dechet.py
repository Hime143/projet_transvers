import random
import pygame


class dechet_poub:

    def __init__(self, collision_map):

        self.type_d = random.choice(["plastique", "verre", "papier"])

        if self.type_d == "plastique":
            self.image = random.choice([
                pygame.image.load('Images/plastique_1.png').convert_alpha(),
                pygame.image.load('Images/plastique_2.png').convert_alpha(),
                pygame.image.load('Images/plastique_3.png').convert_alpha(),
            ])
        elif self.type_d == "verre":
            self.image = random.choice([
                pygame.image.load('Images/verre_1.png').convert_alpha(),
                pygame.image.load('Images/verre_2.png').convert_alpha(),
                pygame.image.load('Images/verre_3.png').convert_alpha(),
            ])
        elif self.type_d == "papier":
            self.image = random.choice([
                pygame.image.load('Images/papier_1.png').convert_alpha(),
                pygame.image.load('Images/papier_2.png').convert_alpha(),
                pygame.image.load('Images/papier_3.png').convert_alpha(),
            ])

        self.image = pygame.transform.smoothscale(self.image, (60, 60))

        # spawn sur la banquise uniquement
        self.x, self.y = self._spawn_valide(collision_map)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def _spawn_valide(self, collision_map):
        while True:
            x = random.randint(50, 1230)
            y = random.randint(50, 620)
            if collision_map.get_at((x, y))[:3] != (0, 0, 0):
                return x, y

    def collecter(self, inventaire):
        inventaire.append(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)