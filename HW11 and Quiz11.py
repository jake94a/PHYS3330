"""
Plot the analytic, implicit, and explicit solutions on the same graph. Use a step size large enough to see the
differences between each curve.
"""
import numpy
import matplotlib.pyplot as plt

h_step = 1
t_start = 0
t_end = 10
t_range = numpy.arange(t_start, t_end, h_step)

y_init = 8
t_init = 0

# HW11.1
y_analytical = 8 * numpy.exp(-1 / 2 * t_range)

# HW11.2
euler_explicit = numpy.zeros(len(t_range))
euler_explicit[0] = y_init
for i in range(len(euler_explicit) - 1):  # must subtract 1 in range since index is increased by 1 on formula
    euler_explicit[i + 1] = euler_explicit[i] * (1 - 0.5 * h_step)

# HW11.3
euler_implicit = numpy.zeros(len(t_range))
euler_implicit[0] = y_init
for i in range(len(euler_implicit) - 1):  # must subtract 1 in range since index is increased by 1 on formula
    euler_implicit[i + 1] = euler_implicit[i] / (1 + 0.5 * h_step)

"""plt.figure("HW11.4-1")
plt.title("HW11.4-1")
plt.plot(t_range, y_analytical)

plt.figure("HW11.4-2")
plt.title("HW11.4-2")
plt.plot(t_range, euler_explicit)

plt.figure("HW11.4-3")
plt.title("HW11.4-3")
plt.plot(t_range, euler_implicit)"""

# HW11.4
plt.figure("HW11.4")  # figure must come first
plt.plot(t_range, y_analytical)
plt.plot(t_range, euler_explicit, 'o')
plt.plot(t_range, euler_implicit, 'r+')
plt.title("HW11.4")
plt.figlegend(("Analytical", "Explicit", "Implicit"))  # figlegend has to come after all plot statements
plt.show()

# Quiz11
runge_kutta = numpy.zeros(len(t_range))  # y_i = runge_kutta
runge_kutta[0] = y_init
for i in range(len(runge_kutta) - 1):  # must subtract 1 in range since index is increased by 1 on formula
    runge_kutta[i + 1] = runge_kutta[i] * (
            (1 / 384) * h_step ** 4 - (1 / 48) * h_step ** 3 + (1 / 8) * h_step ** 2 - (1 / 2) * h_step + 1)
"""    k_1 = -(1/2) * h_step * runge_kutta[i]
    k_2 = runge_kutta[i] * ((1/8) * h_step**2 - (1/2) * h_step)
    k_3 = runge_kutta[i] * ((-1/32) * h_step**3 + (1/8) * h_step**2 - (1/2) * h_step)
    k_4 = runge_kutta[i] * ((1/64) * h_step**4 - (1/16) * h_step**3 + (1/4) * h_step**2 - (1/2) * h_step)
    runge_kutta[i + 1] = runge_kutta[i] + k_1/6 + k_2/3 + k_3/3 + k_4/6"""

plt.figure("Quiz11")
plt.plot(t_range, y_analytical)
plt.plot(t_range, euler_explicit, 'o')  # 'o' shows the points as circles
plt.plot(t_range, euler_implicit, 'r+')  # 'r+' shows the points as red + signs
plt.plot(t_range, runge_kutta)
plt.title("Quiz11")
plt.figlegend(("Analytical", "Explicit", "Implicit", "Runge-Kutta"))
plt.show()
