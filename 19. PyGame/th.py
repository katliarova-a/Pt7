import pygame
import sys
screen=pygame.display.set_mode((600,400))
screen.fill((0,255,0))
pygame.display.set_caption("Hello")
pygame.display.update()
FPS=1
clock=pygame.time.Clock()
while True:
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()