# Re-learning OOP in Python 3


class MyClass:
    
    # this is a class attribute
    species = 'human'

    # this is an instance method 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method to print strings instead of memory alloc
    # also called "dunder methods" -> "__methods__"
    def __str__(self):
        return f'{self.name} is {self.age} years old'

    # these are some methods
    def get_description(self):
        return f'{self.name} is {self.age} years old'
    def speak(self, sound):
        return f'{self.name} is saying {sound}'

