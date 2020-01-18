"""
Description:
Create a function that remove every nth value from a list of consecutive values
Accept a user input "n" and remove all of it's multiples

Function:
Prompt the user to supply an end value for the range
Prompt the user to supply a value that the function will remove multiples of
Define a range using user-input (I said end_value + 1 in order to include 'end_value' from the user)
Initiate an empty list to append certain values into
Using a for loop, check each value 'i' in the range and the modulo of i / n
    If the modulo is not zero, then i is not a multiple of n, and can be stored by appending it to the pre-defined list
Return the list to the user in a messagebox
"""

from tkinter import simpledialog
from tkinter import messagebox


def remove_mult():
    messagebox.showinfo("Directions", "In this program, you will be asked to input two values. The first value is an "
                                      "upper bound for a range of numbers from 1 to end_value. You, the user, "
                                      "get to decide where the range stops. Next, you will be asked to input a value "
                                      "'n' that will remove all nth multiples from the range.")
    end_value = simpledialog.askinteger("Input", "Input an upper bound integer")
    n = simpledialog.askinteger("Input", "Input a value that will remove all multiples from the range")
    range_list = range(end_value + 1)
    return_list = []

    for i in range_list:
        remainder = i % n
        if remainder != 0:
            return_list.append(i)
        else:
            pass
    messagebox.showinfo("Answer", f'Your list with multiples of {n} removed: {return_list}')
    return return_list


if __name__ == '__main__':
    remove_mult()
