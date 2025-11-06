"""
CP1404/CP5632 Practical - Guitar Class exercise.

Time start: 1630
Time Finish: 1708

Estimated time: 45 min
Actual time: 38 min
"""


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
        return f"In 2025 the {self.name} is {2025 - self.year} years old." # should only return the age, not a string

    def is_vintage(self):
        """Return True if the guitar instance is >=50 years old."""
        if (2025 - self.year) >= 50:
            return f"(Vintage)" # should return a boolean, not a string
        else:
            return f""
