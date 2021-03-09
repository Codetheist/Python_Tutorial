# grades = [82.4, 90.1, 75.4, 79.9]

# total = 0.0
# for grade in grades:
#     total += grade
#     avg = total / len(grades)
#     print(avg)

# def max_val(numbers):
    #grades = [82.4, 90.1, 75.4, 79.9]

#     largest = numbers[0]

#     for number in numbers:
#         if number > largest:
#             largest = grade
#     return largest

# grades = [82.4, 90.1, 75.4, 79.9]
# max_val(grades)

# learning how to use file handling.
with open("data.csv") as f:
    for line in f:
        line = line.rstrip()
        print(line)