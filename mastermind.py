import pygame
import random 

pygame.init()
win=pygame.display.set_mode((700,700))
pygame.display.set_caption("Mastermind")


x = 50
y = 50
radius = 20
width = 0
vel = 60

run = True

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


    win.fill((0,0,0))
    i = 0
    



pygame.quit()


def drawRow():
    for i in range(4):
        i += 1
        pygame.draw.circle(win,(255,0,0), (x,y), radius)
        pygame.display.update()
        x += 60