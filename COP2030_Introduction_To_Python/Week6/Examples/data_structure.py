# Learning about data structure
numbers = [5, 3, 2, 9, 3, 11, 15]


# Get an element
num = numbers[3]
print(num)

# Negative indexing
# gET THE LAST ELEMENT
num = numbers[-1]
print(num)

# indexing using variable
idx = 2
num = numbers[idx]
print(num)

# slicing
nums = numbers[1:4]
print(nums)

# count by
nums = numbers[0:-1:2]  # counts every other number
print(nums)


# adding lists
p1 = [1, 8, 3]
p2 = [-4, 19]
nums = p1 + p2
print(nums)

# slicing strings
s = 'Hello from COP2030'
sub = s[0:5]
print(sub)

# zip
p1 = [1, 3, 7]
p2 = [2, -5, 4]
for item in zip(p1, p2):
    print(item)

# Learning about dictionaries
phonebook = {
    'alice': '555-1111',
    'bob': '555-2222'
}
phonebook['charles'] = '555-3333'  # Creating a new key and value
phonebook['alice'] = '555-4444'  # Updates the key with a new value
for key in phonebook:  # loops key & value
    print(key)
    print(phonebook[key])

for key, val in phonebook.items():  # prints key and value as pairs
    print(f'Name: {key} Number: {val}')

phonebook = {
    'alice': {
        'phone': '555-1111',
        'email': 'alice@example.com'
    },
    'bob': {
        'phone': '555-2222',
        'email': 'bob@example.com'
    }
}

email = phonebook['alice']['email']
print(email)

name = input("Enter name: ").lower()
mode = input("Enter mode: ").lower()
result = phonebook[name][mode]
print(result)
