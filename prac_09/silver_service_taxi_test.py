"""
CP1404/CP5632 Practical
SilverServiceTaxi test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxi_one = SilverServiceTaxi("Hummer", 100, 2)


    taxi_one.start_fare()
    print(taxi_one)

    taxi_one.drive(18)

    taxi_one.get_fare()

    # expected_fare = 48.78
    # assert taxi_one.get_fare() == expected_fare

    print(taxi_one)
    print(f"\nFare for {taxi_one.current_fare_distance} kilometers travel in {taxi_one.name} is ${taxi_one.get_fare():.2f}")

if __name__ == "__main__":
    main()