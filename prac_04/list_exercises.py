"""
CP1404/CP5632 Practical
Basic list operations + Woefully inadequate security checker

Ask the user for their username. If the username is in the above list of authorised users, print "Access granted", otherwise print "Access denied".

Prompt the user for 5 numbers and then store each of these in a list called "numbers".
The program should then output information about these numbers.
"""

def main():
    # User security authorisation
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = input("Please enter username: ").strip()
    if username not in usernames:
        print("Access denied.")
        return
    print("Access granted.")

    # Number collection I/O
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)

    # Report number collection
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

if __name__ == "__main__":
    main()