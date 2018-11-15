import numpy as np
import matplotlib.pyplot as plt
from functions import measures as mes


def kernel(x):
    k = np.zeros(len(x))
    for i in range(len(x)):
        if abs(x[i]) <= 1:
           k[i] = 0.5
        else:
           k[i] = 0
    return k


step = 6/(100+1)
x = np.arange(-3,3,step)
mu = mes.sample_mean(x)
s = mes.sq_deviation(x)
print(x)

n = 100
h = s/(n**0.4)

f_k = mes.sum_of_bits(kernel(x))
f = np.exp(-(x**2)/2)/np.sqrt(2*np.pi)
f_t = np.exp((-(x-mu)**2)/(2*(s**2)))/(s*np.sqrt(2*np.pi))

plt.plot(x,f)
plt.plot(x,f_t)
plt.show()
