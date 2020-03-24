"""
Using the spline formulas posted on Canvas, derive a matrix equation that solves for the unknown spline coefficients
for the 4 data included above. Plot the cubic splines passing through each point:
"""
import numpy
import matplotlib.pyplot as plt


def h_values(t_list):
    h_list = []
    for i in range(len(t_list)):
        if i + 1 < len(t_list):
            h_list.append(round(t_list[i + 1] - t_list[i], 2))
        else:
            h_list.append(0)
    return h_list


def b_values(h_list, y_list):
    b_list = []
    for i in range(len(h_list)):
        if i + 1 < len(y_list):
            b_list.append(round((1 / h_list[i]) * (y_list[i + 1] - y_list[i]), 4))
        else:
            b_list.append(0)
    return b_list


def v_values(h_list):
    v_list = []
    for i in range(len(h_list)):
        if (i - 1 < 0) or (h_list[i] is None):
            v_list.append(0)
        else:
            v_list.append(2 * (h_list[i - 1] + h_list[i]))
    return v_list


def u_values(b_list):
    u_list = []
    for i in range(len(b_list)):
        if (i - 1 < 0) or (b_list[i] is None):
            u_list.append(0)
        else:
            u_list.append(round(6 * (b_list[i] - b_list[i - 1]), 2))
    return u_list


def s_equation(z_list, h_list, t_list, y_list, index):
    x_list = numpy.arange(t_list[index], t_list[index + 1], 0.01)
    first_term = (z_list[index + 1] / (6 * h_list[index])) * (x_list - t_list[index]) ** 3
    second_term = (z_list[index] / (6 * h_list[index])) * (t_list[index + 1] - x_list) ** 3
    third_term = ((y_list[index + 1] / h_list[index]) - ((z_list[index + 1] / 6) * h_list[index])) * \
                 (x_list - t_list[index])
    fourth_term = ((y_list[index] / h_list[index]) - ((h_list[index] / 6) * z_list[index])) * \
                  (t_list[index + 1] - x_list)
    return first_term + second_term + third_term + fourth_term, x_list


t_i = [0.9, 1.3, 1.9, 2.1]
y_i = [1.3, 1.5, 1.85, 2.1]
n = len(t_i)
x_i = numpy.arange(t_i[0], t_i[n-1], 0.01)

if len(t_i) != len(y_i):
    print("t array and y array not equal lengths")

v_h_matrix = numpy.zeros((n - 2, n - 2))

list_of_h = h_values(t_i)
list_of_b = b_values(h_values(t_i), y_i)
list_of_v = v_values(h_values(t_i))
list_of_u = u_values(b_values(h_values(t_i), y_i))
print(list_of_h)
print(list_of_b)
print(list_of_v)
print(list_of_u)

v_h_matrix[0][0] = list_of_v[1]
v_h_matrix[0][1] = list_of_h[1]
v_h_matrix[n - 3][n - 4] = list_of_h[n - 3]
v_h_matrix[n - 3][n - 3] = list_of_v[n - 2]

"""
use v_h_matrix inverse * u to find z matrix
"""

inverted_v_h = numpy.linalg.inv(v_h_matrix)
list_of_u = list_of_u[1:n-1]
list_of_z_np = numpy.matmul(inverted_v_h, list_of_u)
list_of_z = [x for x in list_of_z_np]
list_of_z.insert(0, 0)
list_of_z.append(0)


plt.plot(s_equation(list_of_z, list_of_h, t_i, y_i, 0)[1], s_equation(list_of_z, list_of_h, t_i, y_i, 0)[0])
plt.plot(s_equation(list_of_z, list_of_h, t_i, y_i, 1)[1], s_equation(list_of_z, list_of_h, t_i, y_i, 1)[0])
plt.plot(s_equation(list_of_z, list_of_h, t_i, y_i, 2)[1], s_equation(list_of_z, list_of_h, t_i, y_i, 2)[0])
plt.show()

