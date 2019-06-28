from metrics.recall import recall
from metrics.precision import precision

def f1_measure(y, y_pred):
    rec = recall(y, y_pred)
    prec = precision(y, y_pred)
    
    return 2 * (rec * prec / (rec + prec))