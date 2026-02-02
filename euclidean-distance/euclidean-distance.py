import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    
    x = np.array(x)
    y = np.array(y)

    
    sum_ = np.sum((x - y) ** 2)
    Euclidean_Distance = np.sqrt(sum_)
    
    return Euclidean_Distance
        
