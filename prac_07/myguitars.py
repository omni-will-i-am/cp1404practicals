"""
CP1404/CP5632 Practical
A program that reads guitars from a csv and stores them in a list of Guitar objects, using a Guitar class.
"""

import csv
from prac_07.guitar import Guitar


def main():
    guitars = []
    filename = "guitars.csv"
    load_guitars(filename, guitars)
    display_guitars(guitars)  # display unsorted list of guitar objects
    guitars.sort()
    display_guitars(guitars)  # display sorted list of guitar objects

    add_new_guitar(guitars)
    guitars.sort()
    save_guitars(filename, guitars)
    print(f"Saved {len(guitars)} guitars to {filename}")


def display_guitars(guitars):
    print("My guitars:")
    for i, guitar in enumerate(guitars, start=1):
        print(f"{i}. {guitar}")


def load_guitars(filename, guitars):
    in_file = open(filename, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        # print(parts) # debugging
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()


def add_new_guitar(guitars):
    """Prompt the user to add a new guitar. Blank name to finish."""
    print("Add a new guitar:")
    name = input("Guitar name: ").strip()
    while name != "":
        try:
            year = int(input("Year of manufacture: "))
            cost = float(input("Guitar value: $").replace(",", ""))
        except ValueError:
            print("Invalid input. Try again.")
            continue
        guitars.append(Guitar(name, year, cost))
        print(f"Added new guitar: {name} ({year}) valued at ${cost:,.2f}")
        name = input("Guitar name: ").strip()


def save_guitars(filename, guitars):
    """Save guitars to a csv file using csv module."""
    with open(filename, 'w', encoding="utf-8", newline="") as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, f"{guitar.cost:.2f}"])


if __name__ == "__main__":
    main()
