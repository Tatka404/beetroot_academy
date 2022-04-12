from datetime import datetime

# 2
with open('fio.txt', 'r') as file:
    content = file.read()
    words = content.split()
    name = words[1]
    year = words[-1]
# print(words)
# print(name)
# print(year)

your_age = datetime.now().year - int(year)

greeting = input(f'Dear {name}! Your age is {your_age}')

print(greeting)

