"""
Use your favorite denoising algorithm (I suggest 2D IFFT) to remove the salt-and-pepper noise from the quiz9_Lena.png
"""

import numpy
import matplotlib.pyplot as plt
from scipy import fftpack
from matplotlib.colors import LogNorm


def plot_spectrum(fft_image):
    plt.imshow(numpy.abs(fft_image), norm=LogNorm(vmin=5))
    plt.colorbar()


lena_image = plt.imread(
    "quiz9_Lena.png").astype(float)  # use absolute path like C:/Users/Asshole/PycharmProjects/PHYS3330/quiz9_Lena.png
fft_lena = fftpack.fft2(lena_image)
keep_fraction = 0.1
fft2_lena = fft_lena.copy()
r, c = fft2_lena.shape
fft2_lena[int(r*keep_fraction):int(r*(1 - keep_fraction))] = 0  # set value of some of the rows to 0
fft2_lena[:, int(c*keep_fraction):int(c*(1 - keep_fraction))] = 0  # set value of some of the columns to 0
lena_new = fftpack.ifft2(fft2_lena).real

plt.figure()
plt.title("Original Image")
plt.imshow(lena_image, plt.cm.gray)  # makes the plotted image grayscale

plt.figure()
plt.title("FFT Image")
plot_spectrum(fft_lena)

plt.figure()
plt.title("Filtered FFT Image")
plot_spectrum(fft2_lena)

plt.figure()
plt.title("Reconstructed Image")
plt.imshow(lena_new, plt.cm.gray)
plt.show()
