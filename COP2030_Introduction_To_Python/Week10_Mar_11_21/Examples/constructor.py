# Learning about OOP
"""class Dog:

    # Constructor
    def __init__(self, dogname, dogbreed):
        #print('Running Constructor')
        self.name = dogname
        self.breed = dogbreed

    def speak(self):
        print('Bark')

    def say_hello(self):
        print(f'My name is {self.name}')
        print(f'My breed is {self.breed}')

mydog = Dog('Rover', 'Lab')
# mydog.speak()
mydog.say_hello()

mydog2 = Dog('Rover', 'Lab')
# mydog.speak()
mydog2.say_hello()"""


"""class Car:
    def __init__(self):
        self.gear = 0

    def shift_up(self):
        if self.gear <= 6:
            self.gear += 1

    def shift_down(self):
        if self.gear >= 0:
            self.gear -= 1

    def print_state(self):
        print(f'Gear is {self.gear}')


mycar = Car()
mycar.print_state()

mycar.shift_down()
mycar.print_state()

mycar.shift_up()
mycar.print_state()"""


class Animal:

    def __init__(self, w, a):
        self.weight = w
        self.age = a

# Inheritance from the Animal class and its args


class Cat(Animal):

    def speak(self):
        print('Meow')
        print(f'My age is {self.age}')
        print(f'My weight is {self.weight}')


class Dog(Animal):

    def speak(self):
        print('Bark')
        print(f'My age is {self.age}')
        print(f'My weight is {self.weight}')


mycat = Cat(9, 3)
mycat.speak()

print()

mydog = Dog(50, 5)
mydog.speak()
