# Separating out normal correct running code from our error handling code
"""def weeks_to_days(weeks):
    if weeks > 0:
        days = weeks * 7
        return days
    else:
        raise ValueError("Weeks must be postitive")


try:
    days = weeks_to_days(2)
    print(days)
except ValueError as e:
    print("An error happened")
    print(e)"""


"""class Car:
    def __init__(self):
        print('Constructor being called')
        self.current_gear = 0

    def shift_up(self):
        self.current_gear += 1

    def shift_down(self):
        if self.current_gear >= 0:
            self.current_gear -= 1
        else:
            raise ValueError('Cannot shift lower than -1')

    def __str__(self):
        s = f'Current gear is {self.current_gear}'
        return s


mycar = Car()
mycar.shift_up()
print(mycar)

try:
    mycar.shift_down()
    mycar.shift_down()
    mycar.shift_down()
except clear:
    print('Could not shift')
    print(e)

print(mycar)"""


class Cart:

    def __init__(self, inv):
        # pass is a placeholder instead of leaving it blank and causing errors
        self.inventory = inv
        self.total = 0.0

    def add(self, name):
        # the first square brackets [name] adds the entire dict
        # the second square brackets ['price'] finds the value needed
        expires = self.inventory[name]['expires']
        if expires < 100:
            raise ValueError('Item is expired')

        price = self.inventory[name]['price']
        self.total += price

    def __str__(self):
        s = f'Total is {self.total}'
        return s


inventory = {
    'apple': {'price': 1.05, 'expires': 105},
    'milk': {'price': 3.00, 'expires': 120},
    'bread': {'price': 2.50, 'expires': 95}
}

c = Cart(inventory)
c.add('apple')
print(c)
