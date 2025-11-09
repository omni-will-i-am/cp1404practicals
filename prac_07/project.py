

class Project:
    """Represent a project object with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost, completion_percentage):
        """Construct a project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority: {self.priority}, estimated cost: ${self.cost:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Sort projects ascending by priority."""
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage >= 100