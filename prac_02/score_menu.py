"""
CP1404/CP5632 - Practical
Program main menu from scratch:

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit

"""

def main():
    score = None
    menu = "G) Get valid score\nP) Print result\nS) Show stars\nQ) Quit"
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score is None:
                print("No score data. Choose G to enter your score first.")
            else:
                result = determine_grade(score)
                print(result)
        elif choice == "S":
            if score is None:
                print("No score data. Choose G to enter your score first.")
            else:
                print("*" * int(score))
        else:
            print("Invalid choice")

        print(menu)
        choice = input(">>> ").upper()

    print("See you later!")

def get_valid_score():
    is_valid_score = False
    while not is_valid_score:
        try:
            score: float = float(input("Enter score: "))
            if score < 0 or score > 100:
                print("Invalid score")
            else:
                is_valid_score = True
        except ValueError:
            print("Invalid score (not a number)")
    return score

def determine_grade(score: float):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()