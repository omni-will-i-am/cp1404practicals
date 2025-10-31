"""
CP1404/CP5632 Practical - Client code to test the Guitar class.
"""

from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", "1922", "16035.40")

    print(gibson)
    print(gibson.get_age())
    print(gibson.is_vintage())
    # if gibson.is_vintage() is True:
    #     print(f"{gibson.name} is vintage.")
    # else:
    #     print(f"{gibson.name} is not vintage.")


if __name__ == '__main__':
    main()
