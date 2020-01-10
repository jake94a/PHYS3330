"""
Description:
Find the max common factor of two user-inputted numbers a and b
Max factor is the largest number that each a and b are divisible by while the quotient returns an integer
(It is possible to use a while loop here, but I elected not to)
Example, 15 and 25 have a max common factor of 5 because 15/5=3 and 25/5=5, but any number larger than 5 returns decimals.

Function:
Prompt user for two integer inputs, a and b
Define strings to return to the user either with the answer or with an error
if a > b then create a range from 1:a (inclusive)
if a < b then create a range from 1:b (inclusive)
if a = b then just return a (because the max common factor of n and n is n)
Iterate through the created list and if the modulo of a/n and b/n is 0, then store n in a list
Determine the max value in the stored list
"""


import tkinter
from tkinter import messagebox
from tkinter import simpledialog


def max_common_factor():
    root = tkinter.Tk()
    root.withdraw()
    a = simpledialog.askinteger("Input", "Input first value")
    b = simpledialog.askinteger("Input", "Input second value")
    error_string = "Nope"
    equal_string = f'Max factor is {a} because the inputted values are equal'
    if a > b:
        this_range = range(1, a + 1)
    elif b > a:
        this_range = range(1, b + 1)
    else:
        return equal_string
    this_list = []
    for i in this_range:
        if a % i == 0 and b % i == 0:
            this_list.append(i)
    max_factor = max(this_list)
    answer_string = f'The max factor of {a} and {b} is {max_factor}'
    messagebox.showinfo("Answer", answer_string)
    return answer_string


if __name__ == '__main__':
    max_common_factor()
