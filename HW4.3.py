import numpy
import all_the_things
import matplotlib.pyplot as plt

x_num = list(numpy.arange(0, 2 * numpy.pi, 0.01))
my_function = numpy.empty(len(x_num))
the_function = all_the_things.sin_cos()
num_terms = range(1)

plt.plot(all_the_things.sin_cos())
plt.plot(all_the_things.sin_cos_taylor(1, 0, 2*numpy.pi, 0.01))
plt.show()