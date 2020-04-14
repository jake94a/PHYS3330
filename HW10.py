"""
The spherical Bessel functions are a special function subset often used to describe standing waves on closed
surfaces. They satisfy the following ordinary differential equation:
x**2 d**2y/dx**2 + 2x dy/dx + (x**2 − n(n + 1))y = 0

and can be derived using Rayleigh's differential formula as follows:
j_n(x) = (−x)**n (1/x d/dx)**n (sin(x)/x)

1. Use Rayleigh's formula to derive the first three spherical Bessel functions.

2. Plot these functions on a graph over the range x=0...25.

3. Spherical Bessel functions of the second type can be generated (for increasing values of m) using the following
recursion relation:
n_(m + 1)(x) = (2m + 1)/x n_m(x) − n_m − 1(x)

Given:
n_0(x) = −cos(x) x
n_1(x) = −cos(x)/x**2 − sin(x)/x

Write a program that generates the next 8 spherical Bessel functions of the second type and plots them on a graph.
(Don't start at x=0, the program will complain).

Fun fact: this recursion relation works for three other types of special functions (including spherical Bessel
functions of the first type). However, it is directionally unstable, meaning it only works for either increasing or
decreasing values of m (but not both), depending on the function.
"""
import numpy
import matplotlib.pyplot as plt

# 1. Done on paper
# 2. Plot j_0, j_1, j_2

x_range = numpy.arange(0.01, 25, 0.01)
j_0 = numpy.sin(x_range) / x_range
j_1 = numpy.sin(x_range) / (x_range ** 2) - numpy.cos(x_range) / x_range
j_2 = -((x_range ** 2 - 3) * numpy.sin(x_range) + 3 * x_range * numpy.cos(x_range)) / x_range ** 3
# j_2 = ((3/(x_range**3)) - (1/x_range))*numpy.sin(x_range) - (3/x_range**2)*numpy.cos(x_range)

plt.figure("HW10.2")
plt.plot(x_range, j_0)
plt.plot(x_range, j_1)
plt.plot(x_range, j_2)
plt.figlegend(("j_0", "j_1", "j_2"))
plt.title("HW10.2")
plt.show()

"""n_(m + 1)(x) = (2m + 1)/x n_m(x) − n_(m − 1)(x)

Given:
n_0(x) = −cos(x)/x
n_1(x) = −cos(x)/x**2 − sin(x)/x"""


def bessel(x):
    n_range = range(1, 9)  # 1, 2, 3, 4, 5, 6, 7, 8
    n = numpy.zeros((10, len(x)))  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    n[0] = -numpy.cos(x) / x
    n[1] = (-numpy.cos(x) / x ** 2) - (numpy.sin(x) / x)
    legend_list = numpy.arange(10)
    for m in n_range:
        n[m + 1] = (((2 * m + 1) / x) * n[m]) - n[m - 1]
    for eq in n:
        plt.plot(x, eq)
    plt.figlegend(legend_list)
    return n


plt.figure("HW10.3")
plt.title("HW10.3")
bessel(x_range)
plt.ylim((-0.6, 0.6))
plt.xlim((0, 10))
plt.show()
