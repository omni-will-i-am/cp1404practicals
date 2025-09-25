"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()


star_gen = int(input("Enter a number: "))
mode = input("Horizontal or Vertical alignment? (H/V): ").strip().lower()   #forgiving input

if mode.startswith('h'):
    print("*" * star_gen)   #horizontal
elif mode.startswith('v'):
    for _ in range(star_gen):   #vertical
        print("*")
else:
    print("Invalid choice. Goodbye.")
"""

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print("*" * i)