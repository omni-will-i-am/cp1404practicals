"""..."""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness and flagfall."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # price_per_km is scaled by fanciness value
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the silver service taxi instance that includes flagfall."""
        return f"{super().__str__()} plus a flagfall cost of ${self.flagfall:.2f}"

