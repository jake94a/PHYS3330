"""
Description:

Function:

"""
import numpy
import matplotlib.pyplot as plt


def sin_cos():
    x_num = numpy.arange(0, 2 * numpy.pi, 0.01)
    my_func = numpy.sin(2 * x_num) + numpy.cos(3 * x_num)

    plt.title("hw4.1")
    plt.plot(x_num, my_func)
    plt.show()
