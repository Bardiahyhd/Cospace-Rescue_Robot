import pygame
import sys
import time
from random import randint
from math import sin
from math import cos
import cmath
pygame.init()

Board = [[0 for x in range(27)]for y in range(36)]

def mohasebat(x2,x,y2,y):
    x2 = int(x2/2)
    x = int(x/2)
    y2 = int(y2/2)
    y = int(y/2)
    
    for i in range(x2-x):
        for j in range(y2-y):
            if Board[int((x + i)/10)][(int((y + j)/10))] == 0:
                #print("wayinputwall(",int((x + i)/10),",",27 - (int((y + j)/10)),")")
                Board[(int((y + j)/10))][(int((x + i)/10))] = 1

def printall():
    print("//----------------------------------------------------------------------//")
    for z in range(36):
        print("{",Board[z][0],",",Board[z][1],",",Board[z][2],",",Board[z][3],",",Board[z][4],",",Board[z][5],",",Board[z][6],",",Board[z][7],",",Board[z][8],",",Board[z][9],",",Board[z][10],",",Board[z][11],",",Board[z][12],",",Board[z][13],",",Board[z][14],",",Board[z][15],",",Board[z][16],",",Board[z][17],",",Board[z][18],",",Board[z][19],",",Board[z][20],",",Board[z][21],",",Board[z][22],",",Board[z][23],",",Board[z][24],",",Board[z][25],",",Board[z][26],"},")
        
    print("//----------------------------------------------------------------------//")
    
screen = pygame.display.set_mode((720,540))
img = pygame.image.load('U19_W2.png')
screen.blit(img,(0,0))
pygame.display.update()
pygame.key.start_text_input

first_NX = 0
first_NY = 0
second_NX = 0
second_NY = 0
z=0
p=0
while z== 0 :
    
    #p = p+1
    
    #if pygame.key.get_focused == True :
    #    printall()
        
    #if p == 1000000:
    #    p = 0
    #    print(pygame.key.name)
        
    for e in pygame.event.get():

        if e.type == pygame.KEYDOWN:
            printall()
            
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
                mohasebat(second_NX, first_NX, second_NY, first_NY)
                pygame.draw.rect(screen, (0, 0, 0) ,(first_NX,first_NY,second_NX-first_NX,second_NY-first_NY),1)
                pygame.display.update()
           
            #step = step + 1
            print('//Got It//')
