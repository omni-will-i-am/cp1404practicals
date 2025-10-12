"""
CP1404/CP5632 Practical
Basic list operations

Prompt the user for 5 numbers and then store each of these in a list called "numbers".
The program should then output information about these numbers.
"""

def main():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

if __name__ == "__main__":
    main()