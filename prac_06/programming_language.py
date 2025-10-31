"""
CP1404/CP5632 Practical - Programming Language exercise.

Time start: 1600
Time Finish: 1628

Estimated time: 30 min
Actual time: 28 min
"""


class ProgrammingLanguage:
    """Represents a programming language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamic."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the programming languages."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
