import pandas
import numpy

numbers = pandas.read_csv('digit-recognizer/train.csv')


numbers.iloc[:,1:] = numbers.iloc[:,1:] / 255.0 * 0.99 +  0.01

numbers.to_csv('processed_train.csv')

print(numbers)

