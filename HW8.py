"""
Using a pre-built spline interpolation package, perform 2D interpolation as follows:

1. Upsample the image to a size of 2472 x 1540.

2. Downsample the image to a size of 154 x 96.

3. Resize the image to 618 x 500.
"""
import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

batman = mpimg.imread("Batman.jpg")
n_rows = batman.shape[0]
n_cols = batman.shape[1]

batman_red = batman[..., 0]
batman_green = batman[..., 1]
batman_blue = batman[..., 2]
batman_list = [batman_red, batman_green, batman_blue]


def rescale(image, resample_x, resample_y):
    resized_image = np.zeros(shape=(resample_y, resample_x, 3))

    for i in range(3):
        current_image = image[..., i]
        x = np.linspace(0, 1, image.shape[1])
        y = np.linspace(0, 1, image.shape[0])
        X, Y = np.meshgrid(x, y)
        Z = current_image

        x2 = np.linspace(0, 1, resample_x)
        y2 = np.linspace(0, 1, resample_y)
        f = interp2d(x, y, Z, kind='cubic')
        Z2 = f(x2, y2)
        Z2 = Z2-np.min(Z2)
        Z2 = Z2/np.max(Z2)
        resized_image[..., i] = Z2

    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].imshow(image)

    X2, Y2 = np.meshgrid(x2, y2)
    ax[1].imshow(resized_image)


rescale(batman, 2472, 1540)
plt.show()
rescale(batman, 154, 96)
plt.show()
rescale(batman, 618, 500)
plt.show()


