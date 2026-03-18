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

if not ecran_accueil(screen, clock, background, musique, parametre):
    pygame.quit()
    exit()

# positions des éléments sur la map
boubou_rect        = boubou_img.get_rect(center=(640, 350))
maison_rect        = maison.get_rect(center=(240, 150))
peche_rect         = peche.get_rect(center=(540, 300))
poubelle_rect      = poubelle.get_rect(center=(970, 250))
poubelle_bleu_rect  = poubelle_bleu.get_rect(center=(970, 170))
poubelle_verte_rect = poubelle_verte.get_rect(center=(900, 170))
poubelle_jaune_rect = poubelle_jaune.get_rect(center=(1040, 170))

# déchets et inventaire
inventaire    = Inventaire(capacite=15)
interface_tri = InterfaceTri(inventaire, font)
dechets_map   = [Dechet(collision_map) for _ in range(3)]

# timer spawn déchets toutes les 12s
spawn_timer    = 0
spawn_interval = 12 * 60

# animation boubou
direction      = "down"
frame_index    = 0
animation_timer = 0
animation_speed = 20
moving         = False

# inventaire visible ou non
afficher_inventaire = False


def draw_inventaire(screen, inventaire, font):
    """Affiche l'inventaire style Minecraft quand on appuie sur TAB"""

    # fond semi-transparent
    overlay = pygame.Surface((1280, 700), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    # fenêtre inventaire
    fenetre_w = 700
    fenetre_h = 500
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

    # on trie les déchets par catégorie
    categories = {"plastique": [], "verre": [], "papier": []}
    for d in inventaire.contenu:
        categories[d.type_d].append(d)

    COULEURS_LABEL = {
        "plastique": (255, 220, 0),
        "verre":     (0, 200, 120),
        "papier":    (100, 180, 255),
    }

    taille_slot = 90
    marge       = 14
    y_depart    = fenetre_y + 70

    for ligne, type_d in enumerate(categories):
        liste = categories[type_d]
        y     = y_depart + ligne * (taille_slot + marge + 30)

        # label de la catégorie
        label = font.render(f"{type_d.capitalize()} :", True, COULEURS_LABEL[type_d])
        screen.blit(label, (fenetre_x + 20, y))

        # slots des déchets
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

        # compteur x/5
        font_nb = pygame.font.SysFont(None, 26)
        nb_txt  = font_nb.render(f"{len(liste)}/5", True, (200, 200, 200))
        screen.blit(nb_txt, (fenetre_x + fenetre_w - 80, y + 40))

    hint = font.render("TAB pour fermer", True, (150, 150, 150))
    screen.blit(hint, hint.get_rect(center=(fenetre_x + fenetre_w // 2,
                                             fenetre_y + fenetre_h - 20)))


# --- boucle principale ---
while running:

    moving = False
    clock.tick(60)
    souris_pos = pygame.mouse.get_pos()

    # spawn un déchet toutes les 12s (max 6 sur la map)
    spawn_timer += 1
    if spawn_timer >= spawn_interval and len(dechets_map) < 6:
        spawn_timer = 0
        dechets_map.append(Dechet(collision_map))

    # --- événements ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                afficher_inventaire = not afficher_inventaire

        if event.type == pygame.MOUSEBUTTONDOWN:
            # clic sur la poubelle icône → ouvre le tri
            if poubelle_rect.collidepoint(souris_pos) and not inventaire.est_vide():
                interface_tri.ouvrir()
            # clic dans l'interface de tri
            if interface_tri.actif:
                interface_tri.gerer_clic(souris_pos)

    keys = pygame.key.get_pressed()

    # --- mouvements boubou ---
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

    # --- animation boubou ---
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
            boubou_img  = frames[frame_index]
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

    # --- affichage ---
    screen.blit(background, (0, 0))

    # déchets sur la map
    for d in dechets_map:
        d.draw(screen)

    # boubou et icônes
    screen.blit(boubou_img,      boubou_rect)
    screen.blit(maison,          maison_rect)
    screen.blit(peche,           peche_rect)
    screen.blit(poubelle_bleu,   poubelle_bleu_rect)
    screen.blit(poubelle_jaune,  poubelle_jaune_rect)
    screen.blit(poubelle_verte,  poubelle_verte_rect)

    # icône poubelle avec effet survol
    if poubelle_rect.collidepoint(souris_pos):
        poubelle_hover = pygame.transform.smoothscale(poubelle, (75, 75))
        screen.blit(poubelle_hover, poubelle_hover.get_rect(center=poubelle_rect.center))
        if not inventaire.est_vide():
            texte = font.render("Cliquer pour trier", True, (255, 255, 255))
            screen.blit(texte, (poubelle_rect.x - 20, poubelle_rect.y - 25))
    else:
        screen.blit(poubelle, poubelle_rect)

    # --- ramassage déchet avec F ---
    if not interface_tri.actif:
        for d in dechets_map[:]:
            if boubou_rect.colliderect(d.rect):
                nb_type = inventaire.nb_par_type(d.type_d)
                if nb_type >= 5:
                    texte = font.render(f"Plein pour {d.type_d} !", True, (255, 100, 100))
                else:
                    texte = font.render("F pour ramasser", True, (255, 255, 255))
                screen.blit(texte, (boubou_rect.x - 20, boubou_rect.y - 30))
                if keys[pygame.K_f] and nb_type < 5:
                    inventaire.ajouter(d)
                    dechets_map.remove(d)
                    pygame.time.delay(150)

    # --- mini-jeu pêche ---
    if boubou_rect.colliderect(peche_rect):
        texte = font.render("E pour pêcher", True, (5, 5, 255))
        screen.blit(texte, (520, 260))
        if keys[pygame.K_e]:
            lancer_mini_jeu()
            pygame.time.delay(300)

    # inventaire TAB
    if afficher_inventaire:
        draw_inventaire(screen, inventaire, font)

    # interface de tri
    interface_tri.draw(screen)

    # hint TAB
    hint = font.render("TAB : inventaire", True, (180, 180, 180))
    screen.blit(hint, (1100, 10))

    pygame.display.flip()

pygame.quit()