"""
Description:
Write a function that takes a user-inputted integer and determine if that number is prime.
If the input is prime, let the user know
If the input is not prime, let the user know
A number is prime if it's only factors and 1 and the number itself
Example, 17 is prime because the only integers that return whole numbers via division of 17 are 1 and 17.

Function:
Take user input of integer "n"
Create a list of numbers from 2 to n (do not include zero because n/0 returns a divide by zero error)
(do not include 1 because n/1 will return n)
If a number is prime, the remainder of n/[insert any positive number greater than 0 here other than "n" or 1] will not return an integer
We can use modulo "%" here
Modulo returns the remainder of a quotient
So, We take the modulo of n and every number from 2 to n-1, and store the values that return modulo = 0
Look at the stored values. If there are none, then the number is prime.
We can use range(2, n) because range in NON inclusive (so "n" is not included in the range)
"""


import tkinter
from tkinter import simpledialog
from tkinter import messagebox


def is_prime():
    root = tkinter.Tk()
    root.withdraw()
    n = simpledialog.askfloat("Input", "Input an integer")
    n = int(n)
    this_list = []
    this_range = range(2, n)
    prime_string = f'{n} is prime.'
    not_prime_string = f'{n} is not prime.'
    # Since the range does not include 0 or 1 then handle them separately
    # Since 2 is included in the range always, we handle it separately (range(2,2) returns 0)
    # Luckily 0:2 are all prime
    if n == 0 or n == 1 or n == 2:
        messagebox.showinfo("Answer", prime_string)
        return prime_string
    else:
        for i in this_range:
            if n % i == 0:
                this_list.append(i)
            if len(this_list) == 0:
                messagebox.showinfo("Answer", prime_string)
                return prime_string
            else:
                messagebox.showinfo("Answer", not_prime_string)
                return not_prime_string


if __name__ == '__main__':
    is_prime()
