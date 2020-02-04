import numpy
import math
import matplotlib.pyplot as plt


def sin_cos():
    x_num = numpy.arange(0, 2 * numpy.pi, 0.01)
    my_func = numpy.sin(2 * x_num) + numpy.cos(3 * x_num)
    plt.title("hw4.1")
    plt.plot(x_num, my_func)
    return my_func


"""
x_num_list is 629 values
I need fnc_sum to also be a list of 629 values, for each x_num value
"""
def sin_cos_taylor(n_terms):
    x_num = numpy.arange(0, 2 * numpy.pi, 0.01)
    x_num_list = list(x_num)
    return_list = []
    for i in range(n_terms + 1):
        for j in range(len(x_num_list)):
            return_list.append(((-1) ** i) * (
                    (3 * (x_num_list[j] ** (2 * i)) / math.factorial(2 * i)) +
                    (2 * (x_num_list[j] ** ((2 * i) + 1)) / math.factorial((2 * i) + 1))))
    fnc_sum = sum(return_list)
    plt.title("hw4.3")
    plt.plot(x_num, fnc_sum)
    return return_list


plt.plot(sin_cos_taylor(50))
plt.show()
