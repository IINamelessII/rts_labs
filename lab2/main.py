"""Fourier Transforms"""

from time import time

import numpy as np
from matplotlib import pyplot

from lab1.part1 import N, random_signal


def dft(signals):
	"""Discrete Fourier Transform"""

	p = np.arange(len(signals))
	k = p.reshape((len(signals), 1))
	w = np.exp(-2j * np.pi * p * k / len(signals))

	return np.dot(w, signals)


def fft(signals):
	"""Fast Fourier Transform"""

	signals = np.asarray(signals, dtype=float)

	if len(signals) <= 2:
		return dft(signals)

	signal_even = fft(signals[::2])
	signal_odd = fft(signals[1::2])

	terms = np.exp(-2j * np.pi * np.arange(len(signals)) / len(signals))
	return np.concatenate([
		signal_even + terms[:len(signals) // 2] * signal_odd,
		signal_even + terms[len(signals) // 2:] * signal_odd
	])


if __name__ == '__main__':

	x = random_signal()
	y = np.linspace(0, 5, N)

	# DFT
	t1 = time()
	x_dft = dft(x)
	t2 = time()
	print(f'Execution time (DFT): {(t2 - t1) * 1000} ms')

	# DFT
	t1 = time()
	x_fft = fft(x)
	t2 = time()
	print(f'Execution time (FFT): {(t2 - t1) * 1000} ms')

	# Init plots
	chart_signal, chart_DFT, chart_FFT = pyplot.subplots(3, 1, figsize=(16, 9))[1]

	# Plot - Rangom Signal
	chart_signal.set_title("Random signal")
	chart_signal.plot(y, x, 'k')

	# Plot - DFT
	chart_DFT.set_title("DFT")
	chart_DFT.plot(y, x_dft.real, 'g', y, x_dft.imag, 'k')

	# Plot - FFT
	chart_FFT.set_title("FFT")
	chart_FFT.plot(y, x_fft.real, 'g', y, x_fft.imag, 'k')

	pyplot.show()
