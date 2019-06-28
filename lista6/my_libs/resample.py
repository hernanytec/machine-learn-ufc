import numpy as np


def spit_stratified_train_test(y, perc, seed):
    r = np.random.RandomState(seed)
    perm_index = r.permutation(y.shape[0])
    
    n_train = int(np.ceil(y.shape[0] * perce_train))
    
    return perm_index(0:n_train), perm_index(n_train+1:)