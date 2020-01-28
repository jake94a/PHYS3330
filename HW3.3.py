import tkinter
import numpy
import matplotlib.pylab as plt
import matplotlib.image as mpimg

from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

# find photo and read it in then display using plt
some_path = filedialog.askopenfilename(title="Open Image")
absolute_path = "C:/Users/freak/PycharmProjects/Interconnection POC/my_photo.jpg"
relative_path = "my_photo.jpg"
im = mpimg.imread(some_path)


# make photo grayscale
def img_process(some_image):
    # get the num of rows/columns in the image
    # create an array of zeroes (white space) the same size as image
    num_rows = numpy.size(im, 0)
    num_cols = numpy.size(im, 1)
    bw_img = numpy.zeros([num_rows, num_cols])
    for i in range(num_rows):
        for j in range(num_cols):
            bw_img[i, j] = numpy.mean(some_image[i, j])
            # normalize to 0:1
            bw_img[i, j] = bw_img[i, j] / 255
    return bw_img


def contrast_stretch(some_image):
    # get the num of rows/columns in the image
    # create an array of zeroes (white space) the same size as image
    num_rows = numpy.size(im, 0)
    num_cols = numpy.size(im, 1)
    cs_img = numpy.zeros([num_rows, num_cols])
    # raster through image
    for i in range(num_rows):
        for j in range(num_cols):
            cs_img[i, j] = numpy.square(some_image[i, j])
            # cs_img[i, j] = numpy.sqrt(some_image[i, j])
    return cs_img


g_image = img_process(im)
cs_image = contrast_stretch(g_image)

plt.figure(1)
plt.title("Original")
plt.imshow(im)

plt.figure(2)
plt.title("Grayscale")
plt.imshow(g_image, cmap="gray")

plt.figure(3)
plt.title("Contrast Stretch")
plt.imshow(cs_image, cmap="gray")

plt.figure(4)
plt.title("Histogram, Grayscale")
plt.hist(g_image, bins=100)

plt.figure(5)
plt.title("Histogram, Contrast Stretched")
plt.hist(cs_image, bins=100)

plt.show()
