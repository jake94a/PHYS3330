"""
Description:
Show a plot of a taylor series of log(x+1) about a = 2

Function:
Using numpy and matplotlib
define "about" point as 2
define a range of x-values
define the original function
Create a taylor series
"""

import numpy as np
import matplotlib.pyplot as plt

a = 2
x = np.arange(1, 7, 0.001)
f = np.log(1 + x)


def log_taylor(n_terms):
    # define first value of the taylor series
    taylor_series = np.log(1 + a)
    for i in range(1, n_terms + 1):
        # this is the taylor series for log(x+1)
        nth_term = pow(-1, i + 1) * pow((x - a), i) / (i * pow((1 + a), i))
        # n_th term is every nth value of the taylor series evaluated at every x-value in the range
        # add nth term to the taylor series then return it
        taylor_series += nth_term
    return taylor_series


plt.plot(x, f)
plt.plot(x, log_taylor(3))
plt.plot(x, log_taylor(5))
plt.plot(x, log_taylor(10))
plt.plot(x, log_taylor(20))
plt.ylim(-5, 5)
plt.figlegend(("Original Plot", 'n = 3', 'n = 5', 'n = 10', 'n = 20'))
plt.show()
