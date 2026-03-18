import pygame


class Inventaire:

    def __init__(self, capacite=5):
        self.capacite = capacite
        self.contenu = []

    def ajouter(self, dechet):
        if len(self.contenu) < self.capacite:
            self.contenu.append(dechet)
            return True
        return False

    def retirer(self, dechet):
        if dechet in self.contenu:
            self.contenu.remove(dechet)

    def est_plein(self):
        return len(self.contenu) >= self.capacite

    def est_vide(self):
        return len(self.contenu) == 0