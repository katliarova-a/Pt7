import pygame
import sys

screen = pygame.display.set_mode((600, 400))
screen.fill((0, 255, 0))
pygame.display.set_caption("draw")

pygame.draw.rect(screen,("red"),(20,20,25,100),200)

pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

