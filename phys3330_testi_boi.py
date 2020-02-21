"""
Exam 1
Jake Anderson
PHYS 3330
----
Description:
Your objective for this test is to write a functional program
that will simulate projectile motion in varying conditions. Your code should use the trapezoid rule to perform
numerical quadratures of acceleration functions to determine the resulting velocity of an object. This step should
then be repeated, integrating the velocity to obtain the position as a function of time. The program should terminate
execution before the object falls below the ground (y=0). This process should be done in both the x and y directions
and the actual path of the projectile should be plotted in an x-y coordinate system. Use an increment size of 0.01
throughout the exam.
Problem setup:
A 1kg object is launched from a cannon with an initial velocity of 50 m/s, at an angle of 30o.
Plot the trajectory of the object (y as a function of x) under normal gravity (1 g) in the absence of air resistance.
What is the range of the cannon in meters?
Download the attached ‘.txt’ files, which include readings from a nearby force sensor. These data provide the
horizontal force acting on the projectile as a function of time (from 0 to 10 seconds). Plot the resulting trajectory
for each level of variable air resistance.
Choose one of the air resistance files above and plot the trajectory of the object for varying initial velocities (
i.e., 40, 50, 65, 90…). Plot all (4) of these trajectories on the same plot. Repeat this process for 4 different
inclination angles (for a fixed velocity). Plot these trajectories on the same graph.

Function:
Plot y as a fnc of x with no air resistance. What is dx?
"""

import numpy as yourmom
import matplotlib.pyplot as sexy_boi


def read_file(some_txt):
    return_list = []
    for line in some_txt:
        return_list.append(float(line.strip()))
    return return_list


# import txt files
hecka_wind = open("hecka_wind.txt", "r")
little_wind = open("little_wind.txt", "r")
lotta_wind = open("lotta_wind.txt", "r")
mother_of = open("mother_of.txt", "r")
noooooo = open("noooooo.txt", "r")
son_of_a = open("son_of_a.txt", "r")
list_of_files = [hecka_wind, little_wind, lotta_wind, mother_of, noooooo, son_of_a]

# initial conditions
mass_of_obj = 1  # kg
initial_velocity = 50  # m/s
angle_of_traj = 30  # degrees
y_final = 0  # meters
gravity = -9.8  # m/s**2
t_step = 0.01  # seconds
t_min = 0  # seconds
t_max = 10  # seconds
t_range = yourmom.arange(t_min, t_max + t_step, t_step)

# read the contents of the .txt files
file_read_list = []
for i in list_of_files:
    file_read_list.append(read_file(i))

"""
Problem 1.
Plot the trajectory of the object (y as a function of x) under normal gravity (1 g) in the absence of air 
resistance. What is the range of the cannon in meters? 
Assume canon is firing in +x and +y directions
v = v_0 + a * t
d = ((v + v_0) / 2) * t
d = v_0 * t + (1/2) * a * t**2
v**2 = v_0**2 + 2 * a * d
x_velocity is constant
y_velocity is not constant
v_x = d_x/t
x_distance = x_velocity * time
We have:
a = -9.8
v_0 = 50sin(30)
v_f = 0 (when ball reaches arc)
t = -
d = what we want
use: v**2 = v_0**2 + 2 * a * d
use: d = (-v_0**2) / (2 * a)
then find 2 * t 
then use: d = v_0 * t + (1/2) * a * t**2
"""

y_initial_velocity = initial_velocity * yourmom.sin(angle_of_traj)
y_distance = []

total_time = 2 * (y_initial_velocity / gravity)
total_time_range = yourmom.arange(0, total_time, t_step)

x_velocity = yourmom.zeros(len(total_time_range)) + initial_velocity * yourmom.cos(angle_of_traj)
x_distance = x_velocity * total_time_range

for i in total_time_range:
    y_distance.append((-y_initial_velocity * i) + (1 / 2) * gravity * i ** 2)
# print(y_distance)

sexy_boi.plot(x_distance, y_distance)
sexy_boi.title("Prob 1")
sexy_boi.figlegend([f'max distance is {x_distance[-1]}'])
sexy_boi.show()

"""
Problem 2.
Download the attached ‘.txt’ files, which include readings from a nearby force sensor. These data provide the 
horizontal force acting on the projectile as a function of time (from 0 to 10 seconds). Plot the resulting trajectory 
for each level of variable air resistance. 

each file is a list of force values, so to find 'a' we need to divide each value by mass
but mass is just 1, so we can assume force = acceleration
"""

x_displacement_air_resistance_list = []
for i in file_read_list:
    new_list = []
    index = 0
    for j in i:
        new_list.append(max(x_velocity) * t_range[index] + (1 / 2) * j * t_range[index] ** 2)
        index += 1
    x_displacement_air_resistance_list.append(new_list)

y_distance_new = y_distance[:1001]
for i in range(len(x_displacement_air_resistance_list)):
    sexy_boi.plot(x_displacement_air_resistance_list[i], y_distance_new)
sexy_boi.title("Prob 2")
sexy_boi.show()

"""
Problem 3.
Choose one of the air resistance files above and plot the trajectory of the object for varying initial velocities 
(i.e., 40, 50, 65, 90…). Plot all (4) of these trajectories on the same plot. Repeat this process for 4 different 
inclination angles (for a fixed velocity). Plot these trajectories on the same graph. 
"""

prob_three_initial_velocity_list = list(range(30, 121, 30))
air_resistance_file = file_read_list[3]

prob_three_x_initial_velocity = []
prob_three_y_initial_velocity = []

for i in prob_three_initial_velocity_list:
    prob_three_x_initial_velocity.append(i * yourmom.cos(angle_of_traj))
    prob_three_y_initial_velocity.append(i * yourmom.sin(angle_of_traj))

prob_three_x_displacement_air_resistance_list = []
for i in prob_three_initial_velocity_list:
    return_list = []
    index = 0
    for j in air_resistance_file:
        return_list.append(i * t_range[index] + (1 / 2) * j * t_range[index] ** 2)
        index += 1
    prob_three_x_displacement_air_resistance_list.append(return_list)

for i in range(len(prob_three_x_displacement_air_resistance_list)):
    sexy_boi.plot(prob_three_x_displacement_air_resistance_list[i], y_distance_new)

sexy_boi.title("Prob 3.1")
sexy_boi.show()


"""Prob 3.1"""
prob_three_launch_angle_list = [12, 37, 63, 80]
for i in prob_three_launch_angle_list:
    vary_angle_x_vel = initial_velocity * yourmom.cos(i)
    vary_angle_y_vel = initial_velocity * yourmom.sin(i)

vary_x_displacement_list = []
for i in prob_three_launch_angle_list:
    return_list = []
    index = 0
    for j in air_resistance_file:
        return_list.append(i * t_range[index] + (1 / 2) * j * t_range[index] ** 2)
        index += 1
    vary_x_displacement_list.append(return_list)

for i in range(len(vary_x_displacement_list)):
    sexy_boi.plot(vary_x_displacement_list[i], y_distance_new)

sexy_boi.title("Prob 3.2")
sexy_boi.show()
