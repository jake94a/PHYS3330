"""
The attached text file contains a signal waveform, composed of two sine waves, which has been corrupted by noise.
This can be expressed mathematically as:

LaTeX: y(t) = A1 sin(2π f1 t) + A2 sin(2π f2 t) + Noise

1. Create a program that reads in the file and plots it as a function of time.

2. Use the fast Fourier transform function to create a power spectrum for the data.
follow mathworks example

3. Using the power spectrum, determine the values of A1, A2, f1, and f2.

4. Use an inverse FFT to denoise the sample.
"""
import matplotlib.pyplot as plt
import numpy


def read_file(some_txt):
    return_list = []
    for line in some_txt:
        return_list.append(float(line.strip()))
    return return_list


hw_txt = open("hw9_waveform.txt", "r")  # open the text file
hw9_values = read_file(hw_txt)  # read through the text file and save each line in a list
time_list = [t for t in range(len(hw9_values))]  # for each in the hw9_values list, save 0:n iterating
fs = 1500
ts = 1/fs
length_of_sample = len(hw9_values)

noisy_function = numpy.fft.fft(hw9_values)
half_length = int(length_of_sample/2)
p2 = numpy.abs(noisy_function / length_of_sample)
p1 = p2[:half_length]
p1[1:-2] = 2*p1[1:-2]

ps_constant = int(fs/length_of_sample)
power_spec = [ps_constant * index for index in range(half_length)]

# Answers to HW9.3
a1 = 0.96
f1 = 32
a2 = 1.37
f2 = 67

fixed_noisy_function = numpy.fix([(x/.5).real for x in noisy_function])*.5
ifft_function = numpy.fft.ifft(fixed_noisy_function)

plt.figure("HW9.1")
plt.title("HW9.1")
plt.plot(time_list, hw9_values)

plt.figure("HW9.2")
plt.title("HW9.2")
plt.plot(power_spec, p1)

plt.figure("HW9.4")
plt.title("HW9.4")
plt.plot(time_list, ifft_function)
plt.show()
