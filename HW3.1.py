"""
Description:
Accept two square matrices from user and determine the size of the matrices
Multiply the matrices together and return the result to the user

Function:
Use numpy to create an array with numpy.array()
    or create a list of lists, which accomplishes the same result
Accept user input for the size of a matrix. If the user inputs 2, then create a 2x2 matrix, etc
Create a product matrix initialized as a matrix of zeroes, then add the matrix index products
"""

import tkinter

from tkinter import simpledialog
from tkinter import messagebox

# a root window is not used for this mini-gram so close it out
root = tkinter.Tk()
root.withdraw()

# for this mini-gram, we are asked for the product of TWO matrices, so make the number of matrices (or arrays) static
num_arrays = 2
ask_bool = messagebox.askyesno("Question", f'We will be using {num_arrays} matrices. Is that ok?')

# for the lolz
if ask_bool:
    pass
else:
    messagebox.showinfo("Output", "Lol that's too bad")

# determine how large of a matrix the user wants
# the matrices will always be square and the same size
n = simpledialog.askinteger("Input", "How large of square matrices do you want?")


# I didn't end up using this function but I'm keeping it here for future reference
def transpose(some_array):
    # define an array to return as an empty list
    return_array = []
    for i in range(len(some_array[0])):
        # initialize an empty array
        row = []
        for item in some_array:
            # take some_array and break it down into separate lists (rows)
            # take the ith item in each list (each row) and append it to the empty list "row"
            row.append(item[i])
        # after "row" has been iterated through and appended, it is a full list
        # take the full list and place it into "return_array" then redefine "row" as an empty list
        return_array.append(row)
    return return_array


def create_array(a_number, matrix_number):
    # a_number is user input for the size of square matrix they want
    # define an empty list to append user-input values into
    return_array = []
    index_item = 0
    # for a square matrix, the size of the matrix must be iterated over twice
    # so a 2x2 matrix would be two "for i in range(2)" loops, one loop for each row
    for j in range(a_number):
        # this row_list will reset when each column is filled completely
        row_list = []
        for m in range(a_number):
            num_append = simpledialog.askinteger("Input", f'Input index [{j},{m}] for matrix number {matrix_number}')
            row_list.append(num_append)
            index_item += 1
        return_array.append(row_list)
    return return_array


def zeroes_array(a_number):
    return_array = []
    for i in range(a_number):
        row_list = []
        for j in range(a_number):
            row_list.append(0)
        return_array.append(row_list)
    return return_array


def matrix_product(array_1, array_2, matrix_square):
    # initialize the return_array as a square matrix of zeroes
    return_array = zeroes_array(matrix_square)
    for i in range(len(array_1)):
        for j in range(len(array_2[0])):
            for k in range(len(array_2)):
                return_array[i][j] += array_1[i][k] * array_2[k][j]
    return return_array


list_of_arrays = []
matrix_index = 0
while matrix_index < num_arrays:
    list_of_arrays.append(create_array(n, matrix_index + 1))
    matrix_index += 1

# the while loop creates a list of lists of lists, so we need to access each array by its index
first_array = list_of_arrays[0]
second_array = list_of_arrays[1]
product_array = matrix_product(first_array, second_array, n)
messagebox.showinfo("Answer", str(product_array))
