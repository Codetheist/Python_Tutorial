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


class Car:
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
mycar.print_state()
