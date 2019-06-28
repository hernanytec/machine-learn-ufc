import numpy as np

def chebyshev_distance(X, row):
    return max(abs(X - row), axis=1)
