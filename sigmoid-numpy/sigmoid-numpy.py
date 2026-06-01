import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x)

    sigma = 1 /(1 + np.exp(-(x)))
    return sigma


