"""
Description:
Make an array (list of lists) with random values
Prompt the user for an integer value "n"
Return the nth lowest value in the array and its index (row, column)

Function:
Sort the array into an ascending or descending list
find nth value

"""
import tkinter
import numpy

from tkinter import simpledialog
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

num_rows = simpledialog.askinteger("Prompt", "How many rows do you want?")
num_cols = simpledialog.askinteger("Prompt", "How many columns do you want?")
lower_bound = simpledialog.askinteger("Prompt", "Input an lower bound of random integers")
upper_bound = simpledialog.askinteger("Prompt", "Input an upper bound of random integers")
user_prompt = simpledialog.askinteger("Prompt", "Which 'n'th lowest value do you want?")

my_array = numpy.random.randint(lower_bound, upper_bound, (num_rows, num_cols))
nth_lowest_string = ""

if user_prompt == 1:
    nth_lowest_string = "st"
elif user_prompt == 2:
    nth_lowest_string = "nd"
elif user_prompt == 3:
    nth_lowest_string = "rd"
else:
    nth_lowest_string = "th"

my_list = []
returned_list = []
size = my_array.shape
lowest_value = upper_bound
highest_value = lower_bound

# raster scan
for i in my_array:
    for j in i:
        returned_list.append(j)
returned_list.sort()
nth_lowest_index = user_prompt - 1
nth_lowest = returned_list[nth_lowest_index]
string_list = []

# raster scan
i = 0
for n in my_array:
    j = 0
    # print(f'i is {i}')
    i += 1
    for m in n:
        # print(f'j is {j}')
        j += 1
        if m == nth_lowest:
            messagebox.showinfo("Answer", f'{my_array}' '\n'
                                          f'The {user_prompt}{nth_lowest_string} lowest value is {nth_lowest}''\n'
                                          f'{user_prompt}{nth_lowest_string} lowest value at index: [{i - 1}, {j - 1}]'
                                          '\n' f'{user_prompt}{nth_lowest_string} lowest value at position: [{i}, {j}]')
            # print(f'{user_prompt}{nth_lowest_string} lowest value at index: [{i-1}, {j-1}]')
            # print(f'{user_prompt}{nth_lowest_string} lowest value at position: [{i}, {j}]')

"""for i in range(user_prompt):
    for j in my_array:
        for k in j:
            if k < lowest_value:
                lowest_value = k
            if k < lowest_value and k != lowest_value:
    returned_list.append(lowest_value)"""

# print(my_array.shape)
#print(my_array)
# print(lowest_value)
# print(returned_list)
#print(nth_lowest)

#messagebox.showinfo("answer", f'The {user_prompt}{nth_lowest_string} lowest value is {nth_lowest}')
