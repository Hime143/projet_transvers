import pygame

screen = pygame.display.set_mode((1000, 500))
class player :
    def __init__(self,x,y) :
        self.velocity = [0,0]
        self.speed = 5
        self.image = pygame.image.load('Images/BOUBOUVERSNOUS.png')
        pygame.transform.scale(self.image, (80, 138))
        self.rect = self.image.get_rect(x=x,y=y)
        self.inventaire = []

    def move(self) :
        self.rect.move_ip(self.velocity[0]*self.speed,self.velocity[1]*self.speed)

    def draw(self,screenu) :
        screen.blit(pygame.transform.scale(self.image, (80, 138)),self.rect)