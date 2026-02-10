import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("IceQuack")

running = True
ball_x = 320
ball_y = 240
ball_speed_x = 3
ball_speed_y = 3
ball_radius = 20

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Quand on appuie sur une touche
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                ball_y -= 10   # W = monter
            if event.key == pygame.K_s:
                ball_y += 10   # S = descendre
            if event.key == pygame.K_q:
                ball_x -= 10   # A = gauche
            if event.key == pygame.K_d:
                ball_x += 10   # D = droite

    # Effacer l’écran
    screen.fill((255, 255, 255))

    # Redessiner la balle
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)

    # Mettre à jour l’affichage
    pygame.display.flip()

pygame.quit()
