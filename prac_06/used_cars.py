"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"{limo.name} has fuel: {limo.fuel}")
    print(limo)
    limo.drive(115)
    print(f"Limo has fuel: {limo.fuel}")
    print(limo)


main()

# In the used_cars program file, write one new line of code for each of the following:
#
# Create a new Car object called "limo" that is initialised with 100 units of fuel.
#
# Add 20 more units of fuel to this new car object using the add method.
#
# Print the amount of fuel in the car.
#
# Attempt to drive the car 115 km using the drive method.
#
# Now add the __str__ method to the Car class in car.py.
# Using f-string formatting. Make it return a string in the following format:
# Car, fuel=42, odometer=277
# Remember that you can run this method by printing your car object, or passing the car object to the str() function.
# Do NOT call the method verbosely like my_car.__str__()
#
# Now add a name field to the Car class (in car.py), and adjust the __init__ and __str__ methods to set and display this respectively.
# Make the str method return the car's name instead of just "Car".
# Now add names (literals) to the constructors where you create Car objects in the used_cars.py program.
# Test your work and make sure you can now make and view named cars.
#
# In your used_cars.py program, print your car object/s to make sure that the __str__ method is working as expected.