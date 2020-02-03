import numpy as np
import matplotlib.pyplot as plt

x = 8
f = np.log(1 + x)
n = 25

ms = 0
for i in range(1, n + 1):
    print(ms, i)
    ms += pow(-1, i + 1) * pow(x, i) / i

print(f)
print(ms)