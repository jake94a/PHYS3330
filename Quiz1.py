"""
Use tkinter to allow users to input via dialog boxes
and include output in dialog boxes
Prompt user for input 'n'
Test modulo of n/2
If modulo is 0, then n is even
If modulo is anything else, then n is odd
Return the answer of "even" or "odd" to the user
"""


import tkinter
from tkinter import simpledialog
from tkinter import messagebox


def is_even():
    root = tkinter.Tk()
    root.withdraw()
    n = simpledialog.askinteger("Input", "Input an integer to test")
    answer = n % 2
    if answer == 0:
        my_string = f'{n} is even'
    else:
        my_string = f'{n} is odd'
    messagebox.showinfo("Answer", my_string)
    return my_string

if __name__ == '__main__':
    is_even()