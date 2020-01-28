"""
Description:
Sort a list of random integers in ascending order
Return the sorted list

Function:
1)
Using tkinter, prompt the user for a length of vector that they want "n"
Initiate an empty list to append random values to
Iterate "n" times
On each iteration, append a random value to the empty list
Return the now filled list
2)
Determine the length of the list
Initiate an empty list to append minimum values to
Iterate through the list and only append the minimum value of the list to the new list while
    removing the minimum value from the original list
Return the now-ascending-sorted list
"""
import tkinter
from tkinter import simpledialog
from tkinter import messagebox
from random import randint

root = tkinter.Tk()
root.withdraw()


def create_random_list():
    n = simpledialog.askinteger(title="A number", prompt="Input a length of vector")
    return_list = []
    length_of_list = range(n)
    for i in length_of_list:
        return_list.append(randint(0, 100))
    return return_list


def sorting_hat(a_list):
    my_range = range(len(a_list))
    return_list = []
    for i in my_range:
        return_list.append(min(a_list))
        a_list.remove(min(a_list))
    messagebox.showinfo("Answer", return_list)
    return return_list


print(sorting_hat(create_random_list()))
