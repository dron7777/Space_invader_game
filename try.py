import pygame
from pygame import mixer
import random
import math
pygame.init()

screen = pygame.display.set_mode((1280, 660))
caption = pygame.display.set_caption("Shagoto")
icon = pygame.image.load("dalmatian (1).png")
pygame.display.set_icon(icon)
background = pygame.image.load("maxresdefault.jpg")
mixer.music.load("background.wav")
mixer.music.play(-1)
player1 = pygame.image.load("spaceship.png")
px = 650
py = 500
enemypic=[]
ex=[]
ey=[]
e_xchange=[]
e_ychange=[]
enemy_num=6
for i in range(enemy_num):
    enemypic.append(pygame.image.load("character.png"))
    ex.append(random.randint(0, 1275))
    ey.append(random.randint(0, 350))
    e_xchange.append(0.7)
    e_ychange.append(40)

bullet=pygame.image.load("bullet (2).png")
bx=0
by=500

pchange = 0
bex=0
bey=5
bstate="ready"
score=0
font=pygame.font.Font("MontserratAlternates-Black.otf",32)
tx=0
ty=0
font=pygame.font.Font("MontserratAlternates-Black.otf",32)
tez=pygame.font.Font("MontserratAlternates-Black.otf",500)

def show_score(x,y):
    scor=font.render("Score : "+str(score),True,(255,255,255))
    screen.blit(scor,(x,y))
def player(x, y):
    screen.blit(player1, (x, y))


def enemy(x, y,i):
    print("i am enemy", flush=True )
    screen.blit(enemypic[i], (x,y))

def bullets( x,y):
    global bstate
    bstate="fire"
    screen.blit(bullet,(x+16,y+10))
def isCollision(ex,ey,bx,by):
    a=ex-bx
    b=ey-by
    dis=math.sqrt((math.pow(a,2))+(math.pow(b,2)))
    if dis < 27 :
        return True
    else:
        return  False

def game_over_text():
    text = font.render("GAME OVER  " , True, (255, 255, 255))
    screen.blit(text,(500,300))


running = True
while running:
    screen.fill((69, 169, 169))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pchange -= 0.8
            if event.key == pygame.K_RIGHT:
                pchange += 0.8
            if event.key == pygame.K_SPACE:
                b=mixer.Sound("laser.wav")
                b.play()
                bx=px
                bullets(bx,by)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pchange = 0

    px += pchange
    if px <= 0:
        px = 0
    elif px >= 1216:
        px = 1216

    for i in range(enemy_num):
        if ey[i]>461:
            for j in range(enemy_num):
                ey[j]=2000
            game_over_text()
            break
        ex[i] += e_xchange[i]
        if ex[i] <= 0:
            ey[i] += e_ychange[i]
            e_xchange[i] = 0.7
        elif ex[i] >= 1216:
            ey[i] += e_ychange[i]
            e_xchange[i] = -0.7
            print(ex[i], ey[i], e_xchange[i], e_ychange[i])
        collison =isCollision(ex[i],ey[i],bx,by)
        if collison:
            b = mixer.Sound("explosion.wav")
            b.play()
            by=500
            bstate="ready"
            score+=1
            ex[i] = random.randint(0, 1275)
            ey[i] = random.randint(0, 350)
        enemy(ex[i], ey[i],i)
    if by <= 0:
        by = 480
        bstate = "ready"
    if bstate == "fire":
        bullets(px, by)
        by -= bey

    player(px, py)
    show_score(tx,ty)
    pygame.display.update()
