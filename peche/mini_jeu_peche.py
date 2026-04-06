import pygame
import random

from peche.poissons import Poisson
from peche.canne_a_peche import Canne


def lancer_mini_jeu():

    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    poissons = []
    canne = Canne()

    spawn_timer = 0
    score = 0
    objectif = 10
    total_poissons_peches = 0

    temps_total = (60 * 60)
    temps_restant = temps_total

    font_grande = pygame.font.SysFont(None, 52)
    font = pygame.font.SysFont(None, 38)
    font_petite = pygame.font.SysFont(None, 26)

    particules = []

    bulles = [
        {
            "x": random.randint(0, 1280),
            "y": random.randint(0, 700),
            "r": random.randint(3, 8),
            "vitesse": random.uniform(0.3, 0.8)
        }
        for _ in range(30)
    ]

    running = True

    while running:

        screen.fill((10, 60, 120))
        for i in range(700):
            ratio = i / 700
            r = int(10 + ratio * 5)
            g = int(60 - ratio * 30)
            b = int(120 - ratio * 50)
            pygame.draw.line(screen, (r, g, b), (0, i), (1280, i))

        pygame.draw.ellipse(screen, (20, 100, 60),  pygame.Rect(-50, 640, 400, 120))
        pygame.draw.ellipse(screen, (15, 80, 50),   pygame.Rect(300, 650, 500, 100))
        pygame.draw.ellipse(screen, (25, 110, 70),  pygame.Rect(750, 635, 600, 130))

        for b in bulles:
            b["y"] -= b["vitesse"]
            if b["y"] < -10:
                b["y"] = 710
                b["x"] = random.randint(0, 1280)
            pygame.draw.circle(screen, (60, 160, 220), (int(b["x"]), int(b["y"])), b["r"], 1)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

        spawn_timer += 1
        if spawn_timer > 70:
            poissons.append(Poisson())
            spawn_timer = 0

        canne.update(keys)
        bout_x, bout_y = canne.get_hook_pos()

        for p in poissons[:]:
            p.deplacement()

            if (canne.descend or canne.remonte) and p.collision_collecte(bout_x, bout_y):
                score += p.nb_point
                total_poissons_peches += 1
                poissons.remove(p)

                for _ in range(12):
                    particules.append({
                        "x": float(bout_x),
                        "y": float(bout_y),
                        "vx": random.uniform(-3, 3),
                        "vy": random.uniform(-4, 0),
                        "duree": 30,
                        "couleur": p.couleur
                    })

            elif p.disparition():
                poissons.remove(p)

        for part in particules[:]:
            part["x"] += part["vx"]
            part["y"] += part["vy"]
            part["vy"] += 0.15
            part["duree"] -= 1
            pygame.draw.circle(screen, part["couleur"],
                               (int(part["x"]), int(part["y"])), 3)
            if part["duree"] <= 0:
                particules.remove(part)

        for p in poissons:
            p.draw(screen)

        canne.draw(screen)

        texte_score = font.render(f"Score : {score}", True, (255, 255, 255))
        screen.blit(texte_score, (20, 15))

        texte_poissons = font.render(
            f"Poissons : {total_poissons_peches}  |  Objectif : {objectif}",
            True, (180, 230, 255)
        )
        screen.blit(texte_poissons, (20, 55))

        secondes = max(0, temps_restant // 60)
        largeur_barre = int(400 * temps_restant / temps_total)
        couleur_barre = (
            (80, 220, 100)  if secondes > 30
            else (255, 200, 0)  if secondes > 15
            else (255, 60, 60)
        )
        pygame.draw.rect(screen, (30, 30, 60),    pygame.Rect(440, 18, 400, 22), border_radius=10)
        pygame.draw.rect(screen, couleur_barre,   pygame.Rect(440, 18, largeur_barre, 22), border_radius=10)
        pygame.draw.rect(screen, (150, 150, 200), pygame.Rect(440, 18, 400, 22), 2, border_radius=10)
        texte_temps = font_petite.render(f"{secondes}s", True, (200, 220, 255))
        screen.blit(texte_temps, (848, 22))

        temps_restant -= 1

        if temps_restant <= 0 or total_poissons_peches >= objectif:
            running = False

        pygame.display.flip()
        clock.tick(60)

    _ecran_fin(screen, clock, score, objectif, total_poissons_peches, font_grande, font)
    return score


def _ecran_fin(screen, clock, score, objectif, total_peches, font_grande, font):

    victoire = total_peches >= objectif
    timer = 0

    while True:

        screen.fill((5, 30, 70))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and timer > 120:
                return

        timer += 1

        titre = font_grande.render(
            "Bravo !" if victoire else "Temps écoulé...",
            True,
            (255, 220, 60) if victoire else (200, 100, 100)
        )
        ligne1 = font.render(f"Poissons pêchés : {total_peches}", True, (200, 220, 255))
        ligne2 = font.render(f"Score total : {score} pts", True, (200, 220, 255))

        screen.blit(titre,  titre.get_rect(center=(640, 260)))
        screen.blit(ligne1, ligne1.get_rect(center=(640, 330)))
        screen.blit(ligne2, ligne2.get_rect(center=(640, 375)))

        if timer > 120:
            hint = font.render("Clic ou touche pour continuer", True, (150, 170, 200))
            screen.blit(hint, hint.get_rect(center=(640, 445)))

        pygame.display.flip()
        clock.tick(60)