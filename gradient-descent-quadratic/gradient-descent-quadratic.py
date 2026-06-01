def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    y = a * (x0 ** 2) + b * x0 + c
    for i in range(steps):

        df =  lr * ((2 * a * x0) + b) 

        x0 = x0 - df
    return x0
    