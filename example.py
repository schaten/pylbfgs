import lbfgs
import numpy as np
def f(x, *args):
    return x[0]**2 + (x[1] + 10)**2
def g(x):
    return np.array([2*x[0], 2*(x[1]+10)])
print(lbfgs.minimize(f, [0,1], jac=g, options={'gtol': 10e-2}).__dict__)
