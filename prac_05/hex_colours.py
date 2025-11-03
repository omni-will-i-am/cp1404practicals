"""
CP1404/CP5632 Practical
Program that allows user to look up hexadecimal colours.

Use a constant dictionary of about 10 colour names and write a program that allows a user to enter a name and get the code,
e.g., entering AliceBlue (or aliceblue - make it case-independent) should show #f0f8ff.

Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.

"""

COLOUR_CODES = {
    "aqua": "#00ffff",
    "baby blue": "#89cff0",
    "baby pink": "#f4c2c2",
    "cadmium red": "#e30022",
    "celeste": "#b2ffff",
    "electric purple": "#bf00ff",
    "frostbite": "#e936a7",
    "golden yellow": "#ffdf00",
    "green lizard": "#a7f432",
    "laser lemon": "#ffff66",
}


def main():
    colour_name = input("Enter colour name (blank to quit): ").strip()
    while colour_name != "":
        key = colour_name.strip().lower()
        try:
            colour_code = COLOUR_CODES[key]
            print(f"{colour_name.title()} is {colour_code}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name (blank to quit): ").strip()
    print("Farewell!")


if __name__ == "__main__":
    main()
