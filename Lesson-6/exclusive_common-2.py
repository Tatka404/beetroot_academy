import random

my_first_list = [random.randint(0, 10) for i in range(10)]
my_second_list = [random.randint(0, 10) for j in range(10)]

common_list = list(set(my_first_list).intersection(my_second_list))

print('The common integers between the two lists are:', common_list)
