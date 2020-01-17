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


def sub_divide(some_num):
    my_list = list(range(some_num + 1))
    mid_index = int(len(my_list) / 2)
    mid_value = my_list[mid_index]
    a_bool = messagebox.askyesno("Tell me your secrets", f'Is your number {mid_value}?')

    while a_bool is False:
        b_bool = messagebox.askyesno("Don't anger me", f'Is your number greater than {mid_value}?')
        if b_bool:
            del my_list[:mid_index]
            mid_index = int(len(my_list) / 2)
            mid_value = my_list[mid_index]
            a_bool = messagebox.askyesno("Tell me your secrets", f'Is your number {mid_value}?')
        else:
            del my_list[mid_index:]
            mid_index = int(len(my_list) / 2)
            mid_value = my_list[mid_index]
            a_bool = messagebox.askyesno("Tell me your secrets", f'Is your number {mid_value}?')
    return mid_value


def guess_the_number():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Instructions", "Let's play a game where I guess the number you're thinking of. I will only "
                                        "guess numbers greater than or equal to 0.")
    n = simpledialog.askinteger("Input", "Input an upper range limit that your number falls within (from 0 to n)")
    answer = sub_divide(n)
    messagebox.showinfo("Answer", f"We found your number at {answer}! I'm so good at guessing!")


if __name__ == "__main__":
    guess_the_number()
