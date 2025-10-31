"""
CP1404/CP5632 Practical - Client code to use the Guitar class.
This program should use a list to store all the user's guitars (keep inputting until they enter a blank name), then print their details.

Time start: 1845
Time Finish: 1938

Estimated time: 60 min
Actual time: 53 min
"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars: list[Guitar] = []

    get_guitar_input(guitars)

    print_guitar_details(guitars)


def print_guitar_details(guitars):
    print("These are my guitars: ")
    name_width = max(len(guitar.name) for guitar in guitars) if guitars else 0
    for i, guitar in enumerate(guitars, start=1):
        vintage_tag = f" {guitar.is_vintage()}" if guitar.is_vintage() else ""
        print(f"Guitar {i}. {guitar.name:>{name_width}} ({guitar.year}), worth ${guitar.cost:2,.2f}{vintage_tag}")


def get_guitar_input(guitars):
    while True:
        name = input("Guitar model: ").strip()
        if not name:
            break
        year = int(input("Year of manufacture: ").strip())
        cost = float(input("Cost: $").strip())

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added. \n")


if __name__ == '__main__':
    main()
