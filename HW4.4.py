"""
To plot error between taylor series and original function, take each as a list with f(x) where x is a list of
pre-defined values and f(x) is saved as a new list.
f1(x) is the original function
f2(x) is the taylor series
f3(x) is the difference of f1 - f2
plot x_num vs f3 - this is error

I am an idiot, all of this could've been done in a for loop but I did it explicitly like a CHUMP
"""
import matplotlib.pyplot as plt
import all_the_things

"""n_values_list = [1, 2, 3, 5, 10, 15, 20, 25, 50]
for i in n_values_list:
    plt.plot(all_the_things.sin_cos_taylor(i))
plt.show()"""

f0 = all_the_things.sin_cos()
f1 = all_the_things.sin_cos_taylor(1)
f2 = all_the_things.sin_cos_taylor(2)
f3 = all_the_things.sin_cos_taylor(3)
f4 = all_the_things.sin_cos_taylor(5)
f5 = all_the_things.sin_cos_taylor(10)
f6 = all_the_things.sin_cos_taylor(15)
f7 = all_the_things.sin_cos_taylor(20)
f8 = all_the_things.sin_cos_taylor(25)
f9 = all_the_things.sin_cos_taylor(50)
f1_diff = f1 - f0
f2_diff = f2 - f0
f3_diff = f3 - f0
f4_diff = f4 - f0
f5_diff = f5 - f0
f6_diff = f6 - f0
f7_diff = f7 - f0
f8_diff = f8 - f0
f9_diff = f9 - f0
plt.plot(f1_diff)
plt.plot(f2_diff)
plt.plot(f3_diff)
plt.plot(f4_diff)
plt.plot(f5_diff)
plt.plot(f6_diff)
plt.plot(f7_diff)
plt.plot(f8_diff)
plt.plot(f9_diff)
plt.ylim(-5, 5)
plt.figlegend(('n = 1', 'n = 2', 'n = 3', 'n = 5', 'n = 10', 'n = 15', 'n = 20', 'n = 25', 'n = 50'))
plt.show()
