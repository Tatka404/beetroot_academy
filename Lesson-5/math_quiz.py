first_value = 2
second_value = 2
quiz_answer = first_value + second_value

player_answer = float(input(f'How much is {first_value} + {second_value}? '))

if player_answer == quiz_answer:
    print('You are a genius!')
else:
    print('Oh no ...')
