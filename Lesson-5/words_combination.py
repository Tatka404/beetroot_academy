from random import choice

given_word = input('Your word: ')

result = [''.join(choice(given_word) for x in range(len(given_word))) for y in range(5)]

print(f'Your random words are {result}')
