"""Random Signal Generator"""

from math import sin
from random import random
from statistics import mean, variance


#: constants for variant = 22
n, w, N = 10, 1200, 64

A = [random() for _ in range(n)]
phi = [random() for _ in range(n)]
x = [sum(A[i] * sin(w / (i + 1) * (j + 1) + phi[i]) for i in range(n)) for j in range(N)]
m = mean(x)  # Math mean (expected value)
d = variance(x, m)  # Dispersion


if __name__ == '__main__':
    from matplotlib import pyplot

    pyplot.figure(figsize=(16, 9))
    pyplot.title(f'Random Signal | Mean = {m:.3f} | Dispersion = {d:.3f}')
    pyplot.plot(range(N), x, 'b')
    pyplot.show()
