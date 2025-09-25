"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_RATE_LOW = 0.10
BONUS_RATE_HIGH = 0.15
THRESHOLD = 1000

sales = float(input("Enter sales made: $"))

while sales >= 0:
    if sales >= THRESHOLD:
        bonus = sales * BONUS_RATE_HIGH
    else:
        bonus = sales * BONUS_RATE_LOW

    print(f"Estimated bonus: ${bonus}")
    sales = float(input("Enter sales made (or negative number to quit): $"))

print("Done calculating sales bonus, proceed to next thing...")