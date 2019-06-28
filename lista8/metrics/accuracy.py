import numpy as np

def accuracy(y, y_pred):
    return np.sum(y == y_pred) / y.shape[0]