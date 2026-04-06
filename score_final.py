import pygame

SEUIL_BRONZE = 100
SEUIL_ARGENT = 200
SEUIL_OR     = 350


def calculer_medaille(score_total):
    if score_total >= SEUIL_OR:
        return "or"
    elif score_total >= SEUIL_ARGENT:
        return "argent"
    elif score_total >= SEUIL_BRONZE:
        return "bronze"
    else:
        return "normal"


def ecran_score_final(screen, clock, score_peche, score_tri, nb_dechets):

    font_titre  = pygame.font.SysFont(None, 80)
    font_grand  = pygame.font.SysFont(None, 46)
    font        = pygame.font.SysFont(None, 34)
    font_petit  = pygame.font.SysFont(None, 28)

    score_total = score_peche + score_tri + (nb_dechets * 5)
    medaille    = calculer_medaille(score_total)

    img_or     = pygame.image.load("Images/medaille_or.png").convert_alpha()
    img_argent = pygame.image.load("Images/medaille_argent.png").convert_alpha()
    img_bronze = pygame.image.load("Images/medaille_bronze.png").convert_alpha()

    img_or = pygame.transform.smoothscale(img_or, (280, 120))
    img_argent = pygame.transform.smoothscale(img_argent, (240,95))
    img_bronze = pygame.transform.smoothscale(img_bronze, (210, 75))

    if medaille == "or":
        couleur_msg   = (255, 200, 0)
        msg_principal = "Médaille d'OR !"
        msg_encourage = "Félicitations ! Tu as atteint le plus haut niveau !"
    elif medaille == "argent":
        couleur_msg   = (200, 200, 200)
        msg_principal = "Médaille d'ARGENT !"
        msg_encourage = f"Encore {SEUIL_OR - score_total} points pour décrocher l'OR !"
    elif medaille == "bronze":
        couleur_msg   = (180, 100, 30)
        msg_principal = "Médaille de BRONZE !"
        msg_encourage = f"Encore {SEUIL_ARGENT - score_total} points pour l'ARGENT !"
    else:
        couleur_msg   = (150, 200, 255)
        msg_principal = "On peut faire mieux !"
        msg_encourage = f"Encore {SEUIL_BRONZE - score_total} points pour le BRONZE, allez !"

    bouton_menu = pygame.Rect(540, 630, 200, 60)

    while True:

        screen.fill((10, 30, 80))

        # titre
        titre = font_titre.render("Fin de partie !", True, (255, 255, 255))
        screen.blit(titre, titre.get_rect(center=(640, 45)))

        # images des médailles au dessus des socles
        screen.blit(img_or,     img_or.get_rect(center=(640, 175)))
        screen.blit(img_argent, img_argent.get_rect(center=(445, 215)))
        screen.blit(img_bronze, img_bronze.get_rect(center=(835, 240)))

        # socles du podium
        pygame.draw.rect(screen, (255, 200, 0),   pygame.Rect(555, 280, 170, 130), border_radius=6)
        pygame.draw.rect(screen, (180, 180, 180), pygame.Rect(370, 310, 150, 100), border_radius=6)
        pygame.draw.rect(screen, (160, 90, 30),   pygame.Rect(760, 330, 150, 80),  border_radius=6)

        # numéros sur les socles
        nb1 = font_grand.render("1", True, (80, 60, 0))
        nb2 = font_grand.render("2", True, (60, 60, 60))
        nb3 = font_grand.render("3", True, (80, 40, 10))
        screen.blit(nb1, nb1.get_rect(center=(640, 340)))
        screen.blit(nb2, nb2.get_rect(center=(445, 355)))
        screen.blit(nb3, nb3.get_rect(center=(835, 365)))

        # message médaille
        msg = font_grand.render(msg_principal, True, couleur_msg)
        screen.blit(msg, msg.get_rect(center=(640, 440)))

        # message encouragement
        enc = font.render(msg_encourage, True, (180, 210, 255))
        screen.blit(enc, enc.get_rect(center=(640, 480)))

        # scores détaillés
        details = font_petit.render(
            f"Pêche : {score_peche} pts   Tri : {score_tri} pts   Déchets : {nb_dechets * 5} pts   Total : {score_total} pts",
            True, (140, 160, 200)
        )
        screen.blit(details, details.get_rect(center=(640, 520)))

        # seuils
        seuils = font_petit.render(
            f"Bronze : {SEUIL_BRONZE}  |  Argent : {SEUIL_ARGENT}  |  Or : {SEUIL_OR}",
            True, (100, 120, 170)
        )
        screen.blit(seuils, seuils.get_rect(center=(640, 550)))

        # bouton menu
        mouse_pos   = pygame.mouse.get_pos()
        couleur_btn = (0, 200, 255) if bouton_menu.collidepoint(mouse_pos) else (120, 150, 200)
        pygame.draw.rect(screen, couleur_btn, bouton_menu, border_radius=10)
        texte_btn = font.render("Menu", True, (255, 255, 255))
        screen.blit(texte_btn, texte_btn.get_rect(center=bouton_menu.center))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_menu.collidepoint(event.pos):
                    return

        pygame.display.flip()
        clock.tick(60)