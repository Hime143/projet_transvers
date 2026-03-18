import pygame

def ecran_accueil(screen, clock, background,musique,parametre):

    font_titre = pygame.font.SysFont(None, 90)
    font_bouton = pygame.font.SysFont(None, 50)

    bouton_jouer = pygame.Rect(540, 300, 200, 70)
    bouton_quitter = pygame.Rect(540, 400, 200, 70)

    menu_ouvert = None  # None / "music" / "settings"
    volume = 0.5
    pygame.mixer.music.set_volume(volume)

    music_rect = musique.get_rect(topleft=(1150, 20))
    settings_rect = parametre.get_rect(topleft=(1050, 20))
    while True:

        screen.blit(background, (0, 0))

        titre = font_titre.render("IceGuardian", True, (5, 5, 255))
        screen.blit(titre, titre.get_rect(center=(640, 150)))

        mouse_pos = pygame.mouse.get_pos()

        couleur_jouer = (0, 200, 255) if bouton_jouer.collidepoint(mouse_pos) else (120,150,200)
        couleur_quitter = (0, 200, 255) if bouton_quitter.collidepoint(mouse_pos) else (120,150,200)

        pygame.draw.rect(screen, couleur_jouer, bouton_jouer, border_radius=10)
        pygame.draw.rect(screen, couleur_quitter, bouton_quitter, border_radius=10)

        texte_jouer = font_bouton.render("Jouer", True, (255,255,255))
        texte_quitter = font_bouton.render("Quitter", True, (255,255,255))

        screen.blit(texte_jouer, texte_jouer.get_rect(center=bouton_jouer.center))
        screen.blit(texte_quitter, texte_quitter.get_rect(center=bouton_quitter.center))

        def draw_icon(icon, rect):
            if rect.collidepoint(mouse_pos):
                scaled = pygame.transform.scale(icon, (int(rect.width * 1.2), int(rect.height * 1.2)))
                new_rect = scaled.get_rect(center=rect.center)
                screen.blit(scaled, new_rect)
                return new_rect
            else:
                screen.blit(icon, rect)
                return rect

        music_rect_hover = draw_icon(musique, music_rect)
        settings_rect_hover = draw_icon(parametre, settings_rect)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if bouton_jouer.collidepoint(event.pos):
                        return True

                    if bouton_quitter.collidepoint(event.pos):
                        return False



                    if settings_rect_hover.collidepoint(event.pos):
                        print("Menu paramètres (à faire)")

        pygame.display.flip()
        clock.tick(60)