"""
CP1404/CP5632 Practical 09
Taxi simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "(Q)uit, (C)hoose Taxi, (D)rive"


def main():
    """Taxi simulator program"""
    print("Time to drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]
    bill_to_date = 0.0
    current_taxi = None

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == "D":
            bill_to_date = drive_taxi(current_taxi, bill_to_date)
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").upper()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis available:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the taxis with index numbers."""
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


def choose_taxi(taxis, current_taxi):
    """Chooses a taxi and returns it; invalid choice returns previous current_taxi."""
    display_taxis(taxis)
    try:
        choice = int(input("Choose a taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid choice")
            return current_taxi
    except ValueError:
        print("Invalid choice")
        return current_taxi


def drive_taxi(current_taxi, bill_to_date):
    """Drive the current taxi and return the bill."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return bill_to_date
    try:
        distance = float(input("How far would you like to drive? "))
    except ValueError:
        print("Invalid distance")
        return bill_to_date

    current_taxi.start_fare()
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()

    print(f"Your {current_taxi.name} trip has cost you ${trip_cost:.2f}")
    return bill_to_date + trip_cost


if __name__ == "__main__":
    main()
