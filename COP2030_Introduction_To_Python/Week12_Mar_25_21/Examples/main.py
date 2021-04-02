# Separating out normal correct running code from our error handling code
def weeks_to_days(weeks):
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
    print(e)


class Car:
    def __init__(self):
        print('Constructor being called')
        self.current_gear = 0


mycar = Car()
