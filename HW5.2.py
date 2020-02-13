"""
scda: (f(x+h) + f(x-h) - 2*f(x)) / (h^2)
sfda: (f(x+(2*h)) - 2*f(x+h) + f(x)) / h^2
sbda: (f(x) - 2*f(x-h) + f(x-(2*h))) / h^2
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import all_the_things


def fda(x_range, step, fnc):
    fx_h = np.zeros(len(x_range))
    fx = np.zeros(len(x_range))
    for i in range(len(x_range)):
        fx_h[i] = fnc.subs(t, x_range[i] + step)
        fx[i] = fnc.subs(t, x_range[i])
    fda_total = (fx_h - fx) / step
    return fda_total

h = 0.01
t_array = np.arange(0, 2, h)
t = sym.symbols('t')
position = 3 * t ** 4 - 6 * t ** 3 + 2 * t ** 2 - 5 * t + 2

# velocity analysis
velocity_ana = sym.diff(position)
y_t_velocity_ana = all_the_things.expression(t_array, velocity_ana, t)
y_t_velocity_num_fda = all_the_things.fda(t_array, h, position, t)
y_t_velocity_num_bda = all_the_things.bda(t_array, h, position, t)
y_t_velocity_num_cda = all_the_things.cda(t_array, h, position, t)
# difference of...
diff_of_fda = abs(y_t_velocity_ana - y_t_velocity_num_fda)
diff_of_bda = abs(y_t_velocity_ana - y_t_velocity_num_bda)
diff_of_cda = abs(y_t_velocity_ana - y_t_velocity_num_cda)

# acceleration analysis
acceleration_ana = sym.diff(velocity_ana)
y_t_accerlation_ana = all_the_things.expression(t_array, acceleration_ana, t)
"""
y_t_acceleration_num_sfda = all_the_things.sfda(t_array, h, position, t)
y_t_acceleration_num_sbda = all_the_things.sbda(t_array, h, position, t)
y_t_acceleration_num_scda = all_the_things.scda(t_array, h, position, t)
"""
y_t_acceleration_num_sfda = all_the_things.fda(t_array, h, velocity_ana, t)
y_t_acceleration_num_sbda = all_the_things.bda(t_array, h, velocity_ana, t)
y_t_acceleration_num_scda = all_the_things.cda(t_array, h, velocity_ana, t)
# difference of...
diff_of_sfda = abs(y_t_accerlation_ana - y_t_acceleration_num_sfda)
diff_of_sbda = abs(y_t_accerlation_ana - y_t_acceleration_num_sbda)
diff_of_scda = abs(y_t_accerlation_ana - y_t_acceleration_num_scda)

plt.figure(1)
plt.plot(t_array, diff_of_fda)
plt.plot(t_array, diff_of_bda)
plt.plot(t_array, diff_of_cda)
plt.figlegend(("FDA", "BDA", "CDA"))

plt.figure(2)
plt.plot(t_array, diff_of_sfda)
plt.plot(t_array, diff_of_sbda)
plt.plot(t_array, diff_of_scda)
plt.figlegend(("SFDA", "SBDA", "SCDA"))
plt.show()
