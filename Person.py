class Person:
    def __init__(self, name, age, gender, interests=[]):
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.interests = interests

    def hello(self):
        interest = ', '.join(self.interests)
        print(f'Hello, my name is {self.name} and I am {self.age} years old. My interests are {interest}.')
        return self.hello
        
person = Person('Adrian',26,'Male',['being a hardarse','agile','ssd hard drives'])
greeting = person.hello()


