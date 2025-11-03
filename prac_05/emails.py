"""
CP1404/CP5632 Practical 05
User email:name storage/name guess program

Write a program that stores users' emails (unique keys) and names (values) in a dictionary, extracts the users name and print it as a guess.

Estimate: 30 minutes
Actual: 41 minutes
"""


def main():
    email_to_name = {}

    email = input("Enter email: ").strip()
    while email != "":
        guess_name = extract_name_from_email(email)
        user_response = input(f"Is your name \"{guess_name}\"? (Y/n): ").strip().lower()

        if user_response in ("", "y", "yes"):
            name = guess_name
        else:
            name = input("My humble apologies. Please enter your name: ").strip()

        email_to_name[email] = name
        email = input("Enter email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name_from_email(email: str):
    local_part = email.split("@", 1)[0]
    pieces = local_part.replace(".", " ").replace("_", " ").replace("-", " ").split()
    if pieces:
        guess = " ".join(pieces).title()
        return guess
    else:
        return ""


if __name__ == '__main__':
    main()
