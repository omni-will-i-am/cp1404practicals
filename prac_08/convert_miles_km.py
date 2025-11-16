"""CP1404 Practical 08. Miles to Kilometers conversion program with Kivy GUI."""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    """Convert miles to kilometres."""
    output_km = StringProperty("0.0")  # this is bound to the Label's text

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        """Handle converting miles to kilometres."""
        miles = self.get_miles()
        km = miles * MILES_TO_KM
        self.output_km = f"{km:.2f}"

    def handle_increment(self, change):
        """Increase or decrease miles value by 1."""
        miles = self.get_miles() + change
        self.root.ids.input_miles.text = str(miles)

    def get_miles(self):
        """Get the current miles value or 0.0 if the input is invalid.
        Also sets the output label to 0.0 when input is invalid."""

        text = self.root.ids.input_miles.text
        try:
            return float(text)
        except ValueError:
            # Invalid input: show 0.0 and treat as 0 internally
            self.output_km = "0.0"
            return 0.0


MilesToKmApp().run()
