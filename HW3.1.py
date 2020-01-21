"""
Description:
Accept two square matrices from user and determine the size of the matrices
Multiply the matrices together and return the result to the user

Function:
Use numpy to create an array with numpy.array()
    or create a list of lists, which accomplishes the same result
"""

import pandas
import tkinter
import numpy


def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)


root = tkinter.Tk()
root.geometry('500x500')
root.title("Jake's Matrix Program")
txt = tkinter.Entry(root, width=10)
txt.grid(column=0, row=1)
lbl = tkinter.Label(root, text="Input your numbers")
lbl.grid(column=0, row=0)
btn = tkinter.Button(root, text="Click this", command=clicked)
btn.grid(column=1, row=0)
root.mainloop()

"""
a = [[1, 4, 5, 12],
     [-5, 8, 9, 0],
     [-6, 7, 11, 19]]

print(a)


b = numpy.array([[1, 2, 3],
                [4, 5, 6]])
print(b)
print(type(b))

for i in b:
    print(i)
    for j in i:
        print(j)
"""
"""
Description:
Accept two square matrices from user and determine the size of the matrices
Multiply the matrices together and return the result to the user

Function:
Use numpy to create an array with numpy.array()
    or create a list of lists, which accomplishes the same result
"""

import pandas
import tkinter
import numpy

from tkinter import simpledialog
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()
"""
num_arrays = 2
ask_bool = messagebox.askyesno("Question", f'We will be using {num_arrays} matrices. Is that ok?')

if ask_bool:
    pass
else:
    messagebox.showinfo("Output", "Lol that's too bad")

"""
def create_array(a_number, matrix_index):
    b_array = []
    index_item = 0
    for j in range(a_number):
        a_list = []
        for m in range(a_number):
            num_append = simpledialog.askinteger("Input", f'Input index [{j},{m}] for matrix number {matrix_index}')
            a_list.append(num_append)
            index_item += 1
        b_array.append(a_list)
    print(b_array)
    return b_array

"""
list_of_arrays = []
i = 0
n = simpledialog.askinteger("Input", "How large of a matrix do you want?")
while i < num_arrays:
    list_of_arrays.append(create_array(n, i + 1))
    i += 1
"""
t = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
#print(test_list_of_arrays[1][1][1])
product_array = []
for a in t: #list_of_arrays:
    #print(f'first iteration: {a}')
    for b in a:
        print(f'second iteration: {b}')
        for c in b:
            #print(f'third iteration: {c}')
            product_array.append(c)

print(product_array)
print(t[0][0][0], t[0][0][1], t[0][1][0], t[0][1][1], t[1][0][0], t[1][0][1], t[1][1][0], t[1][1][1])

#product_array.append((t[0][0][0] * t[1][0][0]) + (t[0][0][1] * t[1][1][0]))
#product_array.append((t[0][0][0] * t[1][0][1]) + (t[0][0][1] * t[1][1][1]))
#product_array.append((t[0][1][0] * t[1][0][0]) + (t[0][1][1] * t[1][1][0]))
#product_array.append((t[0][1][0] * t[1][0][1]) + (t[0][1][1] * t[1][1][1]))


"""
a = [[1, 4, 5, 12],
     [-5, 8, 9, 0],
     [-6, 7, 11, 19]]

print(a)


b = numpy.array([[1, 2, 3],
                [4, 5, 6]])
print(b)
print(type(b))

for i in b:
    print(i)
    for j in i:
        print(j)
"""
