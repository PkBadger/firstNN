import numpy as np
import json

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class NeuralNetwork:
    def __init__(self, input_number: int, hidden_number: int, output_number: int, lr, fileName = None):
        self.input_nodes = input_number
        self.hidden_nodes = hidden_number
        self.output_nodes = output_number

        self.weights_ih = np.random.normal(0.0, pow(self.hidden_nodes, -0.5),  (self.hidden_nodes, self.input_nodes)) 
        self.weights_ho = np.random.normal(0.0, pow(self.output_nodes, -0.5),  (self.output_nodes, self.hidden_nodes)) 

        self.bias_h = np.random.rand(hidden_number, 1)

        self.bias_o = np.random.rand(output_number, 1)

        self.learning_rate = lr

    def feed_forward(self, input):
        hidden = np.dot(self.weights_ih, input)
        
        #hidden = np.sum([hidden, self.bias_h], axis=0)

        hidden = np.sum([hidden, self.bias_h], axis=0)

        afterSigmoid = sigmoid(hidden)

        output = np.dot(self.weights_ho, afterSigmoid)

        output = np.sum([output, self.bias_o], axis=0)

        return [sigmoid(output), afterSigmoid]

    def predict(self,input):
        inputs = np.array(input, ndmin=2).T  

        outputs, hidden = self.feed_forward(inputs)

        return outputs

    def readState(self, fileName):
        with open(fileName) as json_file:
            data = json.load(json_file)
            self.weights_ho = np.array(data['weightsHO'])
            self.weights_ih = np.array(data['weightsIH'])
            self.bias_h = np.array(data['biasH'])
            self.bias_o = np.array(data['biasO'])

    def saveState(self, fileName):
        data = {
            'inputNodes': self.input_nodes,
            'hiddenNodes': self.hidden_nodes,
            'outputNodes': self.output_nodes,
            'weightsIH':self.weights_ih.tolist(),
            'weightsHO': self.weights_ho.tolist(),
            'biasH': self.bias_h.tolist(),
            'biasO': self.bias_o.tolist(),
            'LR': self.learning_rate,
        }

        with open(fileName, 'w') as outfile:
            json.dump(data, outfile)

    def train(self, input, target):
        inputs = np.array(input, ndmin=2).T  
        targets = np.array(target, ndmin=2).T 

        outputs, hidden = self.feed_forward(inputs)

        # Output errors and gradient
        output_errors = targets - outputs

        gradient = np.array([sigmoid_derivative(output) for output in outputs])

        #gradient = np.reshape(gradient, (self.output_nodes, 1))

        gradient = gradient * output_errors

        gradient = self.learning_rate * gradient

        #hidden_transpose = np.transpose(hidden.reshape(self.hidden_nodes,1))

        weigths_ho_deltas = np.dot(gradient, hidden.T)#.reshape(self.output_nodes, self.hidden_nodes)

        self.weights_ho +=weigths_ho_deltas #np.sum([self.weights_ho, weigths_ho_deltas])

        # Hidden layer errors and gradient
        hidden_errors = np.dot(self.weights_ho.T, output_errors)

        hidden_gradient = np.array([sigmoid_derivative(hid) for hid in hidden])
        
        #hidden_gradient = np.reshape(hidden_gradient, (self.hidden_nodes, 1))

        hidden_gradient = hidden_gradient * hidden_errors

        hidden_gradient = self.learning_rate * hidden_gradient

        #input_transpose = np.transpose(np.reshape(input, (self.input_nodes,1)))

        weights_ih_deltas = np.dot(hidden_gradient,inputs.T)

        self.weights_ih += weights_ih_deltas # np.sum([self.weights_ih, weights_ih_deltas])


if __name__ == '__main__':
    brain = NeuralNetwork(2,10,1)

    input = [1,0]

    target = 1

    #print(brain.pre_feed_forward(input))

    output = brain.train(input, target)

    #print(output)
