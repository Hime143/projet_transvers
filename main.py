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
ball_x += ball_speed_x
ball_y += ball_speed_y
screen.fill((255,255,255))
pygame.draw.circle(screen, (255,0,0), (ball_x, ball_y), ball_radius)
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: