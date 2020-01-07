import matplotlib.pyplot as plt


def fib(n):
    fib_list = []
    i = 0
    j = 1
    if n < 0:
        string = "Error, need value greater than 0"
        return string
    elif n == 0:
        return i
    else:
        fib_list.append(i)
        fib_list.append(j)
        while len(fib_list) < n:
            a = i + j
            i = j
            j = a
            fib_list.append(a)
    plt.plot(fib_list)
    plt.show()
    return fib_list


print(fib(10))
