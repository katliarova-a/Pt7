import pygame
import sys
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Задание 1")
clock=pygame.time.Clock()
x_panel=0
x_ball = x_panel+50
y_ball = 560
dx=1
dy=-1
dx_p=0
play=0
while True:
    clock.tick(120)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                dx_p=-1
            if i.key==pygame.K_RIGHT:
                dx_p=1
            if i.key==pygame.K_SPACE:
                play=1
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen,(255,150,80),(x_ball,y_ball),20)
    if x_ball<=0 or x_ball>=800:
        dx=-dx
    if y_ball<=0: #or y_ball>=600
        dy=-dy
    if y_ball>=580 and x_ball>x_panel and x_ball<x_panel+100:
        dy=-dy
    if y_ball>600:
        play=0
    if x_panel<0 or x_panel>700:
        dx_p=-dx_p
    if play==1:
        x_ball+=dx
        y_ball+=dy
    elif play==0:
        x_ball = x_panel + 50
        y_ball = 560

    pygame.draw.rect(screen,(100,30,5),(x_panel,580,100,20))
    x_panel+=dx_p
    pygame.display.update()