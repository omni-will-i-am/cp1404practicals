"""CP1404 Practical 08, Dynamic Labels Exercise.
This is a very simple app that has a list of names (strings) and dynamically creates a separate Label for each one."""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Simple app that displays a list of names using dynamic Labels."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # dictionary is defined in the init function (this is the data, or model)
        self.names = ["William", "Alice", "Bob", "Charlie"]

    def build(self):
        """Build the GUI from the kv file and create labels dynamically."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")

        # the widgets (Buttons in the demo, but yours will be Labels) are made with a loop in the build function
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)  # add to the child layout with an id, not to root itself

        return self.root


DynamicLabelsApp().run()
