# ****************************************************************************************************
# Assignment #3
# Program By: Antoine Gustave
# File Name: shippingCosts.py
# Function:Create a program which calculates shipping costs.
# Ask the user for package size in pounds and the speed of delivery (slow, medium,fast).
# Use the following to calculate prices based on weights:
# 0-1 lbs: $5 per pound
# 1-3 lbs: $3 per pound
# 3-10 lbs: $1 per pound
# If the speed is slow, multiply the result by by 1.0 (no change),
# medium costs 10% more (multiply by 1.1), and fast costs 50% more (1.5).
# Output the final shipping cost.
# ******************************************************************************************************

print("***********************************")
print("*                                 *")
print("*          Shipping Cost          *")
print("*                                 *")
print("***********************************")

print("***********************************")
print("  0 - 1 lbs: $5 per pound          ")
print("  1 - 3 lbs: $3 per pound          ")
print("  3 - 10 lbs: $1 per pound         ")
print("***********************************")

print("***********************************")
print("  1. Slow = no charge              ")
print("  2. Medium = package total + 10%  ")
print("  3. Fast = package total + 50%    ")
print("***********************************")


def shippingCost():
    packagesize = float(input("Please enter the package weight(lbs): "))
    
    deliveryspeed = float(input("Please enter the speed of delivery: "))
    
    if 0 <= packagesize <= 1:
        
        packagesize = packagesize * 5.0
        
        if deliveryspeed == 1:
            deliveryspeed = 0 * packagesize
        
        elif deliveryspeed == 2:
            deliveryspeed = packagesize * 1.1
        
        elif deliveryspeed == 3:
            deliveryspeed = packagesize * 1.5
        
        totalcost = packagesize + deliveryspeed
        
        print(f"Total shipping cost: ${round(totalcost, 2)}")

    elif 1 <= packagesize <= 3:
        
        packagesize = packagesize * 3.0
        
        if deliveryspeed == 1:
            deliveryspeed = 0 * packagesize
        
        elif deliveryspeed == 2:
            deliveryspeed = packagesize * 1.1
        
        elif deliveryspeed == 3:
            deliveryspeed = packagesize * 1.5
        
        totalcost = packagesize + deliveryspeed
        
        print(f"Total shipping cost: ${round(totalcost, 2)}")

    elif 3 <= packagesize <= 10:
        
        packagesize = packagesize * 1.0
        
        if deliveryspeed == 1:
            deliveryspeed = 0 * packagesize
        
        elif deliveryspeed == 2:
            deliveryspeed = packagesize * 1.1
        
        elif deliveryspeed == 3:
            deliveryspeed = packagesize * 1.5
        
        totalcost = packagesize + deliveryspeed
        
        print(f"Total shipping cost: ${round(totalcost, 2)}")

    else:
        print("\n")
        print("Incorrect values")


shippingCost()
