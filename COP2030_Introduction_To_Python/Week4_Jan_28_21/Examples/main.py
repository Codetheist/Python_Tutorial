#learning about while loops\
#i = 0

#while True:
#    if i < 10:
#        print(i)

#learning about list 
#grades = [82.3, 93.1, 88.7]
#grades.append(92.2)
#print(grades)
#print(grades[0])

#Error because it is out of range
#print(grades[7])

#learning the for loop
#total = 0.0
#for grade in grades:
#    total = total + grade

#average = total / grades
#print(f'Average is: {average}')

#learning about range
#r = range(5)

#for i in range(len(grades)):
#    print(grades[i])

#briefly talk about enumerate
#for i, grade in enumerate(grades):
#    print(grade)

#learning about dictionaries
#phonebook = {}
#phonebook['alice'] = '555-1111'
#phonebook['bob'] = '555-2222'

#print(phonebook['alice'])

#phonebook['alice'] = '555-1112'
#print(phonebook['alice'])

#searching the phonebook by name
#name = input('Enter name: ')
#name = name.lower()

#checking to see if name is in the phonebook
#if name in phonebook:
#    phone = phonebook[name]
#    print(phone)
#else:
#    print('Name not found')

#for name in phonebook:
#    print(name)
#    number = phonebook[name]
#    print(number)

#missed_number = '555-2222'
#for name, number in phonebook.items():
    #print(f'Name: {name} Number: {number}')
    #if number == missed_number:
    # print(name)
    # break

#learning about functions
def add_numbers(a, b):
    results = a + b
    return result

total = add_numbers(2,3)
print(total)

x = 2
y = 5
total = add_numbers(x, y)
print(total)