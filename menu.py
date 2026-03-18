# menu.py
import pygame

def draw_popup(screen, type_menu, volume, mouse_pos):
    """
    Dessine l'overlay + la fenêtre centrale et retourne (close_rect, bar_rect_or_None).
    Ne modifie pas le volume ici — juste l'affichage.
    """

    # overlay semi-transparent
    overlay = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))  # RGBA (150 = alpha)
    screen.blit(overlay, (0, 0))

    # fenêtre centrale
    sw, sh = screen.get_size()
    rect = pygame.Rect(sw//2 - 300, sh//2 - 200, 600, 400)
    pygame.draw.rect(screen, (30, 30, 60), rect, border_radius=15)
    pygame.draw.rect(screen, (100, 100, 200), rect, 3, border_radius=15)

    # polices
    font = pygame.font.SysFont(None, 46)
    font_small = pygame.font.SysFont(None, 32)

    # bouton fermer (X)
    close_rect = pygame.Rect(rect.right - 50, rect.y + 10, 40, 40)
    pygame.draw.rect(screen, (200, 80, 80), close_rect, border_radius=8)
    txt = font_small.render("X", True, (255,255,255))
    screen.blit(txt, txt.get_rect(center=close_rect.center))

    if type_menu == "music":
        # titre
        titre = font.render("Musique", True, (255,255,255))
        screen.blit(titre, titre.get_rect(center=(sw//2, rect.y + 60)))

        # barre de volume
        bar_w = 400
        bar_h = 20
        bar_x = sw//2 - bar_w//2
        bar_y = rect.y + 160
        bar_rect = pygame.Rect(bar_x, bar_y, bar_w, bar_h)

        pygame.draw.rect(screen, (80,80,120), bar_rect, border_radius=10)  # fond barre

        fill_w = int(volume * bar_w)
        if fill_w > 0:
            pygame.draw.rect(screen, (0,200,255), (bar_x, bar_y, fill_w, bar_h), border_radius=10)

        # curseur cercle
        cursor_x = bar_x + fill_w
        pygame.draw.circle(screen, (255,255,255), (cursor_x, bar_y + bar_h//2), 10)

        # valeur texte
        val_txt = font_small.render(f"{int(volume*100)}%", True, (200,200,255))
        screen.blit(val_txt, val_txt.get_rect(center=(sw//2, bar_y + 60)))

        return close_rect, bar_rect

    elif type_menu == "settings":
        titre = font.render("Paramètres", True, (255,255,255))
        screen.blit(titre, titre.get_rect(center=(sw//2, rect.y + 60)))

        txt = font_small.render("Options à venir...", True, (200,200,200))
        screen.blit(txt, txt.get_rect(center=(sw//2, rect.y + 180)))

        return close_rect, None


def ecran_accueil(screen, clock, background, musique, parametre):
    """
    Affiche le menu principal. Retourne True si on lance le jeu, False si on quitte.
    - musique: surface icône musique
    - parametre: surface icône paramètres
    """

    # polices et boutons
    font_titre = pygame.font.SysFont(None, 90)
    font_bouton = pygame.font.SysFont(None, 50)

    sw, sh = screen.get_size()
    bouton_jouer = pygame.Rect(sw//2 - 100, 300, 200, 70)
    bouton_quitter = pygame.Rect(sw//2 - 100, 400, 200, 70)

    # état popup
    menu_ouvert = None  # None / "music" / "settings"
    volume = 0.5
    pygame.mixer.music.set_volume(volume)

    # icônes (positions)
    music_rect = musique.get_rect(topleft=(sw - 130, 20))
    settings_rect = parametre.get_rect(topleft=(sw - 220, 20))

    dragging = False  # pour slider
    bar_rect = None   # rectangle de la barre (mis à jour quand popup ouvert)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        # --- DESSIN DE FOND et UI ---
        screen.blit(background, (0, 0))

        # titre
        titre = font_titre.render("IceGuardian", True, (255, 255, 255))
        screen.blit(titre, titre.get_rect(center=(sw//2, 150)))

        # boutons classiques
        couleur_jouer = (0, 200, 255) if bouton_jouer.collidepoint(mouse_pos) else (120,150,200)
        couleur_quitter = (0, 200, 255) if bouton_quitter.collidepoint(mouse_pos) else (120,150,200)

        pygame.draw.rect(screen, couleur_jouer, bouton_jouer, border_radius=10)
        pygame.draw.rect(screen, couleur_quitter, bouton_quitter, border_radius=10)

        texte_jouer = font_bouton.render("Jouer", True, (255,255,255))
        texte_quitter = font_bouton.render("Quitter", True, (255,255,255))

        screen.blit(texte_jouer, texte_jouer.get_rect(center=bouton_jouer.center))
        screen.blit(texte_quitter, texte_quitter.get_rect(center=bouton_quitter.center))

        # --- icônes avec effet hover (zoom) ---
        def draw_icon(icon, rect):
            if rect.collidepoint(mouse_pos):
                scaled = pygame.transform.smoothscale(icon, (int(rect.width * 1.2), int(rect.height * 1.2)))
                new_rect = scaled.get_rect(center=rect.center)
                screen.blit(scaled, new_rect)
                return new_rect
            else:
                screen.blit(icon, rect)
                return rect

        music_rect_hover = draw_icon(musique, music_rect)
        settings_rect_hover = draw_icon(parametre, settings_rect)

        # --- si popup ouvert, on le dessine maintenant (avant de traiter les events)
        close_rect = None
        bar_rect = None
        if menu_ouvert:
            close_rect, bar_rect = draw_popup(screen, menu_ouvert, volume, mouse_pos)

        # --- EVENTS ---
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            # clic souris
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # boutons principaux (si popup fermé)
                if not menu_ouvert:
                    if bouton_jouer.collidepoint(event.pos):
                        return True
                    if bouton_quitter.collidepoint(event.pos):
                        return False

                    # ouvrir popup en cliquant sur icônes
                    if music_rect_hover.collidepoint(event.pos):
                        menu_ouvert = "music"
                    elif settings_rect_hover.collidepoint(event.pos):
                        menu_ouvert = "settings"

                else:
                    # si popup ouvert, gérer fermeture et barre
                    if close_rect and close_rect.collidepoint(event.pos):
                        menu_ouvert = None
                    elif menu_ouvert == "music" and bar_rect and bar_rect.collidepoint(event.pos):
                        # commencer drag / définir directement le volume
                        dragging = True
                        volume = (event.pos[0] - bar_rect.x) / bar_rect.width
                        volume = max(0.0, min(1.0, volume))
                        pygame.mixer.music.set_volume(volume)

            # relâchement souris -> stop drag
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = False

            # mouvement souris pendant drag -> mise à jour du volume
            if event.type == pygame.MOUSEMOTION:
                if dragging and menu_ouvert == "music" and bar_rect:
                    mx = event.pos[0]
                    volume = (mx - bar_rect.x) / bar_rect.width
                    volume = max(0.0, min(1.0, volume))
                    pygame.mixer.music.set_volume(volume)

            # touche clavier (ex : echap ferme popup)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and menu_ouvert:
                    menu_ouvert = None

        pygame.display.flip()
        clock.tick(60)