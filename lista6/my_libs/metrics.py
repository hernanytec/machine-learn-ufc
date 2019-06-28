import numpy as np

def accuracy(y_test, y_pred):
    return (y_pred == y_test).sum() / y_test.shape[0]