import pygame
def ecran_fin(screen, clock):

    font_titre = pygame.font.SysFont(None, 80)
    font_bouton = pygame.font.SysFont(None, 50)

    bouton_menu = pygame.Rect(540, 400, 200, 70)

    while True:

        screen.fill((10, 30, 80))

        titre = font_titre.render("Temps écoulé !", True, (255,255,255))
        screen.blit(titre, titre.get_rect(center=(640, 200)))

        mouse_pos = pygame.mouse.get_pos()

        couleur = (0,200,255) if bouton_menu.collidepoint(mouse_pos) else (120,150,200)
        pygame.draw.rect(screen, couleur, bouton_menu, border_radius=10)

        texte = font_bouton.render("Menu", True, (255,255,255))
        screen.blit(texte, texte.get_rect(center=bouton_menu.center))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_menu.collidepoint(event.pos):
                    return  # retour au menu principal

        pygame.display.flip()
        clock.tick(60)
