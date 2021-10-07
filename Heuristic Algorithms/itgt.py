from scipy import integrate
import numpy as np
def f(x):
    return (((3.5/2) * (x/2) ** 2.5) * np.exp(-1 * (x / 2) ** 3.5)) * x
v, err = integrate.quad(f, 0, 1)
# print(v)
#
# (((3.5/2) * (x/2) ** 2.5) * np.exp(-1 * (x / 2) ** 3.5)) * x
#
#
# (1-np.exp(-1 * (x / 2) ** 3.5))



(100 * (1-np.exp(-1 * (x / 2) ** 3.5)) + 50 * np.exp(-1 * (x / 2) ** 3.5)) / \
           ((1-np.exp(-1 * (x / 2) ** 3.5)) * v + x * np.exp(-1 * (x / 2) ** 3.5))