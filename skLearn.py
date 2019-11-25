from sklearn.neural_network import MLPClassifier

X = [[0, 0], [1, 1]]
y = [0, 1]

# create mutli-layer perceptron classifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)

# train
clf.fit(X, y)

# make predictions
print( clf.predict([[2., 2.]]) )
print( clf.predict([[0, -1]]) )
print( clf.predict([[1, 2]]) )