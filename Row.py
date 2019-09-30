import random
import pygame

class Row:
    x = 150
    y = 40
    radius = 20
    width = 0
    vel = 100
    rowDrawn = False
    row = 1

    w, h = 6, 11
    
    
        
    
    def self.drawRow():
        
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
            pygame.draw.circle(win,color, (x,y),radius)

            pygame.display.update()
            x += 100
            rowDrawn = True
    # print (Rows[0])
