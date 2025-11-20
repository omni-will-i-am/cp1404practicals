"""CP1404/CP5632 Practical 09.
Taxi class test.
"""

from prac_09.taxi import Taxi

def main():
    my_taxi = Taxi("Prius 1", 100)

    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")

    my_taxi.drive(40)

    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")

    my_taxi.start_fare()
    my_taxi.drive(60)
    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()