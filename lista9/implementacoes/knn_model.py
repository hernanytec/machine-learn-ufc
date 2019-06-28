import numpy as np
from implementacoes.euclidean_distance import euclidean_distance

class KNNModel():
    def __init__(self, k):
        self.k = k
    
    def fit(self, X, y):
        self.X = X
        self.y = y
        return self
    
    def idx_knn(self, linha):
        dist_euc = euclidean_distance(self.X, linha)
        idx_sort = np.argsort(dist_euc)
        return idx_sort[:self.k]

class KNNClassifier(KNNModel):
    
    def classifica(self, linha):
        idx_knn = super().idx_knn(linha)
        count = np.bincount(self.y[idx_knn])
        return np.argmax(count)
    
    
    def predict(self, test):
        return np.array(list(map(lambda linha: self.classifica(linha), test)))
    
      
class KNNRegressor(KNNModel):
    
    def classifica(self, linha):
        idx_knn =super().idx_knn(linha)
        return np.mean(y[idx_knn])
   
    def predict(self, test):
        return np.array(list(map(lambda linha: self.classifica(linha), test)))