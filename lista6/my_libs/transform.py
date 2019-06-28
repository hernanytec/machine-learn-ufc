import numpy as np

class Normalize:
    min_val = []
    max_val = []
    
    def fit(self, X):
        self.min_val = X.min(axis=0)
        self.max_val = X.max(axis=0)
        
    def transform(self, X):
        return (X - self.min_val) / (self.max_val - self.min_val)
    
class Standardize:
    mean_val = []
    std_val = []
    
    def fit(self, X):
        self.mean_val = X.mean(axis=0)
        self.std_val = X.std(axis=0)
        
    def transform(self, X):
        return (X - self.mean_val) / self.std_val
    