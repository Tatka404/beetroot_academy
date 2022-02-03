
# letter H
for row in range(5):
    for col in range(9):
        if col == 0 or col == 8 or (row == 2 and (0 < col < 8)):
            print('#', end='')
        else:
            print(end=' ')
    print()


# letter O
for row in range(5):
    for col in range(9):
        if col == 0 or col == 8 or row == 0 or row == 4:
            print('#', end='')
        else:
            print(end=' ')
    print()


