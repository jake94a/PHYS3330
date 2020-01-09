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

    if n == 0 or n == 1 or n == 2 or n == 3:
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
