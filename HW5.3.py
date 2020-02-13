"""
Description:

Function:

"""
from matplotlib import cm
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = fig.gca(projection='3d')

x_range = numpy.arange(0, 10, 0.01)
y_range = numpy.arange(0, 10, 0.01)
x_range, y_range = numpy.meshgrid(x_range, y_range)
potential_energy = numpy.sin(x_range / 2) * numpy.cos(y_range / 2)
grad_ux = (-1/2)*numpy.cos(x_range/2)*numpy.cos(y_range/2)
grad_uy = (1/2)*numpy.sin(x_range/2)*numpy.sin(y_range/2)

plt.figure(1)
surf1 = ax.plot_surface(x_range, y_range, potential_energy, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.figure(2)
plt.streamplot(x_range, y_range, grad_ux, grad_uy)

plt.show()

