"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        break
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")

# 1. When will a ValueError occur?
#  When a non-integer is entered by the user (e.g., a letter)
# 2. When will a ZeroDivisionError occur?
# When the user enters 0 for the denominator
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Wrapped in a loop and retry on exceptions; break loop if correct values are entered.