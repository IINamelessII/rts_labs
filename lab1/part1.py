"""Random Signal Generator"""

from math import sin
from random import random
from statistics import mean, variance

from matplotlib import pyplot

from rts import log


#: constants for variant = 22
n, w, N = 10, 1200, 64


@log('random_signal.txt')
def random_signal():
    A = [random() for _ in range(n)]
    phi = [random() for _ in range(n)]
    return [sum(A[i] * sin(w / (i + 1) * (j + 1) + phi[i]) for i in range(n)) for j in range(N)]


@log('mean.txt')
def calc_mean(x):
    return mean(x)


@log('variance.txt')
def calc_variance(x, m):
    return variance(x, m)


if __name__ == '__main__':
    x = random_signal()
    m = calc_mean(x)
    d = calc_variance(x, m)

    pyplot.figure(figsize=(16, 9))
    pyplot.title(f'Random Signal | Mean = {m:.5f} | Dispersion = {d:.5f}')
    pyplot.plot(range(N), x, 'b')
    pyplot.show()
