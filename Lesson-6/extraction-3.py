my_list = []
for x in range(1, 100):
    if (x % 7 == 0) and (x % 5 != 0):
        my_list.append(x)

print(my_list)
