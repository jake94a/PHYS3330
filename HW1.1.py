"""
Description:
Make a user-input function that takes a positive integer input n and returns n values of the fibonacci sequence
Use tkinter to allow users to input their value via dialogue box
User matplotlib to plot the returned values

Function:
root.withdraw() allows tkinter windows to open and close
Ask the user for integer input using simpledialog
The fibonacci sequence is: sum(x, x-1) starting at x=0 where (n-1) doesn't exist if x=0
If the user inputs n=0, the function should just return 0
Take the user input and add it to pre-defined 0 and 1
The first few values of the fibonacci sequence are [0, 1, 1, 2, 3, 5, 8, 13...]
"""


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
