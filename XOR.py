import numpy as np
from NN import NeuralNetwork
import pygame
from pygame.locals import *

side = 400
screen = pygame.display.set_mode((side, side))
running = 1

brain = NeuralNetwork(2,4,1, 0.3)
#brain.readState('XOR.state.json')

training_data = [
    {
        'input': [0,0],
        'target': [0]
    },
    {
        'input': [1,0],
        'target': [1]
    },
    {
        'input': [0,1],
        'target': [1]
    },
    {
        'input': [1,1],
        'target': [0]
    }
]

def drawPrediction():
    resolution= 10
    cols = rows = int(side / resolution)

    for i in range(cols):
        for j  in range(rows):
            x1 = i / cols
            x2 = j / rows
            color = int(brain.predict([x1,x2])[0][0] * 255)
            rect = pygame.draw.rect(screen, (color,color,color), (i * resolution,j * resolution,resolution,resolution))
    pygame.display.flip()
        
        


while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        brain.saveState('XOR.state.json')
        running =  0 
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        brain = NeuralNetwork(2,4,1)
    for _ in range(1000):
        data = np.random.choice(training_data)
        brain.train(data['input'], data['target'])
    drawPrediction()
