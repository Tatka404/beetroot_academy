import random

random_number = random.randint(1, 10)
player = int(input('Let\'s start? Guess any number from 1 to 10: '))

if player > 10 or player < 1:
    print('Your input is out of scope! >_<')
elif not player == random_number:
    print('Try again... :(')
elif player == random_number:
    print('You are a wisard! ^_^')
