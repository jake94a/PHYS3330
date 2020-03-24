"""
Write a 2D interpolated image out to a 1D data file (.txt). Using another program, read this 1D data file into the
program and convert it into a 2D matrix manually, without using the resize tool. Display the image.
618 x 385
"""

import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

batman = mpimg.imread("Batman.jpg")
output = open("Quiz8.txt", "w")
n_rows = batman.shape[0]
n_cols = batman.shape[1]
n_colors = batman.shape[2]
output.write(str(n_rows) + '\n' + str(n_cols) + '\n' + str(n_colors) + '\n')

for row in batman:
    for col in row:
        for color in col:
            output.write(str(color) + '\n')

output.close()
