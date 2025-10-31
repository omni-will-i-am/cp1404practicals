"""
CP1404/CP5632 Practical - Guitar Class exercise.

Time start: 1630
Time Finish: 1708

Estimated time: 45 min
Actual time: 38 min
"""

# Write a Guitar class that allows you to store one guitar with these fields (attributes):

# name
# year
# cost

# Define the following methods:

# __init__ - with defaults name="", year=0, cost=0

# __str__ - which uses {} string formatting to return something like (using the values from above):
# Gibson L-5 CES (1922) : $16,035.40

# get_age() - which returns how old the guitar is in years (e.g., in 2022 the L-5 is: 2022 - 1922 = 100)

# is_vintage() - which returns True if the guitar is 50 or more years old, False otherwise
# Hint: try using get_age() to simplify the implementation of this method!

class Guitar:
    """Represents a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """Return a string representation of the guitar instance."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Get the age of the guitar instance"""
        return f"In 2025 the {self.name} is {2025 - self.year} years old."

    def is_vintage(self):
        """Return True if the guitar instance is >=50 years old."""
        if (2025 - self.year) >= 50:
            return True
        else:
            return False