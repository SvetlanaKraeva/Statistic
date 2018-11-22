import numpy as np


def sum_of_bits(x, i, n):
    s = 0
    for j in range(i, n):
        s += x[j]
        return s


def sample_mean(x):
    return sum_of_bits(x, 0, len(x))/len(x)


def sample_median(x):
    n = len(x)
    if 0.5 * n == round(0.5 * n):
        k = int(0.5 * n)
        z = 0.5*(x[k]+x[k+1])
    else:
        k = 0.5*(n+1)
        z = x[k]
    return z


def sample_r(x):
    return 0.5*(x[0]+x[len(x)-1])


def trimmed_mean(x):
    n = len(x)
    a = 0.1
    r = round(a*n)
    z = sum_of_bits(x, r+1, n-r)/(n-2*r)
    return z


def sample_q(x):
    n = len(x)
    if 0.25 * n == round(0.25 * n):
        k = int(0.25 * n)
    else:
        k = round(0.25 * n) + 1
    lq = x[k]
    if 0.75 * n == round(0.75 * n):
        kk = int(0.75 * n)
    else:
        kk = round(0.75 * n) + 1
    uq = x[kk]
    z = 0.5*(lq+uq)
    return z


def sq_deviation(x):
    n = len(x)
    x_n = np.zeros(len(x), dtype=float)
    for j in range(0, n):
        x_n[j] = ((x[j]-sample_mean(x)) ** 2)
    s = (sum_of_bits(x_n, 0, n)/n)**0.5
    return s


def ab_deviation(x):
    n = len(x)
    x_n = np.zeros(len(x), dtype=float)
    for j in range(0, n):
        x_n[j] = abs(x[j]-sample_median(x))
    d = sum_of_bits(x_n, 0, n)/n
    return d


def sample_range(x):
    r = x[len(x)-1]-x[0]
    return r


def iqr(x):
    n = len(x)
    if 0.25 * n == round(0.25 * n):
        k = 0.25 * n
    else:
        k = round(0.25 * n) + 1
    k = int(k)
    lq = x[k]
    if 0.75*n == round(0.75 * n):
        kk = 0.75 * n
    else:
        kk = round(0.75 * n) + 1
    kk = int(kk)
    uq = x[kk]
    z = lq-uq
    return z


def mad(x):
    n = len(x)
    x_n = np.zeros(len(x), dtype=float)
    for j in range(0, n):
        x_n[j] = abs(x[j]-sample_median(x))
    m = sample_median(x_n)
    return m

