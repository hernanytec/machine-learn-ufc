import numpy as np
from sklearn.metrics import confusion_matrix

def precision(y, y_pred):
    cm = confusion_matrix(y, y_pred)
    return cm[0,0] / np.sum(cm[:, 0])