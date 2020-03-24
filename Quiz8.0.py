"""
Write a 2D interpolated image out to a 1D data file (.txt). Using another program, read this 1D data file into the
program and convert it into a 2D matrix manually, without using the resize tool. Display the image.
"""
import numpy
import matplotlib.pyplot as plt

read_file = open("Quiz8.txt")

n_rows = int(read_file.readline())
n_cols = int(read_file.readline())
n_colors = int(read_file.readline())

image_array = numpy.zeros(shape=(n_rows, n_cols, n_colors))
for rows in range(n_rows):
    for cols in range(n_cols):
        for colors in range(n_colors):
            image_array[rows][cols][colors] = float(read_file.readline()) / 255

plt.imshow(image_array)
plt.show()
