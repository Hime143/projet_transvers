import pygame
from peche.mini_jeu_peche import lancer_mini_jeu
from menu import ecran_accueil
from dechet.dechet import dechet_poub as Dechet
from dechet.inventaire import Inventaire
from dechet.tri_dechet import InterfaceTri

pygame.init()
font = pygame.font.SysFont(None, 30)

screen = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("IceGuardian")
clock = pygame.time.Clock()
running = True
speed = 3
from img import *

if not ecran_accueil(screen, clock, background):
    pygame.quit()
    exit()

boubou_rect = boubou_img.get_rect(center=(640, 350))
maison_rect = maison.get_rect(center=(240, 150))
musique_rect = musique.get_rect(center=(340, 200))
parametre_rect = parametre.get_rect(center=(440, 250))
peche_rect = peche.get_rect(center=(540, 300))
poubelle_rect = poubelle.get_rect(center=(640, 350))

inventaire = Inventaire(capacite=5)
interface_tri = InterfaceTri(inventaire, font)
dechets_map = [Dechet(collision_map) for _ in range(10)]
afficher_inventaire = False

direction = "down"
frame_index = 0
animation_timer = 0
animation_speed = 20
moving = False


def _draw_inventaire_minecraft(screen, inventaire, font):

    overlay = pygame.Surface((1280, 700), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    fenetre_w, fenetre_h = 700, 500
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

    taille_slot = 90
    marge = 14
    y_depart = fenetre_y + 70

    for ligne, (type_d, liste) in enumerate(compteur.items()):

        y = y_depart + ligne * (taille_slot + marge + 30)

        label = font.render(f"{type_d.capitalize()} :", True, COULEURS_TYPE[type_d])
        screen.blit(label, (fenetre_x + 20, y))

        for col, dechet in enumerate(liste):
            sx = fenetre_x + 20 + col * (taille_slot + marge)
            sy = y + 28

            pygame.draw.rect(screen, (60, 60, 60),
                             pygame.Rect(sx, sy, taille_slot, taille_slot),
                             border_radius=6)
            pygame.draw.rect(screen, (120, 120, 120),
                             pygame.Rect(sx, sy, taille_slot, taille_slot),
                             1, border_radius=6)

            img = pygame.transform.smoothscale(dechet.image, (78, 78))
            screen.blit(img, (sx + 6, sy + 6))

        if liste:
            font_nb = pygame.font.SysFont(None, 26)
            nb_txt = font_nb.render(f"{len(liste)}/5 max", True, (200, 200, 200))
            screen.blit(nb_txt, (fenetre_x + fenetre_w - 110, y + 40))

    hint = font.render("TAB pour fermer", True, (150, 150, 150))
    screen.blit(hint, hint.get_rect(center=(fenetre_x + fenetre_w // 2, fenetre_y + fenetre_h - 20)))


while running:
    moving = False
    clock.tick(60)

    souris_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                afficher_inventaire = not afficher_inventaire

        if event.type == pygame.MOUSEBUTTONDOWN:
            if poubelle_rect.collidepoint(souris_pos) and not inventaire.est_vide():
                interface_tri.ouvrir()
            if interface_tri.actif:
                interface_tri.gerer_clic(souris_pos)

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
    screen.blit(maison, maison_rect)
    screen.blit(musique, musique_rect)
    screen.blit(parametre, parametre_rect)
    screen.blit(peche, peche_rect)

    # icône poubelle avec effet survol
    if poubelle_rect.collidepoint(souris_pos):
        poubelle_hover = pygame.transform.smoothscale(poubelle, (75, 75))
        screen.blit(poubelle_hover, poubelle_hover.get_rect(center=poubelle_rect.center))
        if not inventaire.est_vide():
            texte = font.render("Cliquer pour trier", True, (255, 255, 255))
            screen.blit(texte, (poubelle_rect.x - 20, poubelle_rect.y - 25))
    else:
        screen.blit(poubelle, poubelle_rect)

    # ramassage avec F
    if not interface_tri.actif:
        for d in dechets_map[:]:
            if boubou_rect.colliderect(d.rect):
                texte = font.render("F pour ramasser", True, (255, 255, 255))
                screen.blit(texte, (boubou_rect.x - 20, boubou_rect.y - 30))
                if keys[pygame.K_f] and not inventaire.est_plein():
                    inventaire.ajouter(d)
                    dechets_map.remove(d)
                    pygame.time.delay(150)

    # pêche
    if boubou_rect.colliderect(peche_rect):
        texte = font.render("Appuyez sur E pour pêcher", True, (5, 5, 255))
        screen.blit(texte, (520, 260))
        if keys[pygame.K_e]:
            lancer_mini_jeu()
            pygame.time.delay(300)

    if afficher_inventaire:
        _draw_inventaire_minecraft(screen, inventaire, font)

    interface_tri.draw(screen)

    hint = font.render("TAB : inventaire", True, (180, 180, 180))
    screen.blit(hint, (1100, 10))

    pygame.display.flip()

pygame.quit()