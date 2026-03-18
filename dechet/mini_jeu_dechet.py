import pygame
import random
from dechet.dechet import dechet_poub


def lancer_jeu_poubelle(screen, clock, font, collision_map):

    nb_dechet = []
    max_dechet = 5
    spawn_timer = 0
    spawn_interval = 12 * 60

    running = True

    while running:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # spawn toutes les 12s
        spawn_timer += 1
        if spawn_timer >= spawn_interval or len(nb_dechet) == 0:
            spawn_timer = 0
            if len(nb_dechet) < max_dechet:
                nb_dechet.append(dechet_poub(collision_map))

        screen.fill((200, 220, 255))

        for d in nb_dechet:
            d.draw(screen)

        pygame.display.flip()

    return True