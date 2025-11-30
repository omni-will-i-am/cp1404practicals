"""
CP1404/CP5632 Practical
Unreliable car child class
"""
from random import uniform
from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability attribute."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car."""
        drive_chance = uniform(0, 100)
        if drive_chance < self.reliability:
            return super().drive(distance)
        else:
            return 0