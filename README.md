# Multilayer preceptron using python

### Requirements:

- Numpy
- pandas
- Pygame

### Project files

- NN.py: file that contains the neural network implementation, this implementation has an input layer, a hidden layer and an output layer, the size of this layers can be customized

- skLearn.py: A simple example of a Neural netowork using a library

- XOR.py: a simple example of the network working by solving the categorization of an XOR logic gate

- preproccess-digits.py: This code will change out initial datased: https://www.kaggle.com/c/digit-recognizer/data to the format that we need, to use it you will need to download the dataset and extract it in a folder called digit-recognizer

- digit-recognizer.py: File that will train the NN to recognize handwritten digits, this will use the file created by preproccess-digits.py

- draw-image.py: Code to test your neural network, this will take the test data from the dataset, show you the handwritten image in a window, and the guess that the Neural network does in the terminal

### XOR intstructions:

Run `python XOR.py`, the code will start training the neural network to solve the XOR problem, more information about XOR: https://www.electronics-tutorials.ws/logic/logic_7.html

The code will show you a screen in which you can see the training in action, since the Neural network returns a number between 0 and 1, we transform that into a black and white color, in this example we divide the window into different squares, each one has a value between 0 and 1, and they are consecutives, so in the window we can clearly see the values closer to (0,1) and (1,0) as white since the NN returns a number closer to 1, and the values closer to (0,0) and (0,1) as black

### Digit recognizer instruction

1.- Download the dataset  https://www.kaggle.com/c/digit-recognizer/data and extract it in a folder called digit-recognizer

2.- Run preproccess-digits.py, this will estandarize the input for the neural network, this code will create a file called proccessed_train.csv, be aware that this is a huge file (~250 mb)

3.- Run digit-recognizer.py, this will train the NN by using the information stored in proccessed_train.csv, the train will be done wih 42000 samples, this will print the current sample so you can see the progress, once it´s done, it will generate a file called digit-recognizer.state.json, this file has all the information of the weights and biases of the trained neural network so that we can use it later

4.- The neural network is trained, so now you can test it by running drawImage.py, this program will show you a window with the current image to process, and in will print the prediction in the console, if you click on it, it will go to the next image and so on.

### Credits

I want to thank https://www.youtube.com/user/shiffman (the coding train) for providing a video tutorial of how to create a Neural network
