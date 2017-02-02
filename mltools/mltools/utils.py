import numpy as np

def one_hot(y, num_class=None):
    y = np.array(y, dtype='int').ravel()
    if not num_class:
        num_class = np.max(y) + 1
    n = y.shape[0]
    out = np.zeros((n, num_class))
    out[np.arange(n), y] = 1
    return out
