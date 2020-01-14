"""
Description:
Guess a user's number within a specified range
The user will input a range where their guess is within that range
The function will continually subdivide the range and prompt the user
if their number is above or below the new range

Function:
Using tkinter, prompt the user to input a range
The user's 'range' should simply be an integer input
Redefine the range as a list of numbers from 0 to the top limit
(n+1 since range is not inclusive)
"""

import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


def guess_the_number():
    root = tk.Tk()
    root.withdraw()
    n = simpledialog.askinteger("Input", "Input an upper range limit that your number falls within (from 0 to n)")
    the_range = len(range(0, n))
    half = int(the_range / 2)
    answer = messagebox.askyesnocancel("Question", f'Is your number {half}?')
    if answer:
        my_string = f"I'm so glad we found your number at {half}!"
        messagebox.showinfo("Answer", my_string)
        return my_string
    else:
        while answer is False:
            answer = messagebox.askyesnocancel("Question", f'Is your number greater than {half}?')
            if answer:
                half = int(half + (half / 2))


if __name__ == "__main__":
    guess_the_number()
