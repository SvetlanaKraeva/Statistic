import numpy as np


def cauchy_normal(x):
    f = []
    for i in range(0, x):
        if np.random.uniform()>0.9:
            f.append(np.random.standard_cauchy())
        else:
            f.append(np.random.standard_normal())
    return f
