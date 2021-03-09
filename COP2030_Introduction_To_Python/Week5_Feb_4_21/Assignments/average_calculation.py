# ******************************************************************************
# Assignment #4
# Program By: Antoine Gustave
# File Name: average_calculation.py
# Function:For this program, use the following list:
# [10.0, 15.2, 38.4, 80.6, 44.2]
# Create a program which finds the average of this list.
# The program should create a function called average which takes
# in a list and returns the average of the list.
# The program must use a for loop.
# Use the "max_value" and "grade average" examples as a template.
# Do not hard-code any sizes. Use the len() function.
# ******************************************************************************

tickets = [10.0, 15.2, 38.4, 80.6, 44.2]

def average(tickets):
    total_cost = 0.0
    for ticket in tickets:
        total_cost += ticket
        average_sales = round(total_cost / len(tickets), 2)
    
    return average_sales

print(f"The average is: {average(tickets)}")

largest = 0.0
def max_value(tickets):
    largest = tickets[0]
    for ticket in tickets:
        if ticket > largest:
            largest = ticket
    return largest

print(f"The max value is: {max_value(tickets)}")
