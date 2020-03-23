"""
Description:
Make a spline

Function:

"""
import matplotlib.pyplot as plt

t_i = [0.9, 1.3, 1.9, 2.1]
y_i = [1.3, 1.5, 1.85, 2.1]


def h_values(t_list):
    h_list = []
    for i in range(len(t_list)):
        if i + 1 < len(t_list):
            h_list.append(round(t_list[i + 1] - t_list[i], 2))
        else:
            h_list.append(None)
    return h_list


def b_values(h_list, y_list):
    b_list = []
    for i in range(len(h_list)):
        if i + 1 < len(y_list):
            b_list.append(round((1 / h_list[i]) * (y_list[i + 1] - y_list[i]), 4))
        else:
            b_list.append(None)
    return b_list


def v_values(h_list):
    v_list = []
    for i in range(len(h_list)):
        if (i - 1 < 0) or (h_list[i] is None):
            v_list.append(None)
        else:
            v_list.append(2 * (h_list[i - 1] + h_list[i]))
    return v_list


def u_values(b_list):
    u_list = []
    for i in range(len(b_list)):
        if (i - 1 < 0) or (b_list[i] is None):
            u_list.append(None)
        else:
            u_list.append(round(6 * (b_list[i] - b_list[i - 1]), 2))
    return u_list


list_of_h = h_values(t_i)
list_of_b = b_values(h_values(t_i), y_i)
list_of_v = v_values(h_values(t_i))
list_of_u = u_values(b_values(h_values(t_i), y_i))
print(list_of_h)
print(list_of_b)
print(list_of_v)
print(list_of_u)

v_h_matrix = []
for i in range(len(t_i)):
    print(i)
    if i > len(list_of_v):
        pass
    else:
        blank_list = [list_of_v[i], list_of_h[i]]
        v_h_matrix.append(blank_list)
print(v_h_matrix)