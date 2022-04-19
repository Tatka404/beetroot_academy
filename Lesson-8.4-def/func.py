import math
from random import randint
import random


# 1
def square():
    s = int(input('Enter side of square: '))
    a, p, d = (s * s, 4 * s, s * math.sqrt(2))
    print(f'Area = {a}, Perimeter = {p}, Diagonal = {round(d, 2)}')


square()

# 2
month = int(input('Enter month: '))


def season(month):
    return ['winter', 'spring', 'summer', 'autumn'][round((month % 12) // 3, 0)]


print(season(month))


# 3
def roll_dice():
    print(f'Number is: {randint(1, 6)}')


roll_dice()


# 4
def ascii_dice(v, e=' o'):
    half = f'+ - - - - +\n|  {e[v > 1]}   {e[v > 3]}  |\n|  {e[v > 5]} '
    return f'{half}{e[v & 1]}{half[::-1]}'


def multi_dice(*d, sep='   '):
    zipped = zip(*(ascii_dice(v).splitlines() for v in d))
    return '\n'.join([sep.join(l) for l in zipped])


print(multi_dice(*random.sample(range(1, 7), 1)))


# 5
faces = int(input('How many sides on a dice? ') or '6')


def universal_dice():
    if faces:
        for die in range(faces):
            return randint(1, faces)


print(f'You have rolled: {universal_dice()}')


# 6
num_dice = int(input('How many dice? ') or '6')
num_faces = int(input('How many sides on a dice?') or '6')


def dice_busket():
    rolls = []
    for dice in range(num_dice):
        dice_roll = randint(1, num_faces)
        rolls.append(dice_roll)
    return rolls


print(f'You have rolled: {dice_busket()}')
