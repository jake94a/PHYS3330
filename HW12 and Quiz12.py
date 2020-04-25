"""
The diffusion of heat through a 2D metal plate can be modeled by the following partial differential equation:

∂ T ∂ t = α ( ∂ 2 T ∂ x 2 + ∂ 2 T ∂ y 2 ) ,

where T represents temperature and α represents the diffusivity of the material (a ratio between the thermal
conductivity and the product of the density and specific heat capacity).

1. Discretize this equation by replacing the analytic partial derivatives with numerical derivatives
(i.e., the first and second central difference approximations).

2. Calculate the time step required to preserve a stable solution.  You may find this Link to be useful.

3. Build a grid in Matlab or Python and set the initial temperature of the plate at each point, along with boundary
conditions along the edges. Choose one region of the plate to be significantly hotter than the rest of the plate,
allowing the heat to diffuse.

4. Display the temperature in the plate after 1, 2, 3, 4, 7, and 10 time steps.


Parts 1 and 2 done by hand
"""

import matplotlib.pyplot as plt
import numpy

t_range = list(range(11))
alpha_gold = 0.1  # gold = 127 * 10 ** -6
h_step = 0.04
delta_t_max = h_step ** 2 / (4 * alpha_gold)  # must follow delta_t <= h**2 / (4 * alpha) > 0
# delta_t = 0.1
delta_t = h_step ** 2 / (4.3 * alpha_gold)

if delta_t > delta_t_max:
    print("error, delta_t too large")

x = numpy.arange(-1, 1, h_step)
y = numpy.arange(-1, 1, h_step)
X, Y = numpy.meshgrid(x, y)
T = X * 0
T[(numpy.abs(X) < 0.2) & (numpy.abs(Y) < 0.2)] = 1  # square
# T[(numpy.abs(X**2 + Y**2) < 0.2)] = 1  # circle
# T[(numpy.abs(Y - X**2) < 0.2)] = 1  # parabola
# T[(numpy.abs(2 * X) < 0.2) & (numpy.abs(Y) < 0.2)] = 1  # rektangle
# T[numpy.abs(X*Y) < 0.1] = 1  # hyperbola
T_time = [T]

for time in range(50):
    next_t = T.copy()
    for i in range(1, len(X) - 1):
        for j in range(1, len(Y) - 1):
            next_t[i][j] = T_time[-1][i][j] * (1 - (4 * alpha_gold * delta_t) / h_step ** 2) + \
                           ((alpha_gold * delta_t) / h_step ** 2) * (T_time[-1][i][j - 1] + T_time[-1][i - 1][j]
                                                                     + T_time[-1][i + 1][j] + T_time[-1][i][j + 1])
    T_time.append(next_t)

time_steps = [0, 1, 2, 3, 4, 7, 10, 50]
fig, ax = plt.subplots(nrows=2, ncols=4)
i = 0
for steps in time_steps:
    col = i % 4
    row = int(i / 4)
    ax[row][col].pcolormesh(X, Y, T_time[steps], vmin=0, vmax=1)
    ax[row][col].title.set_text(f'{steps} time steps')
    ax[row][col].axis('off')
    i += 1

plt.show()
