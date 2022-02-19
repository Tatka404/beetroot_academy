import random

random_number = random.randint(1, 10)
player_guess = int(input("Let's start? Guess any number from 1 to 10: "))

if player_guess < 1 or player_guess > 10:
    print("Your input is out of scope! >_<")
elif player_guess == random_number:
    print("You are a wizard! ^_^")
else:
    print("Try again... :(")


