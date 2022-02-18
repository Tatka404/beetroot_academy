try:
    first_number = int(input('Enter your first number: '))
    second_number = int(input('Enter your second number: '))

    def euclidean_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    print(f'The gcd of {first_number} and {second_number} is: {(euclidean_gcd(first_number, second_number))}')
except ValueError:
    print('Ooops! Number must be an integer :(')


