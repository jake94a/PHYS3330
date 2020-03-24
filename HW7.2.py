import numpy
import matplotlib.pyplot as plt

t_i = [0.9, 1.3, 1.9, 2.1]
y_i = [1.3, 1.5, 1.85, 2.1]
coef_matrix = []
n = len(t_i)
for i in t_i:
    new_list = [i ** 3, i ** 2, i, 1]
    coef_matrix.append(new_list)

inverted_coef_matrix = numpy.linalg.inv(coef_matrix)
coef = numpy.matmul(inverted_coef_matrix, y_i)
coef = [float(x) for x in coef]

equation = f'{round(coef[0], 2)}x**3 + {round(coef[1], 2)}x**2 + {round(coef[2], 2)}x + {round(coef[3], 2)}'
points = zip(t_i, y_i)
x_list = numpy.arange(t_i[0], t_i[-1], 0.01)
fx_list = 0
for i in range(n):
    fx_list += x_list ** (n - 1 - i) * coef[i]

plt.plot(x_list, fx_list)
plt.plot(t_i, y_i, 'o')
plt.figlegend([equation])
plt.show()
