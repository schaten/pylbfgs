import lbfgs
import numpy as np
def f(x, *args):
    return x**2
def g(x):
    return np.array([2*x])
print(lbfgs.minimize(f, 10, jac=g))
