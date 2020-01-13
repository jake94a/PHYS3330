"""
Description:
Create a function that accepts two user-inputted integers, a and b
Determine if a is divisible by b "a/b"
Using modulo, determine a % b
If the modulo of a / b is zero, then the function should return true
In any other case (modulo is not zero) then the function should return false

Function:
Using tkinter, allow the user to input two integers into a dialogue box
Define those two inputs as a and b
Since the user inputs happen within the function, we don't need to define function parameters
Operate on a and b, such that if a % b = 0, then True, else False
If True, then we know that a is divisible by b, and return a message to the user
If False, then we know that a is not divisible by b, return a message to the user
Use tkinter to open a messagebox with the returned message
"""

import tkinter as tk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb


def is_divisible():

    root = tk.Tk()
    root.withdraw()
    a = sd.askinteger("Input", "Input an integer")
    b = sd.askinteger("Input", "Input another integer")
    answer = a % b

    if answer == 0:
        string = f'{a} is divisible by {b}'
    else:
        string = f'{a} is not divisible by {b}, with a remainder of {answer}'
    mb.showinfo("Answer", string)
    return string


if __name__ == "__main__":
    is_divisible()
