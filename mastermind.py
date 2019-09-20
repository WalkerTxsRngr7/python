import pygame
import random 

pygame.init()
win=pygame.display.set_mode((700,700))
pygame.display.set_caption("Mastermind")


x = 100
y = 40
radius = 20
width = 0
vel = 100
rowDrawn = False
row = 1

w, h = 6, 11
Rows = [[0 for x in range(w)] for y in range(h)] 

run = True

def board():
    m = 10
    z = 10
    for j in range(11):
        pygame.draw.rect(win, (125,125,125), (m,z, 680, 60), 5)
        z += 70
    pygame.display.update()
        

def drawRow():
    global rowDrawn
    global x
    global y
    global radius
    global width
    global vel
    for i in range(4):
        colorNum = random.randrange(6)

        if (colorNum == 0):  #red
            color = (255,0,0)
        elif (colorNum == 1):    #orange
            color = (255,128,0)
        elif (colorNum == 2):    #yellow
            color = (255,255,0)
        elif (colorNum == 3):    #green
            color = (0,255,0)
        elif (colorNum == 4):    #blue
            color = (0,0,255)
        elif (colorNum == 5):    #pink
            color = (255,0,255)

        Rows[0][i] = colorNum
        

        pygame.draw.circle(win,color, (x,y), radius)

        pygame.display.update()
        x += 100
        rowDrawn = True
        i += 1


    print (Rows[0])

    

#[[c1, c2, c3, c4, right, wrongSpot],[]]




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


