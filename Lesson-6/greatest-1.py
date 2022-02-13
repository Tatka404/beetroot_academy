import random

my_random_list = [random.randint(0, 10) for i in range(10)]
my_random_list.sort()

print('The greatest numbrer from the list of random ones is:', my_random_list[-1])
