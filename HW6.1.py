"""
Description:

Function:

"""

import sympy
import numpy

t_lower = 0
t_upper = 10
t_range = numpy.arange(0, 10, 0.01)
t = sympy.symbols('t')
velocity_trogdor = t * sympy.sin(t)
disp_trogdor = sympy.integrate(velocity_trogdor, (t, t_lower, t_upper))

print(disp_trogdor.evalf())
print(disp_trogdor)