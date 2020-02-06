import numpy
import math


def sin_cos():
    x_num = numpy.arange(0, 2 * numpy.pi, 0.01)
    my_func = numpy.sin(2 * x_num) + numpy.cos(3 * x_num)
    # plt.title("hw4.1")
    # plt.plot(x_num, my_func)
    return my_func


def sin_cos_taylor(n_terms):
    x = numpy.arange(0, 2 * numpy.pi, 0.01)
    error_list = []
    ms = 1
    even_counter = 0
    odd_counter = 0
    for i in range(1, n_terms + 1):
        # print(ms, i)
        if i % 2 == 0:  # cos
            nth_term = ((-1) ** (even_counter + 1)) * ((3 ** i) / math.factorial(i)) * (x ** i)
            even_counter += 1
        else:  # sin
            nth_term = ((-1) ** odd_counter) * ((2 ** i) / math.factorial(i)) * (x ** i)
            odd_counter += 1
        ms += nth_term
        error_list.append(nth_term)
    return ms
    # plt.title(f'Error is {nth_term[-1]}')
