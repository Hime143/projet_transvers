import pygame
from peche.mini_jeu_peche import lancer_mini_jeu


pygame.init()
font = pygame.font.SysFont(None, 30)


screen = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("IceGuardian")
clock = pygame.time.Clock()
running = True
speed = 3
from img import *

boubou_rect = boubou_img.get_rect(center=(640, 350))
maison_rect = maison.get_rect(center=(240, 150))
musique_rect = musique.get_rect(center=(340, 200))
parametre_rect = parametre.get_rect(center=(440, 250))
peche_rect = peche.get_rect(center=(540, 300))
poubelle_rect = poubelle.get_rect(center=(640, 350))

direction = "down"
frame_index = 0
animation_timer = 0
animation_speed = 20
moving = False
while running:
    moving = False
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_z] or keys[pygame.K_UP]:
        old_y = boubou_rect.y
        boubou_rect.y -= speed
        direction = "up"
        moving = True

        foot_x = boubou_rect.centerx
        foot_y = boubou_rect.bottom

        if collision_map.get_at((foot_x, foot_y))[:3] == (0, 0, 0):
            boubou_rect.y = old_y

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        old_y = boubou_rect.y
        boubou_rect.y += speed
        direction = "down"
        moving = True

        foot_x = boubou_rect.centerx
        foot_y = boubou_rect.bottom

        if collision_map.get_at((foot_x, foot_y))[:3] == (0, 0, 0):
            boubou_rect.y = old_y

    if keys[pygame.K_q] or keys[pygame.K_LEFT]:
        old_x = boubou_rect.x
        boubou_rect.x -= speed
        direction = "left"
        moving = True

        foot_x = boubou_rect.centerx
        foot_y = boubou_rect.bottom

        if collision_map.get_at((foot_x, foot_y))[:3] == (0, 0, 0):
            boubou_rect.x = old_x

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        old_x = boubou_rect.x
        boubou_rect.x += speed
        direction = "right"
        moving = True

        foot_x = boubou_rect.centerx
        foot_y = boubou_rect.bottom

        if collision_map.get_at((foot_x, foot_y))[:3] == (0, 0, 0):
            boubou_rect.x = old_x

    if moving:
        animation_timer += 1
        if animation_timer >= animation_speed:
            animation_timer = 0

            if direction == "up":
                frames = [img_up1, img_up2]
            elif direction == "down":
                frames = [img_down1, img_down2]
            elif direction == "left":
                frames = [img_left1, img_left2]
            else:
                frames = [img_right1, img_right2]

            frame_index = (frame_index + 1) % len(frames)
            boubou_img = frames[frame_index]
    else:
        if direction == "up":
            boubou_img = img_up
        elif direction == "down":
            boubou_img = img_down
        elif direction == "left":
            boubou_img = img_left
        elif direction == "right":
            boubou_img = img_right

    screen.blit(background, (0,0))
    screen.blit(boubou_img, boubou_rect)
    screen.blit(maison, maison_rect)
    screen.blit(peche, peche_rect)
    screen.blit(poubelle, poubelle_rect)
    screen.blit(musique, musique_rect)
    screen.blit(parametre, parametre_rect)
    if boubou_rect.colliderect(peche_rect):

        texte = font.render("Appuyez sur E pour pêcher", True, (255, 255, 255))
        screen.blit(texte, (520, 260))

        if keys[pygame.K_e]:
            lancer_mini_jeu()

            # petite pause pour éviter que ça relance direct
            pygame.time.delay(300)
    pygame.display.flip()

#banquise et poubelles

pygame.quit()
