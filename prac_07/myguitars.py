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
    display_guitars(guitars) # display unsorted list of guitar objects
    guitars.sort()
    display_guitars(guitars) # display sorted list of guitar objects


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


main()