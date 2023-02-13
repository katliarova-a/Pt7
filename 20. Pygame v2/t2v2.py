import pygame
import sys
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Задание 1")
clock=pygame.time.Clock()
x_ball=130
y_ball=500
x_panel=350
dx=3
dy=-3
dxp=3
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 16)
while True:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                dxp=-2
            if i.key==pygame.K_RIGHT:
                dxp=2
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen,(255,150,80),(x_ball,y_ball),20)
    pygame.draw.rect(screen,(100,30,5),(x_panel,580,100,20),20)
    if x_ball>780 or x_ball<20:
        dx=-dx
    if y_ball<20:
        dy=-dy
    if x_panel>700 or x_panel<0:
        dxp=-dxp
    if x_ball>x_panel and x_ball<x_panel+100 and y_ball>580:
        dy=-dy
    if y_ball>590:
        ower = font.render('Game ower', True, (205, 5, 55))
        screen.blit(ower, (320, 220))
    x_ball+=dx
    y_ball+=dy
    x_panel+=dxp
    pygame.display.update()