import pygame
import sys
import time
from random import randint
import cmath
pygame.init()
def test():
    print("int stepx[] = [",ssx,",]")
    print("int stepy[] = [",ssy,",]")
step = 0;
stepx = []
stepy = []
screen = pygame.display.set_mode((720,540))
img = pygame.image.load('U19_W2.png')
screen.blit(img,(0,0))
pygame.display.update()
first_NX = 0
first_NY = 0
second_NX = 0
second_NY = 0
ssx= 0
ssy= 0
z=0
while z== 0 :
    for e in pygame.event.get():
         if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         if e.type == pygame.MOUSEBUTTONUP:
            time.sleep(0.1)
            Mouse_X , Mouse_Y = pygame.mouse.get_pos()
            first_NX = second_NX
            first_NY = second_NY
            second_NX = Mouse_X
            second_NY = Mouse_Y
            second_NXT = int(Mouse_X/2)
            second_NYT = 270-(int(Mouse_Y/2))
            stepx.append(float(second_NXT))
            stepy.append(float(second_NYT))
            print ("int stepx[",len(stepx),"] =",stepx)
            print ("int stepy[",len(stepy),"] =",stepy)
            ssx = ssx + 1
            ssy = ssy + 1
            step = step + 1
            print('//---//')
            
            if first_NX != 0  and first_NY != 0  :
                pygame.draw.line(screen, (255, 39, 39) ,(first_NX,first_NY),(second_NX,second_NY),3)
                font = pygame.font.Font(None,20)
                stepb = step -1
                screen.blit(font.render('%d'%stepb,True,(2,2,2)),(second_NX+5,second_NY+5))
                pygame.display.update()




#int stepx[12] = [336.0, 271.0, 272.0, 186.0, 183.0, 58.0, 49.0, 25.0, 19.0, 122.0, 128.0, 103.0];
#int stepy[12] = [30.0, 28.0, 168.0, 180.0, 237.0, 242.0, 137.0, 124.0, 52.0, 45.0, 118.0, 192.0];







                
