import pygame


class Inventaire:

    def __init__(self, capacite=15):
        self.capacite = capacite
        self.contenu = []

    def ajouter(self, dechet):
        nb_type = sum(1 for d in self.contenu if d.type_d == dechet.type_d)
        if nb_type >= 5:
            return False  # 5 max par catégorie
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