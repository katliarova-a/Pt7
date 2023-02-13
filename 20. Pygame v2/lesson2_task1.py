import pygame
import sys
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Задание 1")
clock=pygame.time.Clock()
x_ball=130
y_ball=500
dx=1
dy=-1
while True:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen,(255,150,80),(x_ball,y_ball),20)
    x_ball+=dx
    y_ball+=dy
    pygame.display.update()