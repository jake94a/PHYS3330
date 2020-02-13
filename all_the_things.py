import numpy
import math
import tkinter
from tkinter import messagebox


def sbda(x_range, step, fnc, x):
    # sbda: (f(x) - 2*f(x-h) + f(x-(2*h))) / h^2
    fx_minus_2h = numpy.zeros(len(x_range))
    fx_minus_h = numpy.zeros(len(x_range))
    fx = numpy.zeros(len(x_range))
    for i in range(len(x_range)):
        fx_minus_h[i] = fnc.subs(x, x_range[i] - step)
        fx_minus_2h[i] = fnc.subs(x, x_range[i] + (2 * step))
        fx = fnc.subs(x, x_range[i])
    sbda_total = (fx - (2*fx_minus_h) + fx_minus_2h) / (step**2)
    return sbda_total


def sfda(x_range, step, fnc, x):
    # sfda: (f(x+(2*h)) - 2*f(x+h) + f(x)) / h^2
    fx_plus_2h = numpy.zeros(len(x_range))
    fx_plus_h = numpy.zeros(len(x_range))
    fx = numpy.zeros(len(x_range))
    for i in range(len(x_range)):
        fx_plus_h[i] = fnc.subs(x, x_range[i] + step)
        fx_plus_2h[i] = fnc.subs(x, x_range[i] + (2 * step))
        fx = fnc.subs(x, x_range[i])
    sfda_total = (fx_plus_2h - (2*fx_plus_h) + fx) / (step**2)
    return sfda_total


def scda(x_range, step, fnc, x):
    # scda = (f(x+h) + f(x-h) - 2*f(x)) / (h ** 2)
    fx_plus_h = numpy.zeros(len(x_range))
    fx_minus_h = numpy.zeros(len(x_range))
    fx = numpy.zeros(len(x_range))
    for i in range(len(x_range)):
        fx_plus_h[i] = fnc.subs(x, x_range[i] + step)
        fx_minus_h[i] = fnc.subs(x, x_range[i] - step)
        fx = fnc.subs(x, x_range[i])
    scda_total = (fx_plus_h + fx_minus_h - (2*fx)) / (step**2)
    return scda_total


def cda(x_range, step, fnc, x):
    fx_plus_h = numpy.zeros(len(x_range))
    fx_minus_h = numpy.zeros(len(x_range))
    for i in range(len(x_range)):
        fx_plus_h[i] = fnc.subs(x, x_range[i] + step)
        fx_minus_h[i] = fnc.subs(x, x_range[i] - step)
    cda_total = (fx_plus_h - fx_minus_h) / (2 * step)
    return cda_total


def bda(x_range, step, fnc, x):
    fx_h = numpy.zeros(len(x_range))
    fx = numpy.zeros(len(x_range))
    for i in range(len(x_range)):
        fx_h[i] = fnc.subs(x, x_range[i] - step)
        fx[i] = fnc.subs(x, x_range[i])
    bda_total = (fx - fx_h) / step
    return bda_total


def fda(x_range, step, fnc, x):
    fx_h = numpy.zeros(len(x_range))
    fx = numpy.zeros(len(x_range))
    for i in range(len(x_range)):
        fx_h[i] = fnc.subs(x, x_range[i] + step)
        fx[i] = fnc.subs(x, x_range[i])
    fda_total = (fx_h - fx) / step
    return fda_total


def expression(x_t, fnc, x):
    # Define a list of zeroes the size of the range of x_t as y_t
    # iterate through this new list of zeroes
    # for each index of y_t, take the mathematical function "fnc"
    # take the symbol from "fnc" and substitute the index of x_t
    y_t = numpy.zeros(len(x_t))
    for i in range(len(x_t)):
        y_t[i] = fnc.subs(x, x_t[i])
    return y_t


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
