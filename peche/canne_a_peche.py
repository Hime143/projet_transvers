import pygame
import math


class Canne:

    def __init__(self):

        self.x = 640
        self.y = 50

        self.descend = True
        self.remonte = False

        self.vitesse_descente = 1.2
        self.vitesse_remontee = 8

        self.max_longueur = 650

        self.direction_x = 0.0
        self.vitesse_derive = 1.8

        self.points = [(self.x, self.y)]

    def _bout(self):
        return self.points[-1]

    def _longueur_totale(self):
        total = 0.0
        for i in range(1, len(self.points)):
            dx = self.points[i][0] - self.points[i-1][0]
            dy = self.points[i][1] - self.points[i-1][1]
            total += math.sqrt(dx*dx + dy*dy)
        return total

    def update(self, keys):

        if self.descend:

            if keys[pygame.K_LEFT] or keys[pygame.K_q]:
                self.direction_x = -self.vitesse_derive
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.direction_x = self.vitesse_derive
            else:
                self.direction_x = 0.0

            bx, by = self._bout()
            nouveau_x = bx + self.direction_x
            nouveau_y = by + self.vitesse_descente

            nouveau_x = max(20, min(1260, nouveau_x))

            self.points.append((nouveau_x, nouveau_y))

            if self._longueur_totale() >= self.max_longueur:
                self.descend = False
                self.remonte = True

        elif self.remonte:

            if len(self.points) > 1:
                for _ in range(8):
                    if len(self.points) > 1:
                        self.points.pop()
            else:
                self.points = [(self.x, self.y)]
                self.remonte = False
                self.descend = True

    def get_hook_pos(self):
        return self._bout()

    def draw(self, screen):

        pygame.draw.circle(screen, (150, 75, 0), (self.x, self.y), 8)

        if len(self.points) >= 2:
            pts_int = [(int(p[0]), int(p[1])) for p in self.points]
            pygame.draw.lines(screen, (255, 255, 255), False, pts_int, 2)

        hx, hy = self._bout()
        pygame.draw.circle(screen, (200, 200, 200), (int(hx), int(hy)), 6)