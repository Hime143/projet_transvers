import pygame
from temps import pause_fin , pause_debuter

# couleurs des poubelles
COULEURS = {
    "plastique": (255, 220, 0),   # jaune
    "verre":     (0, 200, 100),   # vert
    "papier":    (0, 150, 255),   # bleu
}

# position horizontale des poubelles sur l'écran
POSITIONS = {
    "plastique": 250,
    "verre":     640,
    "papier":    1030,
}


class InterfaceTri:

    def __init__(self, inventaire, font):
        self.inventaire = inventaire
        self.font = font

        # est-ce que l'interface est ouverte ?
        self.actif = False

        # score du joueur
        self.score = 0

        # message affiché après un tri (bon ou mauvais)
        self.feedback = None
        self.feedback_timer = 0

        # timer de 30 secondes pour trier
        self.temps_total = 30 * 60
        self.temps_restant = self.temps_total

        # on crée les rectangles de chaque poubelle
        self.rects_poubelles = {}
        for cat in POSITIONS:
            self.rects_poubelles[cat] = pygame.Rect(
                POSITIONS[cat] - 70,
                250,
                140,
                180
            )
        # chargement des images des poubelles
        self.images_poubelles = {
            "plastique": pygame.transform.smoothscale(
                pygame.image.load("Images/poubelle_jaune.png").convert_alpha(), (140, 280)
            ),
            "verre": pygame.transform.smoothscale(
                pygame.image.load("Images/poubelle_verte.png").convert_alpha(), (140, 280)
            ),
            "papier": pygame.transform.smoothscale(
                pygame.image.load("Images/poubelle_bleu.png").convert_alpha(), (140, 280)
            ),
        }

    def ouvrir(self):
        # ouvre l'interface et remet le timer à zéro
        self.actif = True
        self.temps_restant = self.temps_total
        pause_debuter()

    def fermer(self):
        # ferme l'interface
        self.actif = False
        self.feedback = None
        pause_fin()

    def trier(self, categorie_choisie):
        # si l'inventaire est vide on ferme
        if self.inventaire.est_vide():
            self.fermer()
            return

        # on prend le premier déchet de l'inventaire
        dechet = self.inventaire.contenu[0]

        # bon tri → +10 points, mauvais tri → -5 points
        if categorie_choisie == dechet.type_d:
            self.score += 10
            self.feedback = ("Bien trié ! +10", (80, 220, 100))
        else:
            self.score -= 5
            self.feedback = (f"Mauvais tri ! -5  (c'était {dechet.type_d})", (220, 80, 80))

        # on affiche le feedback pendant 90 frames (1.5 secondes)
        self.feedback_timer = 90

        # on retire le déchet de l'inventaire
        self.inventaire.retirer(dechet)

        # si l'inventaire est vide on ferme
        if self.inventaire.est_vide():
            self.fermer()

    def gerer_clic(self, pos):
        # on vérifie sur quelle poubelle le joueur a cliqué
        for categorie in self.rects_poubelles:
            if self.rects_poubelles[categorie].collidepoint(pos):
                self.trier(categorie)

    def update(self):
        # on met à jour le timer à chaque frame
        if not self.actif:
            return

        self.temps_restant -= 1

        if self.feedback_timer > 0:
            self.feedback_timer -= 1

        # temps écoulé → on ferme
        if self.temps_restant <= 0:
            self.fermer()

    def draw(self, screen):
        # on n'affiche rien si l'interface est fermée
        if not self.actif:
            return

        # fond noir semi-transparent
        overlay = pygame.Surface((1280, 700), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # titre
        titre = self.font.render("Trie tes déchets !", True, (255, 255, 255))
        screen.blit(titre, titre.get_rect(center=(640, 60)))

        # déchet à trier affiché au centre
        if not self.inventaire.est_vide():
            dechet = self.inventaire.contenu[0]
            img = pygame.transform.smoothscale(dechet.image, (100, 100))
            screen.blit(img, img.get_rect(center=(640, 170)))
            nom = self.font.render(dechet.type_d.capitalize(), True, (255, 255, 255))
            screen.blit(nom, nom.get_rect(center=(640, 230)))

        # on dessine les 3 poubelles avec les vraies images
        for cat in self.rects_poubelles:
            rect = self.rects_poubelles[cat]
            # image à la place du rectangle coloré
            screen.blit(self.images_poubelles[cat], rect)
            # label en dessous
            label = self.font.render(cat.capitalize(), True, (255, 255, 255))
            screen.blit(label, label.get_rect(center=(rect.centerx, rect.bottom + 20)))

        # message bon/mauvais tri
        if self.feedback is not None and self.feedback_timer > 0:
            texte_fb = self.font.render(self.feedback[0], True, self.feedback[1])
            screen.blit(texte_fb, texte_fb.get_rect(center=(640, 460)))

        # score
        texte_score = self.font.render(f"Score tri : {self.score}", True, (255, 255, 255))
        screen.blit(texte_score, (20, 20))

        # barre de temps
        secondes = self.temps_restant // 60
        largeur = int(400 * self.temps_restant / self.temps_total)

        if secondes > 15:
            couleur_barre = (80, 220, 100)   # vert
        elif secondes > 7:
            couleur_barre = (255, 200, 0)    # jaune
        else:
            couleur_barre = (255, 60, 60)    # rouge

        pygame.draw.rect(screen, (30, 30, 60),   pygame.Rect(440, 20, 400, 22), border_radius=10)
        pygame.draw.rect(screen, couleur_barre,  pygame.Rect(440, 20, largeur, 22), border_radius=10)
        pygame.draw.rect(screen, (150, 150, 200), pygame.Rect(440, 20, 400, 22), 2, border_radius=10)

        texte_temps = self.font.render(f"{secondes}s", True, (200, 220, 255))
        screen.blit(texte_temps, (848, 22))