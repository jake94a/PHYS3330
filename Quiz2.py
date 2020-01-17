"""
Description:
Create a function that generates a list of random numbers then returns the max and min of that list

Function:
This function will use the 'random' and 'tkinter' python packages
Display a dialog box to the user explaining what's about to happen so they can prepare themselves
Ask the user to input an integer value for the size of list that they want "num values"
Ask the user to input an integer value for the lower bound of random numbers to be generated
Ask the user to input an integer value for the upper bound of random numbers to be generated
Define an initial "min value" as the upper bound of random numbers
    Do this to ensure that, if the list has more than one unique value, a new "min value" will be assigned later
Define an initial "max value" as the lower bound of random numbers
    Do this to ensure that, if the list has more than one unique value, a new "max value" will be assigned later
Create a list of length "num values"
Iterate through the list and assign a random integer to each index
If the iterative value is greater or less than the current "max value" or "min value"
    then reassign the respective variable to the iterative value
    If the iterative value is not greater or less than the current "max value" or "min value" then don't do anything
Return both max and min values to the user
"""

import random

from tkinter import messagebox
from tkinter import simpledialog


def max_min():
    messagebox.showinfo("Description", "This program will return the max and min values from a random set of numbers "
                                       "generated with the requirements that you, the user, set.")
    num_values = simpledialog.askinteger("Input", "Input how large of a list you would like")
    lower_bound = simpledialog.askinteger("Input", "Input a lower bound of random values")
    upper_bound = simpledialog.askinteger("Input", "Input an upper bound of random values")
    my_list = []
    max_val = lower_bound
    min_val = upper_bound
    test_value_string = f'True max is {max(my_list)}. True min is {min(my_list)}'

    for i in range(num_values):
        my_list.append(random.randint(lower_bound, upper_bound))

    for i in range(len(my_list)):
        if my_list[i] > max_val:
            max_val = my_list[i]
        elif my_list[i] < min_val:
            min_val = my_list[i]
        else:
            pass

    messagebox.showinfo("Output", f'The max value generated is {max_val}. The min value generated is {min_val}.')
    print(my_list)
    return max_val, min_val


if __name__ == '__main__':
    max_min()
