"""
Description:

Function:
right - ana
left - ana
mid - ana
trap - ana
"""

import all_the_things
import pandas
import numpy
import matplotlib.pyplot as plt

step_list = [0.1, 0.01, 0.001, 0.0001]
lower_bound = 0
upper_bound = 10
right_answer_list = []
left_answer_list = []
mid_answer_list = []
trap_answer_list = []
ana_answer_list = []
my_index = 0

for i in step_list:
    right_answer_list.append(abs(
        all_the_things.right_riemann(i, lower_bound, upper_bound) - all_the_things.ana_integration(lower_bound,
                                                                                                   upper_bound)))
    left_answer_list.append(abs(
        all_the_things.left_riemann(i, lower_bound, upper_bound) - all_the_things.ana_integration(lower_bound,
                                                                                                  upper_bound)))
    mid_answer_list.append(abs(
        all_the_things.midpoint(i, lower_bound, upper_bound) - all_the_things.ana_integration(lower_bound,
                                                                                              upper_bound)))
    trap_answer_list.append(abs(
        all_the_things.trapezoidal(i, lower_bound, upper_bound) - all_the_things.ana_integration(lower_bound,
                                                                                                 upper_bound)))
    ana_answer_list.append(abs(
        all_the_things.ana_integration(lower_bound, upper_bound) - all_the_things.ana_integration(lower_bound,
                                                                                                  upper_bound)))

my_table = pandas.DataFrame(numpy.array([right_answer_list, left_answer_list, mid_answer_list, trap_answer_list]),
                            columns=step_list, index=['right', 'left', 'mid', 'trap'])
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.table(cellText=my_table.values, colLabels=my_table.columns, loc='center', rowLabels=my_table.index, cellLoc='center')
fig.tight_layout()
plt.show()
