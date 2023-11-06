import pygame
import sys
import time
from random import randint
pygame.init()
screen = pygame.display.set_mode((720,540))
step =0
def helper_XY(FX , FY , SX , SY):
    print('	if (py <',SY,'&& py >',FY,'&& px <',SX,'&& px >',FX,' && sy <',SY,'&& sy >',FY,'&& sx <',SX,'&& sx >',FX,'&& base == 0)')
    print('	{')
    print('		base = 1;')
    print('		tik = 0;')
    print('	}')
    
   
pygame.display.update()
Board = [[0 for x in range(360)]for y in range(270)]
marhale = 1
img = pygame.image.load('U19_W2.png')
screen.blit(img,(0,0))
pygame.display.update()

def sinoo(zav , tol):
    zav = zav*3.14/180
    y1 = sin(zav)*tol
    x1 = cos(zav)*tol
    y1 = y1 + 135
    x1 = x1 + 180
    print(int(x1))
    print(int(y1))
    print("---")
    pygame.draw.circle(screen, (0,0,0) ,(int(x1),int(y1)),2,0)
    pygame.display.update()

#sinoo(18,70)
#sinoo(90,70)
#sinoo(162,70)
#sinoo(234,70)
#sinoo(306,70)
#pygame.display.update()

first_NX = 0
first_NY = 0
second_NX = 0
second_NY = 0
z=0
while z== 0 :
    for e in pygame.event.get():
         if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         if e.type == pygame.MOUSEBUTTONUP:
            time.sleep(0.1)
            Mouse_X , Mouse_Y = pygame.mouse.get_pos()
            if second_NX == 0 and second_NY == 0 and first_NX == 0 and first_NY == 0:
                first_NX = Mouse_X
                first_NY = Mouse_Y
            elif first_NX != 0 and first_NY != 0 and  second_NX == 0 and second_NY == 0 :
                second_NX = Mouse_X
                second_NY = Mouse_Y
            else :
                first_NX = Mouse_X
                first_NY = Mouse_Y
                second_NX = 0
                second_NY = 0
            second_NXT = int(Mouse_X/2)
            second_NYT = 270-(int(Mouse_Y/2))
            if first_NX != 0 and first_NY != 0 and  second_NX != 0 and second_NY != 0 :
                helper_XY(int(first_NX/2),270-(int(first_NY/2)), int(second_NX/2),270-(int(second_NY/2)))
                pygame.draw.rect(screen, (0, 0, 0) ,(first_NX,first_NY,second_NX-first_NX,second_NY-first_NY),2)
                pygame.display.update()
            #step = step + 1
            print('//---//')
            #print('//X',second_NX,'//')
            #print('//Y',second_NY,'//')
            #print('//X',first_NX,'//')
            #print('//Y',first_NY,'//')
            #if first_NX != 0  and first_NY != 0  :
                #pygame.draw.line(screen, (255, 39, 39) ,(first_NX,first_NY),(second_NX,second_NY),3)
                #font = pygame.font.Font(None,20)
                #stepb = step -1
                #screen.blit(font.render('%d'%stepb,True,(2,2,2)),(second_NX+5,second_NY+5))
                #pygame.display.update()
            

            
