from itertools import accumulate

# 1.2
to_do = ['1: create table', '2: alter table', '3: drop table',
         '4: truncate table','5: study sql', '6: forget sql', '7: be a human']

# 1.3
print(to_do[0])
print(to_do[2])
print(to_do[3])
print(to_do[-1])

# 1.4
length_to_split = [3, 4]

split_lists = [to_do[x - y: x] for x, y in zip(
          accumulate(length_to_split), length_to_split)]

print(split_lists)

# 1.5
to_do.extend(['8: study python', '9: create a list'])
print(to_do)

# 1*
to_do[0], to_do[-1] = to_do[-1], to_do[0]
print(to_do)

# 2*
next_task = to_do.append((input('Type down your next task: ')).lower())
print(f'your to_do list now: {to_do}')
