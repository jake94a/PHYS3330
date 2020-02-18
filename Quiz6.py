"""
Description:
Find location and velocity of rock after it falls for 6 seconds
t = 6s
a = -9.8m/s
a = dv/dt
v = dx/dt

Function:
v = a*t
d = int(v) from t_range
"""

import numpy
import matplotlib.pyplot as plt

t_max = 6
t_min = 0
t_step = 0.01
t_range = numpy.arange(t_min, t_max, t_step)
t_range_plot = numpy.arange(t_min, t_max - t_step, t_step)
fnc_array = numpy.zeros(len(t_range)) - 9.8


def trapezoidal(step, lower, upper, function_array):
    inte_sum = 0
    t_values_trap = numpy.arange(lower, upper + step, step)
    # return_array = numpy.zeros(len(t_values_trap))
    return_array = []
    plot_array = []
    try:
        for i in range(len(t_values_trap)):
            f_a = function_array[i]
            f_b = function_array[i + 1]
            inte_sum += ((f_a + f_b) / 2) * step
            # return_array[i] = inte_sum
            return_array.append(inte_sum)
            plot_array.append(t_values_trap[i])
    except:
        pass
    return return_array, plot_array


velocity_bounds = trapezoidal(t_step, t_min, t_max, fnc_array)[1]
velocity = trapezoidal(t_step, t_min, t_max, fnc_array)[0]

displacement_bounds = trapezoidal(t_step, t_min, t_max, velocity)[1]
displacement = trapezoidal(t_step, t_min, t_max, velocity)[0]

absement_bounds = trapezoidal(t_step, t_min, t_max, displacement)[1]
absement = trapezoidal(t_step, t_min, t_max, displacement)[0]

plt.plot(velocity_bounds, velocity)
plt.plot(displacement_bounds, displacement)
plt.plot(absement_bounds, absement)
plt.show()
