import pygame


COULEURS = {
    "plastique": (255, 220, 0),
    "verre":     (0, 200, 100),
    "papier":    (0, 150, 255),
}

POSITIONS = {
    "plastique": 250,
    "verre":     640,
    "papier":    1030,
}


class InterfaceTri:

    def __init__(self, inventaire, font):
        self.inventaire = inventaire
        self.font = font
        self.actif = False
        self.score = 0
        self.feedback = None
        self.feedback_timer = 0

        self.temps_total = 30 * 60
        self.temps_restant = self.temps_total

        self.rects_poubelles = {
            cat: pygame.Rect(POSITIONS[cat] - 70, 250, 140, 180)
            for cat in POSITIONS
        }

    def ouvrir(self):
        self.actif = True
        self.temps_restant = self.temps_total

    def fermer(self):
        self.actif = False
        self.feedback = None

    def trier(self, categorie_choisie):
        if self.inventaire.est_vide():
            self.fermer()
            return

        dechet = self.inventaire.contenu[0]

        if categorie_choisie == dechet.type_d:
            self.score += 10
            self.feedback = ("Bien trié ! +10", (80, 220, 100))
        else:
            self.score -= 5
            self.feedback = (f"Mauvais tri ! -5  (c'était {dechet.type_d})", (220, 80, 80))

        self.feedback_timer = 90
        self.inventaire.retirer(dechet)

        if self.inventaire.est_vide():
            self.fermer()

    def gerer_clic(self, pos):
        for categorie, rect in self.rects_poubelles.items():
            if rect.collidepoint(pos):
                self.trier(categorie)

    def update(self):
        if not self.actif:
            return
        self.temps_restant -= 1
        if self.feedback_timer > 0:
            self.feedback_timer -= 1
        if self.temps_restant <= 0:
            self.fermer()

    def draw(self, screen):
        if not self.actif:
            return

        overlay = pygame.Surface((1280, 700), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        titre = self.font.render("Trie tes déchets !", True, (255, 255, 255))
        screen.blit(titre, titre.get_rect(center=(640, 60)))

        if not self.inventaire.est_vide():
            dechet = self.inventaire.contenu[0]
            img = pygame.transform.smoothscale(dechet.image, (100, 100))
            screen.blit(img, img.get_rect(center=(640, 170)))
            nom = self.font.render(dechet.type_d.capitalize(), True, (255, 255, 255))
            screen.blit(nom, nom.get_rect(center=(640, 230)))

        for cat, rect in self.rects_poubelles.items():
            pygame.draw.rect(screen, COULEURS[cat], rect, border_radius=12)
            label = self.font.render(cat.capitalize(), True, (0, 0, 0))
            screen.blit(label, label.get_rect(center=(rect.centerx, rect.bottom + 20)))

        if self.feedback and self.feedback_timer > 0:
            texte_fb = self.font.render(self.feedback[0], True, self.feedback[1])
            screen.blit(texte_fb, texte_fb.get_rect(center=(640, 460)))

        texte_score = self.font.render(f"Score tri : {self.score}", True, (255, 255, 255))
        screen.blit(texte_score, (20, 20))

        secondes = self.temps_restant // 60
        largeur = int(400 * self.temps_restant / self.temps_total)
        couleur_barre = (
            (80, 220, 100) if secondes > 15
            else (255, 200, 0) if secondes > 7
            else (255, 60, 60)
        )
        pygame.draw.rect(screen, (30, 30, 60),  pygame.Rect(440, 20, 400, 22), border_radius=10)
        pygame.draw.rect(screen, couleur_barre, pygame.Rect(440, 20, largeur, 22), border_radius=10)
        pygame.draw.rect(screen, (150, 150, 200), pygame.Rect(440, 20, 400, 22), 2, border_radius=10)
        texte_temps = self.font.render(f"{secondes}s", True, (200, 220, 255))
        screen.blit(texte_temps, (848, 22))
