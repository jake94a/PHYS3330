import tkinter
import matplotlib.pyplot as plt

from tkinter import messagebox
from tkinter import simpledialog


def fib():
    root = tkinter.Tk()
    root.withdraw()
    n = simpledialog.askinteger("Input", "Gimme a whole number")
    fib_list = []
    i = 0
    j = 1
    if n < 0:
        string = "Error, need value greater than 0"
        messagebox.showinfo("Error", string)
        return string
    elif n == 0:
        messagebox.showinfo("Answer", str(i))
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
    messagebox.showinfo("Answer", str(fib_list))
    return fib_list


if __name__ == '__main__':
    fib()