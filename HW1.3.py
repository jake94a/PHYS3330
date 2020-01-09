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
