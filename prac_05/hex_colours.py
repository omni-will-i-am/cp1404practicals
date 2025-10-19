"""
CP1404/CP5632 Practical
Program that allows user to look up hexadecimal colours.

Use a constant dictionary of about 10 colour names and write a program that allows a user to enter a name and get the code,
e.g., entering AliceBlue (or aliceblue - make it case-independent) should show #f0f8ff.

Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.

"""

COLOUR_CODES = {
    "Aqua": "#00ffff",
    "Baby Blue": "#89cff0",
    "Baby Pink": "#f4c2c2",
    "Cadmium Red": "#e30022",
    "Celeste": "#b2ffff",
    "Electric Purple": "#bf00ff",
    "Frostbite": "#e936a7",
    "Golden Yellow": "#ffdf00",
    "Green Lizard": "#a7f432",
    "Laser Lemon": "#ffff66",
}