"""CP1404/CP5632 Practical 09.
Unreliable car class test.
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    unreliable_car = UnreliableCar("Holden Commodore", 100, 30) # 30% reliability
    reliable_car = UnreliableCar("AU Ford Falcon", 100, 80) # 80% reliability

    test_drives = 10
    drive_distance = 10

    reliable_successes = 0
    unreliable_successes = 0

    for _ in range(test_drives):
        if reliable_car.drive(drive_distance) > 0:
            reliable_successes += 1
        if unreliable_car.drive(drive_distance) > 0:
            unreliable_successes += 1

    print(f"{reliable_car.name} drove {reliable_successes} times out of {test_drives} attempts.")
    print(f"{unreliable_car.name} drove {unreliable_successes} times out of {test_drives} attempts.")


if __name__ == "__main__":
    main()