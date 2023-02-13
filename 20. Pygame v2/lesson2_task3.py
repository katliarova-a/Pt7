import pygame
import sys
from random import randint
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 16)
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Задание 1")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
clock=pygame.time.Clock()
paddle = pygame.image.load('paddle.png')
paddle=pygame.transform.scale(paddle,(80,30))
ball = pygame.image.load('ball.png')
bg = pygame.image.load("bg.png")
rec_paggle=paddle.get_rect(center=(50, 550))
rec_ball=ball.get_rect(center=(rec_paggle.centerx,rec_paggle.centery-30))
pad=paddle
class Cloud(pygame.sprite.Sprite):
  def __init__(self, x,y, filename):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(filename)
    self.rect = self.image.get_rect(center=(x, y))
  def update(self):
   if self.rect.x < 800:
    self.rect.x += 2
   else:
       self.rect.x=0
clouds = pygame.sprite.Group()
clouds.add(Cloud(randint(1, 400),50, 'cloud.png'), Cloud(randint(400, 800),250, 'cloud.png'))

play=0
score=0

dx=1
dy=-1
dx_p=0

while True:
    clock.tick(120)
    screen.blit(bg, (0, 0))
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                dx_p=-1
                pad = pygame.transform.rotate(paddle, 180)
                #pad=pygame.transform.flip(paddle, True, False)
            elif i.key==pygame.K_RIGHT:
                dx_p=1
                pad = paddle
            if i.key==pygame.K_SPACE:
                play=1

    if rec_ball.centerx <= 0 or rec_ball.centerx >= 800:
        dx = -dx
    if rec_ball.centery <= 0:  # or y_ball>=600
        dy = -dy
    if rec_paggle.colliderect(rec_ball):
        dy = -dy
    if rec_ball.centery > 600:
        play = 0
    if rec_paggle.centerx < 0 or rec_paggle.centerx > 700:
        dx_p = -dx_p
    for cloud in clouds:
        if rec_ball.colliderect(cloud):
            dy=-dy
    if play == 1:
        rec_ball.centerx += dx
        rec_ball.centery += dy
    elif play == 0:
        rec_ball.centerx = rec_paggle.centerx
        rec_ball.centery = rec_paggle.centery-30

    rec_paggle.centerx+=dx_p
    screen.blit(ball,rec_ball)
    screen.blit(pad,rec_paggle)

    view_score = font.render('Счет: ' + str(score), True, (205, 5, 55))
    screen.blit(view_score, (20, 20))
    clouds.draw(screen)
    pygame.display.update()
    clouds.update()