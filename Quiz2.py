import random

my_list = []
for i in range(100):
    my_list.append(random.randint(0, 100))

max_num = 0
for i in range(len(my_list)):
    try:
        if my_list[i] > my_list[i + 1]:
            max_num = my_list[i]
    except IndexError:
        pass

print(max_num)
