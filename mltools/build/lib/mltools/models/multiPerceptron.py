import numpy as np
from .baseLearner import BaseLearner
from .perceptron import Perceptron

class MultiPerceptron(BaseLearner):
    """ My implementation of the perceptron algorithm."""
    
    def __init__(self, num_classes=3):
        self.num_classes = num_classes
    
    def train(self, x_train, y_train, lr=.1, epochs=100, verbose=True):
        
        # Initialize a perceptron for each class
        self.p_list = []
        for i in range(self.num_classes):
            pTron = Perceptron()
            class_y_train = np.copy(y_train)
            class_y_train[y_train == i] = 1
            class_y_train[y_train != i] = 0

            pTron.train(x_train, class_y_train, lr=lr, epochs=epochs, verbose=False)
            self.p_list.append(pTron)
            
    
    def predict(self, x_test):
        predictions = [0] * self.num_classes
        for i in range(self.num_classes):
            predictions[i] = self.p_list[i].predict(x_test, binary=False)
        
        return np.argmax(np.vstack(predictions), axis=0)
