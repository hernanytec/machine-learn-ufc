from implementacoes.minkowski_distance import minkowski_distance

def euclidean_distance(X, row):
    return minkowski_distance(X, row, 2)