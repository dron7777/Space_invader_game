import pygame
pygame.init()
screen =pygame.display.set_mode((1280, 660))
background = pygame.image.load("stains_light_color_47319_1280x720.jpg")
man = pygame.image.load("hk.png")
man_x=1100
man_y=660

def man_hat(x,y):
    screen.blit(man,(x,y))
running =True
while running:
    screen.blit(background, (0, 0))
    while man_y!=400:
        man_y-=20
        man_hat(man_x, man_y)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


    pygame.display.update()