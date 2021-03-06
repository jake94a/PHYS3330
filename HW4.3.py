"""
Description:

Function:

"""

import all_the_things
import matplotlib.pyplot as plt

all_the_things.hw4_2()
plt.plot(all_the_things.sin_cos())
plt.plot(all_the_things.sin_cos_taylor(1))
plt.plot(all_the_things.sin_cos_taylor(2))
plt.plot(all_the_things.sin_cos_taylor(3))
plt.plot(all_the_things.sin_cos_taylor(5))
plt.plot(all_the_things.sin_cos_taylor(10))
plt.plot(all_the_things.sin_cos_taylor(15))
plt.plot(all_the_things.sin_cos_taylor(20))
plt.plot(all_the_things.sin_cos_taylor(25))
plt.plot(all_the_things.sin_cos_taylor(50))
plt.ylim(-5, 5)
plt.figlegend(("Original Plot", 'n = 1', 'n = 2', 'n = 3', 'n = 5', 'n = 10', 'n = 15', 'n = 20', 'n = 25', 'n = 50'))
plt.show()
