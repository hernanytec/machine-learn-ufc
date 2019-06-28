import numpy as np


def minkowski_distance(X, row, p):
    X_ = abs(X - row) ** p
    return np.sum(X_, axis=1) ** (1 / p)