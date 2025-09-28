"""
CP1404/CP5632 - Practical
Program to determine score status
"""

def score_parameter(score: float):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    result = score_parameter(score)
    print(result)

if __name__ == "__main__":
    main()
