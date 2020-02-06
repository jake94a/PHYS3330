"""
Description:
Import all_the_things which contains the function we need

Function:
Import all_the_things and matplotlib.pyplot
plot the sin_cos() function from all_the_things
Give the title 'hw4.1'
Show the plot
"""

import all_the_things
import matplotlib.pyplot as plt

plt.plot(all_the_things.sin_cos())
plt.title("hw4.1")
plt.show()