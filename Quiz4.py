import numpy as np
import matplotlib.pyplot as plt

a = 2
x = np.arange(a, 5, 0.01)
f = np.log(1 + x)


def log_taylor(n_terms):
    error_list = []
    ms = np.log(1 + a)
    for i in range(1, n_terms + 1):
        # print(ms, i)
        nth_term = pow(-1, i + 1) * pow((x - a), i) / (i * pow((1 + a), i))
        ms += nth_term
        error_list.append(nth_term)
    return ms
    # plt.title(f'Error is {nth_term[-1]}')

log_taylor(5)
plt.plot(x, f)
plt.plot(x, log_taylor(3))
plt.plot(x, log_taylor(5))
plt.plot(x, log_taylor(10))
plt.plot(x, log_taylor(20))
plt.figlegend(("Original Plot", 'n = 3', 'n = 5', 'n = 10', 'n = 20'))
plt.show()
