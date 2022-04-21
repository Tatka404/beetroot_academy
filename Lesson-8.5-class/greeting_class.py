class Person:
    def __init__(self, f, l, a):
        self.firstname = f
        self.lastname = l
        self.age = a

    def talk(self):
        print(f'Hi! I am {self.firstname} {self.lastname}, {int(self.age)} years old')


person_attributes = Person('Ivchyk', 'Tetiana', '28')
person_attributes.talk()
