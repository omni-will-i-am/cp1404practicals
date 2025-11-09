"""
CP1404/CP5632 Practical - Guitar Class exercise.

"""


class Guitar:
    """Represents a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar instance."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Order guitars by year: oldest to newest."""
        return self.year < other.year
