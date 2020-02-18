"""
Description:
Left Riemann Sum

Function:
midpoint - ((f(a) + f(b)) / 2) * step
trap - f(a) + f(b)
"""

import numpy

# velocity_trogdor = t * numpy.sin(t)
step = 0.01
t_values_left = numpy.arange(0, 10, step)
t_values_right = numpy.arange(step, 10 + step, step)
t_values_mid = numpy.arange(0, 10 + step, step / 2)
t_values_trap = numpy.arange(0, 10 + step, step)
disp_trogdor_left = 0
disp_trogdor_right = 0
disp_trogdor_mid = 0
disp_trogdor_trap = 0

for i in t_values_left:
    disp_trogdor_left += (i * numpy.sin(i)) * step

for i in t_values_right:
    disp_trogdor_right += (i * numpy.sin(i)) * step

for i in range(len(t_values_mid)):
    if (i % 2) != 0:
        disp_trogdor_mid += (t_values_mid[i] * numpy.sin(t_values_mid[i])) * step
    else:
        pass

for i in t_values_trap:
    f_values = ((i * numpy.sin(i)) + ((i + step) * numpy.sin(i + step))) / 2
    disp_trogdor_trap += f_values * step

print(disp_trogdor_left, disp_trogdor_right, disp_trogdor_mid, disp_trogdor_trap)
