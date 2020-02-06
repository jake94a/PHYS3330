"""
Quiz5

Take FDA, BDA, CDA, and SCDA
on range x=range(0, 10, 0.01)
of f(x) = 2sin(3x) + cos(4x)
"""
import matplotlib.pyplot as plt
import numpy

h = 0.01
x = numpy.arange(0, 10, h)
f_x = 2 * numpy.sin(3 * x) + numpy.cos(4 * x)


def derivative_of_original():
    x_range = numpy.arange(0, 10, h)
    # f_x_thing = 2 * numpy.sin(3 * x_thing) + numpy.cos(4 * x_thing)
    the_derivative = 6 * numpy.cos(3 * x_range) - 4 * numpy.sin(4 * x_range)
    return the_derivative


# fda = (f(x+h) - f(x)) / h
# bda = (f(x) - f(x-h)) / h
# cda = (f(x+h) - f(x-h)) / (2*h)
# scda = (f(x+h) + f(x-h) - 2*f(x)) / (h ** 2)

def fda(x_range, step):
    fx_h = 2 * numpy.sin(3 * (x_range + step)) + numpy.cos(4 * (x_range + step))
    fx = 2 * numpy.sin(3 * x_range) + numpy.cos(4 * x_range)
    fda_total = (fx_h - fx) / step
    return fda_total


def bda(x_range, step):
    fx_h = 2 * numpy.sin(3 * (x_range - step)) + numpy.cos(4 * (x_range - step))
    fx = 2 * numpy.sin(3 * x_range) + numpy.cos(4 * x_range)
    bda_total = (fx - fx_h) / step
    return bda_total


def cda(x_range, step):
    fx_plus_h = 2 * numpy.sin(3 * (x_range + step)) + numpy.cos(4 * (x_range + step))
    fx_minus_h = 2 * numpy.sin(3 * (x_range - step)) + numpy.cos(4 * (x_range - step))
    cda_total = (fx_plus_h - fx_minus_h) / (2 * step)
    return cda_total


#def scda


fda_plot = fda(x, h)
bda_plot = bda(x, h)
cda_plot = cda(x, h)
plt.plot(derivative_of_original())
plt.plot(fda_plot)
plt.plot(bda_plot)
plt.plot(cda_plot)
plt.show()
