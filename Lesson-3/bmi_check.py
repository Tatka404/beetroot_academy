weight = 90
height = 150

index = weight / height ** 2

lower_bound = 18.5
upper_bound = 25

result = lower_bound < index < upper_bound

print(f'Your BMI is normal: {result}')

