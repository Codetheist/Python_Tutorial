# ****************************************************************************************************
# Assignment Final
# Program By: Antoine Gustave
# File Name: final_exam.py
# Function:
# Question #1
# Using the students dictionary below, answer the following questions.

# Using a for loop and if statement, print the names of all students over the age of 50.
# Using a single line of code, update Johns age to 56.

# Question #2
# Use the Cart class below. Note, this version is slightly modified from our class notes. Make sure to use this version, not the version from your notes.
# Add this method to the cart class: def validate_price(self, name)
# This method will validate an item price. If the price is negative, a ValueError will be raised. If the price is not negative, the function doesn't do anything additional.
# ******************************************************************************************************

# Question 1:

students = {
    'John' :
    {
        'email' : 'john@irsc.edu',
        'phone' : '555-1234',
        'address' : '123 irsc st',
        'age': 55
        },
        
    'Mary' :
    {
        'email' : 'mary@irsc.edu',
        'phone' : '555-1235',
        'address' : '500 irsc st',
        'age': 44
    },

    'Chris' :
    {
        'email' : 'chris@irsc.edu',
        'phone' : '555-1236',
        'address' : '900 irsc st',
        'age': 33
    },
    
    'Alison' :
    {
        'email' : 'alison@irsc.edu',
        'phone' : '555-1237',
        'address' : '1205 irsc st',
        'age': 22
    }
}

for student in students:
    if students[student]["age"] > 50:
        print(student)

students['John']['age'] = 56

# Question 2:
class Cart:
    def __init__(self, inv):
        self.inventory = inv
        self.total = 0.00

    def add(self, name):

        expires = self.inventory[name]['expires']
        if expires < 100:
            raise ValueError("Item is expired")

        price = self.inventory[name]['price']
        self.total += price

    def validate_price(self, name):
        check_valid = self.inventory[name]['price']
        if check_valid < 0:
            raise ValueError("Item cannot be negative")
    
    def __str__(self):
        s = f'Total is {self.total}'
        return s

inventory = {
    'apple': {'price': 1.05, 'expires': 105},
    'milk': {'price': -3.00, 'expires': 120},
    'bread': {'price': 2.50, 'expires': 95}
}

#print(inventory['apple']['price'])
c = Cart(inventory)
c.add('apple')
c.add('apple')
# c.validate_price('milk')