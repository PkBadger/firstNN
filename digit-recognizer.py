import pandas
import numpy
from NN import NeuralNetwork

numbers = pandas.read_csv('processed_train.csv')
#print(numbers.iloc[:,1:])

brain = NeuralNetwork(784,100,10, 0.3)

total = numbers.shape[0]

for index, row in numbers.iterrows():
    target = row[1]
    inputs = row[2:]
    targets = numpy.zeros(10) + 0.01  
    targets[int(target)] = 0.99

    brain.train(inputs, targets)
    print(str(index) + '/' + str(total))

brain.saveState('digit-recognizer.state.json')
