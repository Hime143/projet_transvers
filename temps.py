import pygame

temps_depart       = pygame.time.get_ticks()
duree_partie       = 300
temps_pause_total  = 0
pause_debut        = 0
multiplicateur_temps = 1.0

def init_timer():
    global temps_depart, temps_pause_total
    temps_depart = pygame.time.get_ticks()
    temps_pause_total = 0


def get_temps_restant():
    temps_actuel = pygame.time.get_ticks()
    temps_ecoule = (temps_actuel - temps_depart - temps_pause_total)
    temps_ecoule *= multiplicateur_temps
    temps_ecoule = int(temps_ecoule // 1000)
    return max(0, duree_partie - temps_ecoule)


def pause_debuter():
    global pause_debut
    pause_debut = pygame.time.get_ticks()


def pause_fin():
    global temps_pause_total
    pause_fin = pygame.time.get_ticks()
    temps_pause_total += (pause_fin - pause_debut)


temps_down_peche_depart = 0
temps_down_peche_duree = 60
peche_recent = False


def lancer_cooldown_peche():
    global peche_recent, temps_down_peche_depart
    peche_recent = True
    temps_down_peche_depart = pygame.time.get_ticks()


def get_cooldown_peche():
    if not peche_recent:
        return 0

    temps_actuel = pygame.time.get_ticks()
    temps_ecoule = (temps_actuel - temps_down_peche_depart) // 1000
    restant = max(0, temps_down_peche_duree - temps_ecoule)

    return restant


def update_cooldown_peche():
    global peche_recent
    if peche_recent and get_cooldown_peche() <= 0:
        peche_recent = False

def set_multiplicateur(valeur):
    global multiplicateur_temps
    multiplicateur_temps = valeur