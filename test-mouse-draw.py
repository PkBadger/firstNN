import pygame
import numpy as np
from pygame.locals import *

side = 100
step = 5

screen = pygame.display.set_mode((side, side))
running = 1

squares = {}

def fillSquare(mousePos, eraser):
    x = mousePos[0] - (mousePos[0] % step)
    y = mousePos[1] - (mousePos[1] % step)

    color = 255 if eraser else 0
    
    rectangle = pygame.draw.rect(screen, (color,color,color), (x,y,step,step))
    key = str(x) + ',' + str(y)
    squares[key] = rectangle
    pygame.display.update(rectangle)

def fillSelector(mousePos):
    x = mousePos[0] - (mousePos[0] % step)
    y = mousePos[1] - (mousePos[1] % step)

    #print(x,y)
    key = str(x) + ',' + str(y)
    
    rectangle = pygame.draw.rect(screen, (0,0,255), (x,y,step,step), 3)
    rectangle_list = [rectangle]
    if key in squares:
        rectangle_list.append(squares[key])
    #pygame.display.update(rectangle_list)

screen.fill((255,255,255))
pygame.display.flip()
drawing = False
eraser = False

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running =  0 
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        print('MOSUE PRESS')
        drawing = True
        eraser = False
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        drawing = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        drawing = True
        eraser = True
    if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
        drawing = False

    if drawing:
        pos = pygame.mouse.get_pos()
        fillSquare(pos, eraser)
    

    #pos = pygame.mouse.get_pos()
    #fillSelector(pos)




    #for pixelY in range(0,side,step):
    #    for pixelX in range(0,side,step):
    #        color = np.random.randint(0,256)
    #        pygame.draw.rect(screen, (color,color,color), (pixelY,pixelX,step,step))
    

