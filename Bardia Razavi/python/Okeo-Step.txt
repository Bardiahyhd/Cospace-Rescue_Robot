import pygame
import sys
import time
from random import randint
import Persian
from bidi import algorithm
from math import sin
from math import cos
import cmath
pygame.init()
screen = pygame.display.set_mode((720,540))
step =0
def helper_XY():
    print('else if (step1 == ',step,' && px != 0 && py != 0 && tik == 0 && base == 0)')
    print('	{')
    print('		borobaadi++;')
    print('		if (( PositionX >',second_NXT,'- 7 && PositionX <',second_NXT,'+ 7 && PositionY >',second_NYT,'- 7 && PositionY <',second_NYT,'+ 7) || (borobaadi > timema))')
    print('		{')
    print('			step1++;')
    print('			borobaadi = 0;')
    print('		}')
    print('		else')
    print('		{')
    print('			zavie = mazmaz(',second_NXT,',',second_NYT,');')
    print('			bahbah(zavie);')
    print('		}')
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
            first_NX = second_NX
            first_NY = second_NY
            second_NX = Mouse_X
            second_NY = Mouse_Y
            second_NXT = int(Mouse_X/2)
            second_NYT = 270-(int(Mouse_Y/2))
            helper_XY()
            step = step + 1
            print('//---//')
            print('//X',second_NXT,'//')
            print('//Y',second_NYT,'//')
            
            if first_NX != 0  and first_NY != 0  :
                pygame.draw.line(screen, (255, 39, 39) ,(first_NX,first_NY),(second_NX,second_NY),3)
                font = pygame.font.Font(None,20)
                stepb = step -1
                screen.blit(font.render('%d'%stepb,True,(2,2,2)),(second_NX+5,second_NY+5))
                pygame.display.update()
            

            
