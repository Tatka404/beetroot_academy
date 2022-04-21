class Dog:
    age_factor = 7

    def __init__(self, h=int(input('enter your dog age: '))):
        self.human_years = h

    def human_age(self):
        return f'Your dog is {self.human_years * self.age_factor} human years old'


lisa = Dog()
print(lisa.human_age())
