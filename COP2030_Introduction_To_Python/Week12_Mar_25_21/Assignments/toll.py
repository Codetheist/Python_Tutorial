# ****************************************************************************************************
# Assignment #6
# Program By: Antoine Gustave
# File Name: toll.py
# Function:Assume today's date is 100.
# For this toll, a car is $1.00 and truck is $1.50.  As each vehicle passes through the toll,
# keep a sum total of the total funds collected as well as total number of vehicles..
# If a license plate is expired, an exception should be raised so the vehicle
# can be flagged (just raise the exception, don't worry about handling it)
# ******************************************************************************************************

# Create a TollBooth class.
class TollBooth:
    def __init__(self, lpn):
        self.vehicles = lpn
        self.total_price = 0.0
        self.total_vehicles = 0

    # The class will have a function/method called

    # lpn is short for license plate number
    def charge_toll(self, lpn):
        expires = self.vehicles[lpn]['expires']
        if expires < 100:
            raise ValueError('License plate expires')
        car_charge = 1.00
        truck_chage = 1.50
        vehcile_type = self.vehicles[lpn]['type']
        
        if vehcile_type == "car":
            self.total_price += car_charge
            self.total_vehicles += 1
        
        if vehcile_type == "truck":
            self.total_price += truck_chage
            self.total_vehicles += 1

    def __str__(self):
        s = f'Total price is ${self.total_price} and the total of vehicles {self.total_vehicles}'
        return s


# Use the following dictionary to represent all the vehicles
vehicles = {
    'ABC746': {
        'type': 'car',
        'expires': 105
    },
    'ZZA398': {
        'type': 'truck',
        'expires': 110
    },
    'BFH918': {
        'type': 'car',
        'expires': 90
    },
}

try:
    check_plate = TollBooth(vehicles)
    check_plate.charge_toll("ABC746")
    check_plate.charge_toll('ZZA398')
    check_plate.charge_toll('BFH918')
    print(check_plate)
except ValueError as e:
    print('Could not find')
    print(e)
