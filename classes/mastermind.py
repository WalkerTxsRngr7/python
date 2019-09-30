import pygame
import random 
from Row import *

pygame.init()
win=pygame.display.set_mode((700,710))
pygame.display.set_caption("Mastermind")







# Rows = [[0 for x in range(w)] for y in range(h)] 
Rows = []
Rows.append(Row())



# Rows[0][i] = colorNum

run = True    

#[[c1, c2, c3, c4, right, wrongSpot],[]]

def board():
    radius = 20
    m = 10
    z = 10
    b=40
    for j in range(10):
        pygame.draw.rect(win, (200,200,200), (m,z, 680, 60), 5)
        z += 70
        a=150
    

        for h in range(4):
        
            pygame.draw.circle(win,(75,75,75), (a,b), radius-7)

            pygame.display.update()
            a += 100

        v = a
        w = b
        v -= 10
        w -= 7
        pygame.draw.circle(win,(125,125,125), (v,w), radius-15) #top left
        v += 15
        pygame.draw.circle(win,(125,125,125), (v,w), radius-15) #top right
        w += 15
        pygame.draw.circle(win,(125,125,125), (v,w), radius-15) #bottom right
        v -= 15
        pygame.draw.circle(win,(125,125,125), (v,w), radius-15) #bottom left

        b+= 70
    pygame.display.update()


board()
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    if (rowDrawn == False):
        drawRow()

    win.fill((0,0,0))
    i = 0
    



pygame.quit()


