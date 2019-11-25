import pandas
import pygame
import numpy as np
from pygame.locals import *
from NN import NeuralNetwork

side = 28 * 8
step = 8

screen = pygame.display.set_mode((side, side))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
running = 1
numberIndex = 0

brain = NeuralNetwork(784,100,10, 0.3)
brain.readState('digit-recognizer.state.json')
numbers = pandas.read_csv('digit-recognizer/test.csv')

numberIndex = 0


def drawNumber(index):
    number = numbers.iloc[index]

    pixelX = 0
    pixelY = 0
    for (columnName, color) in number.iteritems():
        if(pixelX == 28):
            pixelX = 0
            pixelY += 1
        
        rect = pygame.draw.rect(screen, (color,color,color), (pixelX * step,pixelY * step,step,step))
        pygame.display.update(rect)
        pixelX +=1

def guess(index):
    number = numbers.iloc[index] / 255.0 * 0.99 +  0.01
    prediction = brain.predict(number)
    print(np.argmax(prediction))

drawNumber(numberIndex)
guess(numberIndex)

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running =  0 
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        numberIndex += 1
        drawNumber(numberIndex)
        guess(numberIndex)
    