import numpy
import math
import tkinter
from tkinter import messagebox

def hw4_2():
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Hello", "HW4.2 was completed on paper."
                        "\nI wouldn't have been able to do HW4.3 without it."
                        "\nSo this is me saying I did it.")


def sin_cos():
    x_num = numpy.arange(0, 2 * numpy.pi, 0.01)
    my_func = numpy.sin(2 * x_num) + numpy.cos(3 * x_num)
    # plt.title("hw4.1")
    # plt.plot(x_num, my_func)
    return my_func


def sin_cos_taylor(n_terms):
    x = numpy.arange(0, 2 * numpy.pi, 0.01)
    # error_list = []
    # the first value of the taylor series at x=0 is 1
    ms = 1
    even_counter = 0
    odd_counter = 0
    for index in range(1, n_terms + 1):
        # print(ms, i)
        if index % 2 == 0:  # cos
            nth_term = ((-1) ** (even_counter + 1)) * ((3 ** index) / math.factorial(index)) * (x ** index)
            even_counter += 1
        else:  # sin
            nth_term = ((-1) ** odd_counter) * ((2 ** index) / math.factorial(index)) * (x ** index)
            odd_counter += 1
        ms += nth_term
        # error_list.append(nth_term)
    return ms
    # plt.title(f'Error is {nth_term[-1]}')
