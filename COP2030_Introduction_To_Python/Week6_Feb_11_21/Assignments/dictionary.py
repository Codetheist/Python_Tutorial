# ****************************************************************************************************
# Assignment #5
# Program By: Antoine Gustave
# File Name: dictionary.py
# Function:
# 1. Print all the students names using a loop
# 2. Print all the email addresses using a loop
# 3. Create a new student named 'Bob' and assign him a fake email, phone, and address. This should be exactly four lines of code.
# 4. In a single line of code, print Mary's phone
# ******************************************************************************************************

students = {
    'John': {
        'email': 'john@irsc.edu',
        'phone': '555-1234',
        'address': '123 irsc st'
    },

    'Mary': {
        'email': 'mary@irsc.edu',
        'phone': '555-1235',
        'address': '500 irsc st'
    },

    'Chris': {
        'email': 'chris@irsc.edu',
        'phone': '555-1236',
        'address': '900 irsc st'
    },

    'Alison': {
        'email': 'alison@irsc.edu',
        'phone': '555-1237',
        'address': '1205 irsc st'
    }
}

students['Bob'] = {
    'email': 'bob@irsc.edu',
    'phone': '555-1238',
    'address': '2500 irsc st'
}

for name, email in students.items():
    print(f'Name: {name} and their email: {students[name]["email"]}\n')

print(f"Mary number is: {students['Mary']['phone']}")
