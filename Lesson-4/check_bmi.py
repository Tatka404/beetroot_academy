weight = float(input('What is your weight (in kg)? '))
height = float(input('What is your height (in m)? '))
index = (weight / height ** 2)
lower_bound = 18.5
upper_bound = 25

if lower_bound <= index <= upper_bound:
    print('Congratulations: your BMI is normal')
elif index < lower_bound:
    print('Bad news: your BMI is below the line')
elif index > upper_bound:
    print('Bad news: your BMI is above the line')
