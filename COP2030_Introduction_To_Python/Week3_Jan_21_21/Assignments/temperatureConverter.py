# ****************************************************************************************************
# Assignment #2
# Program By: Antoine Gustave
# File Name: temperatureConverter.py
# Function: Create an interactive program to convert Fahrenheit to Celsius. Ask the user what their
# temperature is (in Fahrenheit), store the input in a variable, convert to Celsius, then output the
# temperature in Celsius.
# ******************************************************************************************************
# Fahrenheit formula: (°F − 32) × 5/9 = °C
# Celsius formula: (°C × 9/5) + 32 = °F

print("Temperature Converter Calculator.\n")

user_input = input("Do you want to convert the tem in Fahrenheit (F) or Celsius (C)? ")

if user_input == 'f' or user_input == 'F':
    fahrenheitTemp = float(input("Enter the Fahrenheit: "))
    celsiusTemp = (fahrenheitTemp - 32) * (5 / 9)
    print(f"{fahrenheitTemp}°F = {round(celsiusTemp, 1)}°C")

elif user_input == 'c' or user_input == 'C':
    celsiusTemp = float(input("Enter the Celsius: "))
    fahrenheitTemp = (celsiusTemp * (9 / 5)) + 32
    print(f"{celsiusTemp}°F = {round(fahrenheitTemp, 1)}°C")
