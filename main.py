import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("IceGuardian")
clock = pygame.time.Clock()
running = True
speed = 3

background = pygame.image.load("Images/Banquise.png").convert_alpha()
background = pygame.transform.scale(background, (1280,700))

collison_map = pygame.image.load("Images/collision_map.png").convert_alpha()
collison_map = pygame.transform.scale(collison_map, (1280,700))
img_up = pygame.image.load("Images/BOUBOUHAUT.png").convert_alpha()
img_up = pygame.transform.scale(img_up, (70,128))

img_down = pygame.image.load("Images/BOUBOUVERSNOUS.png").convert_alpha()
img_down = pygame.transform.scale(img_down, (70,128))

img_left = pygame.image.load("Images/BOUBOUGAUCHE.png").convert_alpha()
img_left = pygame.transform.scale(img_left, (70,128))

img_right = pygame.image.load("Images/BOUBOUDROITE.png").convert_alpha()
img_right = pygame.transform.scale(img_right, (70,128))

boubou_img = img_down

img_up1 = pygame.image.load("Images/BOUBOUDERRIERE1.png").convert_alpha()
img_up1 = pygame.transform.scale(img_up1, (70,128))

img_up2 = pygame.image.load("Images/BOUBOUDERRIERE2.png").convert_alpha()
img_up2 = pygame.transform.scale(img_up2, (70,128))

img_down1 = pygame.image.load("Images/BOUBOUDEVANT1.png").convert_alpha()
img_down1 = pygame.transform.scale(img_down1, (70,128))

img_down2 = pygame.image.load("Images/BOUBOUDEVANT2.png").convert_alpha()
img_down2 = pygame.transform.scale(img_down2, (70,128))

img_left1 = pygame.image.load("Images/BOUBOUGAUCHE1.png").convert_alpha()
img_left1 = pygame.transform.scale(img_left1, (70,128))

img_left2 = pygame.image.load("Images/BOUBOUGAUCHE2.png").convert_alpha()
img_left2 = pygame.transform.scale(img_left2, (70,128))

img_right1 = pygame.image.load("Images/BOUBOUDROITE1.png").convert_alpha()
img_right1 = pygame.transform.scale(img_right1, (70,128))

img_right2 = pygame.image.load("Images/BOUBOUDROITE2.png").convert_alpha()
img_right2 = pygame.transform.scale(img_right2, (70,128))

boubou_rect = boubou_img.get_rect(center=(640, 350))

direction = "down"
frame_index = 0
animation_timer = 0
animation_speed = 20
moving = False
while running:
    moving = False
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_z] or keys[pygame.K_UP]:
        old_y = boubou_rect.y
        boubou_rect.y -= speed
        direction = "up"
        moving = True

        foot_x = boubou_rect.centerx
        foot_y = boubou_rect.bottom

        if collison_map.get_at((foot_x, foot_y))[:3] == (0, 0, 0):
            boubou_rect.y = old_y

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        old_y = boubou_rect.y
        boubou_rect.y += speed
        direction = "down"
        moving = True

        foot_x = boubou_rect.centerx
        foot_y = boubou_rect.bottom

        if collison_map.get_at((foot_x, foot_y))[:3] == (0, 0, 0):
            boubou_rect.y = old_y

    if keys[pygame.K_q] or keys[pygame.K_LEFT]:
        old_x = boubou_rect.x
        boubou_rect.x -= speed
        direction = "left"
        moving = True

        foot_x = boubou_rect.centerx
        foot_y = boubou_rect.bottom

        if collison_map.get_at((foot_x, foot_y))[:3] == (0, 0, 0):
            boubou_rect.x = old_x

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        old_x = boubou_rect.x
        boubou_rect.x += speed
        direction = "right"
        moving = True

        foot_x = boubou_rect.centerx
        foot_y = boubou_rect.bottom

        if collison_map.get_at((foot_x, foot_y))[:3] == (0, 0, 0):
            boubou_rect.x = old_x

    if moving:
        animation_timer += 1
        if animation_timer >= animation_speed:
            animation_timer = 0

            if direction == "up":
                frames = [img_up1, img_up2]
            elif direction == "down":
                frames = [img_down1, img_down2]
            elif direction == "left":
                frames = [img_left1, img_left2]
            elif direction == "right":
                frames = [img_right1, img_right2]

            frame_index = (frame_index + 1) % len(frames)
            boubou_img = frames[frame_index]
    else:
        if direction == "up":
            boubou_img = img_up
        elif direction == "down":
            boubou_img = img_down
        elif direction == "left":
            boubou_img = img_left
        elif direction == "right":
            boubou_img = img_right

    screen.blit(background, (0,0))
    screen.blit(boubou_img, boubou_rect)
    pygame.display.flip()

pygame.quit()
