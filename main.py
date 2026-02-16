import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("IceGuardian")

running = True
boubou_x = 320
boubou_y = 240
speed = 0.3
img_up = pygame.image.load("Images/BOUBOUHAUT.png").convert_alpha()
img_up = pygame.transform.scale(img_up, (70,128))
img_down = pygame.image.load("Images/BOUBOUVERSNOUS.png").convert_alpha()
img_down = pygame.transform.scale(img_down, (70,128))
img_left = pygame.image.load("Images/BOUBOUGAUCHE.png").convert_alpha()
img_left = pygame.transform.scale(img_left, (70,128))
img_right = pygame.image.load("Images/BOUBOUDROITE.png").convert_alpha()
img_right = pygame.transform.scale(img_right, (70,128))
boubou_img = img_down
boubou_rect = boubou_img.get_rect(center=(boubou_x,boubou_y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                boubou_y -= speed
                boubou_img = img_up
            if event.key == pygame.K_s:
                boubou_y += speed
                boubou_img = img_down
            if event.key == pygame.K_q:
                boubou_x -= speed
                boubou_img = img_left
            if event.key == pygame.K_d:
                boubou_x += speed
                boubou_img = img_right

        if boubou_y == 1280:
            boubou_y = 0
        if boubou_y == 0:
            boubou_y = 1280
        if boubou_x == 700:
            boubou_x = 0
        if boubou_x == 0:
            boubou_x = 700

    screen.fill((255, 255, 255))
    screen.blit(boubou_img, boubou_rect)
    pygame.display.flip()

pygame.quit()
