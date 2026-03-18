import pygame

def ecran_accueil(screen, clock, background):

    font_titre = pygame.font.SysFont(None, 90)
    font_bouton = pygame.font.SysFont(None, 50)

    bouton_jouer = pygame.Rect(540, 300, 200, 70)
    bouton_quitter = pygame.Rect(540, 400, 200, 70)

    while True:

        screen.blit(background, (0, 0))

        titre = font_titre.render("IceGuardian", True, (255, 255, 255))
        screen.blit(titre, titre.get_rect(center=(640, 150)))

        mouse_pos = pygame.mouse.get_pos()

        couleur_jouer = (0, 200, 255) if bouton_jouer.collidepoint(mouse_pos) else (0,150,255)
        couleur_quitter = (255, 80, 80) if bouton_quitter.collidepoint(mouse_pos) else (200,50,50)

        pygame.draw.rect(screen, couleur_jouer, bouton_jouer, border_radius=10)
        pygame.draw.rect(screen, couleur_quitter, bouton_quitter, border_radius=10)

        texte_jouer = font_bouton.render("Jouer", True, (255,255,255))
        texte_quitter = font_bouton.render("Quitter", True, (255,255,255))

        screen.blit(texte_jouer, texte_jouer.get_rect(center=bouton_jouer.center))
        screen.blit(texte_quitter, texte_quitter.get_rect(center=bouton_quitter.center))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if bouton_jouer.collidepoint(event.pos):
                        return True

                    if bouton_quitter.collidepoint(event.pos):
                        return False

        pygame.display.flip()
        clock.tick(60)