# Example file showing a circle moving on screen
import pygame
import random
from dechet import dechet_poub
from boubou_dechet import player

def lancer_jeu_poubelle() :
    pygame.init()
    nb_dechet = []
    max_dechet = 3
    boubou = player(0,0)
    screen = pygame.display.set_mode((1000, 500))
    clock = pygame.time.Clock()
    running = True

    dt = 0

    def spawn():
        while len(nb_dechet) < max_dechet:
            coord_x = random.randint(1, screen.get_width() // 2)
            coord_y = random.randint(1, screen.get_height() // 2)
            dec = dechet_poub(coord_x, coord_y)
            nb_dechet.append(dec)


    while running:
        #event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            boubou.velocity[1] = -1
        elif keys[pygame.K_s]:
            boubou.velocity[1] = 1
        else :
            boubou.velocity[1] = 0

        if keys[pygame.K_q]:
            boubou.velocity[0] = -1
        elif keys[pygame.K_d]:
            boubou.velocity[0] = 1
        else :
            boubou.velocity[0] = 0



        spawn()
        for d in nb_dechet:
            screen.blit(pygame.transform.scale(d.image, (100, 100)), d.rect)


        #for toucher in nb_dechet:
            #if toucher.rect.colliderect(boubou.rect) :
                #t = font.render("touvher ", True, (5, 5, 255))
                #screen.blit(t, toucher.rect)



        #update
        boubou.move()





        #display
        boubou.draw(screen)
        pygame.display.flip()
        screen.fill("white")

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


lancer_jeu_poubelle()