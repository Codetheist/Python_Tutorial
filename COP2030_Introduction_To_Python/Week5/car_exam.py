# Created by: Antoine Gustave


def rent_car():
    age = int(input("Enter age: "))

    if age > 0 and age < 18:
        print("You're too young to rent the car.")
    elif age >= 18 and age < 25:
        days = int(input("Enter number of days you want to rent: "))
        price = 65
        total_price = days * price
        print(
            f"The price is ${price} and you'll rent for {days} days. Your total is ${total_price}")
    elif age >= 25:
        days = int(input("Enter number of days you want to rent: "))
        price = 55
        total_price = days * price
        print(
            f"The price is ${price} and you'll rent for {days} days. Your total is ${total_price}")
    else:
        print("Invalid input.")


rent_car()
