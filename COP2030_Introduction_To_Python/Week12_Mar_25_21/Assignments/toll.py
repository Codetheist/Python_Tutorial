# ****************************************************************************************************
# Assignment #
# Program By: Antoine Gustave
# File Name: toll.py
# Function:Assume today's date is 100.
# For this toll, a car is $1.00 and truck is $1.50.  As each vehicle passes through the toll, keep a sum total of the total funds collected as well as total number of vehicles.. 
# If a license plate is expired, an exception should be raised so the vehicle can be flagged (just raise the exception, don't worry about handling it)
# ******************************************************************************************************


vehicles = {
    'ABC746': {
        'type':'car',
        'expires': 105
    },
    'ZZA398': {
        'type':'truck',
        'expires': 110
    },
    'BFH918': {
        'type':'car',
        'expires': 90
    },
}