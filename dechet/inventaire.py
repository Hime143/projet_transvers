import pygame

class Inventaire:

    def __init__(self, capacite=15):
        # capacité totale de l'inventaire (5 par catégorie x 3 = 15)
        self.capacite = capacite
        # liste qui stocke les déchets ramassés
        self.contenu = []

    def ajouter(self, dechet):
        # on compte combien on a déjà de ce type de déchet
        nb_type = 0
        for d in self.contenu:
            if d.type_d == dechet.type_d:
                nb_type += 1

        # on refuse si on a déjà 5 de ce type ou si l'inventaire est plein
        if nb_type >= 5:
            return False
        if len(self.contenu) >= self.capacite:
            return False

        self.contenu.append(dechet)
        return True

    def retirer(self, dechet):
        # on retire un déchet de l'inventaire après le tri
        if dechet in self.contenu:
            self.contenu.remove(dechet)

    def est_plein(self):
        # vérifie si l'inventaire est plein
        return len(self.contenu) >= self.capacite

    def est_vide(self):
        # vérifie si l'inventaire est vide
        return len(self.contenu) == 0

    def nb_par_type(self, type_d):
        # retourne le nombre de déchets d'un type donné
        nb = 0
        for d in self.contenu:
            if d.type_d == type_d:
                nb += 1
        return nb