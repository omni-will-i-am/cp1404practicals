"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator

Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def get_valid_input():
    while True:
        try:
            user_input = int(input("Enter number of quick picks: "))
            if user_input > 0:
                return user_input
            print("Enter a positive whole number.")
        except ValueError:
            print("Invalid input. Enter a positive whole number.")

def generate_quick_picks():
    picks: list[int] = []
    while len(picks) < NUMBERS_PER_LINE:
        random_pick = random.randint(MIN_NUMBER, MAX_NUMBER)
        if random_pick not in picks:
            picks.append(random_pick)
    picks.sort()
    return picks

def format_quick_picks(pick: list[int]):
    return " ".join(f"{n:2}" for n in pick)

def main():
    pick_count = get_valid_input()
    for i in range(pick_count):
        pick = generate_quick_picks()
        print(format_quick_picks(pick))

if __name__ == "__main__":
    main()