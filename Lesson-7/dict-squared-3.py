i = list(range(1, 11))
j = [i**2 for i in range(1, 11)]

my_dict = dict((key, value) for (key, value) in zip(i, j))

print(my_dict)
