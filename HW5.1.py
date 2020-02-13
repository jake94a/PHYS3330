"""
Description:


Function:

"""

import sympy as sym
import matplotlib.pyplot as plt
import numpy as np


def expression(x_t, fnc):
    # Define a list of zeroes the size of the range of x_t as y_t
    # iterate through this new list of zeroes
    # for each index of y_t, take the mathematical function "fnc"
    # take the symbol from "fnc" and substitute the index of x_t
    y_t = np.zeros(len(x_t))
    for i in range(len(x_t)):
        y_t[i] = fnc.subs(t, x_t[i])
    return y_t


t_array = np.arange(0, 2, 0.01)
t = sym.symbols('t')
position = 3 * t ** 4 - 6 * t ** 3 + 2 * t ** 2 - 5 * t + 2
velocity = sym.diff(position)
acceleration = sym.diff(velocity)

y_t_position = expression(t_array, position)
y_t_velocity = expression(t_array, velocity)
y_t_acceleration = expression(t_array, acceleration)

plt.title("HW5.1")
plt.plot(t_array, y_t_position)
plt.plot(t_array, y_t_velocity)
plt.plot(t_array, y_t_acceleration)
plt.figlegend(("position", "velocity", "acceleration"))
plt.show()
