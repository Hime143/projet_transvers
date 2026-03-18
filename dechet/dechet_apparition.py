import pygame
import random
from dechet.dechet import dechet_poub as Dechet
from dechet.inventaire import Inventaire
from dechet.tri_dechet import InterfaceTri


def lancer_jeu_dechet(screen, clock, font, collision_map, background,
                       boubou_img_ref, boubou_rect_ref,
                       img_up, img_down, img_left, img_right,
                       img_up1, img_up2, img_down1, img_down2,
                       img_left1, img_left2, img_right1, img_right2,
                       poubelle):

    boubou_rect = boubou_rect_ref.copy()
    boubou_img = img_down

    inventaire = Inventaire(capacite=5)
    interface_tri = InterfaceTri(inventaire, font)
    dechets_map = [Dechet(collision_map) for _ in range(10)]

    afficher_inventaire = False

    direction = "down"
    frame_index = 0
    animation_timer = 0
    animation_speed = 20
    speed = 3
    moving = False

    running = True

    while running:

        moving = False
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    afficher_inventaire = not afficher_inventaire
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN and interface_tri.actif:
                interface_tri.gerer_clic(event.pos)

        keys = pygame.key.get_pressed()

        if not interface_tri.actif:
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

        interface_tri.update()

        screen.blit(background, (0, 0))

        for d in dechets_map:
            d.draw(screen)

        screen.blit(boubou_img, boubou_rect)
        screen.blit(poubelle, pygame.Rect(0, 0, 60, 60).move(640, 350))

        if not interface_tri.actif:
            for d in dechets_map[:]:
                if boubou_rect.colliderect(d.rect):
                    texte = font.render("E pour ramasser", True, (255, 255, 255))
                    screen.blit(texte, (boubou_rect.x - 20, boubou_rect.y - 30))
                    if keys[pygame.K_e] and not inventaire.est_plein():
                        inventaire.ajouter(d)
                        dechets_map.remove(d)
                        pygame.time.delay(150)

            poubelle_rect = pygame.Rect(640 - 30, 350 - 30, 60, 60)
            if boubou_rect.colliderect(poubelle_rect) and not inventaire.est_vide():
                texte = font.render("E pour trier", True, (255, 255, 255))
                screen.blit(texte, (boubou_rect.x - 20, boubou_rect.y - 30))
                if keys[pygame.K_e]:
                    interface_tri.ouvrir()
                    pygame.time.delay(200)

        _draw_hotbar(screen, inventaire, font)

        if afficher_inventaire:
            _draw_inventaire_minecraft(screen, inventaire, font)

        interface_tri.draw(screen)

        hint = font.render("TAB : inventaire", True, (180, 180, 180))
        screen.blit(hint, (1100, 10))

        pygame.display.flip()

    return True


def _draw_hotbar(screen, inventaire, font):

    taille_slot = 60
    nb_slots = inventaire.capacite
    marge = 6
    largeur_totale = nb_slots * taille_slot + (nb_slots - 1) * marge
    start_x = (1280 - largeur_totale) // 2
    y = 700 - taille_slot - 15

    compteur = {}
    for d in inventaire.contenu:
        compteur[d.type_d] = compteur.get(d.type_d, 0) + 1

    pygame.draw.rect(
        screen, (30, 30, 30),
        pygame.Rect(start_x - 8, y - 8, largeur_totale + 16, taille_slot + 16),
        border_radius=8
    )
    pygame.draw.rect(
        screen, (80, 80, 80),
        pygame.Rect(start_x - 8, y - 8, largeur_totale + 16, taille_slot + 16),
        2, border_radius=8
    )

    vus = {}
    for i in range(nb_slots):
        sx = start_x + i * (taille_slot + marge)

        pygame.draw.rect(screen, (50, 50, 50),
                         pygame.Rect(sx, y, taille_slot, taille_slot), border_radius=4)
        pygame.draw.rect(screen, (100, 100, 100),
                         pygame.Rect(sx, y, taille_slot, taille_slot), 1, border_radius=4)

        if i < len(inventaire.contenu):
            dechet = inventaire.contenu[i]
            img = pygame.transform.smoothscale(dechet.image, (48, 48))
            screen.blit(img, (sx + 6, y + 6))

            qte = compteur.get(dechet.type_d, 1)
            if dechet.type_d not in vus:
                vus[dechet.type_d] = 0
            vus[dechet.type_d] += 1

            if qte > 1:
                font_nb = pygame.font.SysFont(None, 22)
                nb_txt = font_nb.render(str(vus[dechet.type_d]), True, (255, 255, 255))
                screen.blit(nb_txt, (sx + taille_slot - 16, y + taille_slot - 18))


def _draw_inventaire_minecraft(screen, inventaire, font):

    overlay = pygame.Surface((1280, 700), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    fenetre_w, fenetre_h = 500, 400
    fenetre_x = (1280 - fenetre_w) // 2
    fenetre_y = (700 - fenetre_h) // 2

    pygame.draw.rect(screen, (40, 40, 40),
                     pygame.Rect(fenetre_x, fenetre_y, fenetre_w, fenetre_h),
                     border_radius=10)
    pygame.draw.rect(screen, (100, 100, 100),
                     pygame.Rect(fenetre_x, fenetre_y, fenetre_w, fenetre_h),
                     2, border_radius=10)

    titre = font.render("Inventaire", True, (220, 220, 220))
    screen.blit(titre, (fenetre_x + 20, fenetre_y + 15))

    compteur = {"plastique": [], "verre": [], "papier": []}
    for d in inventaire.contenu:
        compteur[d.type_d].append(d)

    COULEURS_TYPE = {
        "plastique": (255, 220, 0),
        "verre":     (0, 200, 120),
        "papier":    (100, 180, 255),
    }

    taille_slot = 64
    marge = 10
    y_depart = fenetre_y + 60

    for ligne, (type_d, liste) in enumerate(compteur.items()):

        y = y_depart + ligne * (taille_slot + marge + 30)

        label = font.render(f"{type_d.capitalize()} :", True, COULEURS_TYPE[type_d])
        screen.blit(label, (fenetre_x + 20, y))

        for col, dechet in enumerate(liste):
            sx = fenetre_x + 20 + col * (taille_slot + marge)
            sy = y + 25

            pygame.draw.rect(screen, (60, 60, 60),
                             pygame.Rect(sx, sy, taille_slot, taille_slot),
                             border_radius=4)
            pygame.draw.rect(screen, (120, 120, 120),
                             pygame.Rect(sx, sy, taille_slot, taille_slot),
                             1, border_radius=4)

            img = pygame.transform.smoothscale(dechet.image, (52, 52))
            screen.blit(img, (sx + 6, sy + 6))

        if liste:
            font_nb = pygame.font.SysFont(None, 22)
            nb_txt = font_nb.render(f"{len(liste)}/5 max", True, (200, 200, 200))
            screen.blit(nb_txt, (fenetre_x + fenetre_w - 90, y + 30))

    hint = font.render("TAB pour fermer", True, (150, 150, 150))
    screen.blit(hint, hint.get_rect(center=(fenetre_x + fenetre_w // 2, fenetre_y + fenetre_h - 20)))