import numpy as np
from .baseLearner import BaseLearner

class Perceptron(BaseLearner):
    """ My implementation of the perceptron algorithm."""
    
    def train(self, x_train, y_train, lr=.1, epochs=100, end_cnt=10, verbose=True):
        # Add Bias
        x_train = np.hstack((np.ones((x_train.shape[0],1)), x_train))
        n, d = x_train.shape
        
        # Initialize Weights
        self.w = np.random.randn(d) * .1
        acc_list = []
        j, acc, acc_cnt = 0, 0, 0
        last_acc = 0
        misclass = []
        
        while j < epochs and acc_cnt < end_cnt:
            #Shuffle the data
            idx = np.random.permutation(n)
            x_train = x_train[idx]
            y_train = y_train[idx]
            for i in range(n):
                predicted = np.dot(self.w, x_train[i])
                predicted = 0 if predicted < 0 else 1
                self.w = self.w + (lr * (y_train[i] - predicted) * x_train[i])
                
            # Calc Loss
            y_hat = np.dot(x_train, self.w)
            y_hat[y_hat > 0] = 1
            y_hat[y_hat <= 0] = 0
            acc = accuracy_score(y_train, y_hat)
            
            # Stopping criteria
            if acc <= last_acc:
                acc_cnt += 1
            else:
                last_acc = acc
                acc_cnt = 0
                
            # Store Metrics
            acc_list.append(acc)
            con_mat = confusion_matrix(y_train, self.predict(x_train[:,1:]))
            misclass.append(con_mat[0,1]+con_mat[1,0])

            if verbose:
                print("[{}] Acc: {}".format(j, acc))   
            j += 1
            
        self.acc_list = acc_list
        self.misclass = misclass
            
    
    def predict(self, x_test, binary=True):
        x_test = np.hstack((np.ones((x_test.shape[0], 1)), x_test))
        probs = np.dot(x_test, self.w)
        if binary:
            probs[probs > 0] = 1
            probs[probs <= 0] = 0
        return probs
