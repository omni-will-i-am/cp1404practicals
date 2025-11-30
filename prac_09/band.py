"""
CP1404/CP5632 Practical: Band class
"""

class Band:
    """Band (parent) object that has Musicians (children)"""

    def __init__(self, name):
        """Initialise a Band object with a name and an empty list of Musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band"""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band and its cohort of musicians"""
        band_members = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({band_members})"

    def play(self):
        """Return a string of the band playing, with each musician playing on its own line."""
        return "\n".join(musician.play() for musician in self.musicians)