"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

#define the actual menu
def menu_display():
    print("Menu:")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

#input name
name = input("Hello, who are you? ").strip()

menu_display()
choice = input(">>> ").strip().upper()

while choice != "Q":
    if choice == "H":
        print(f"It's nice to finally meet you, {name}")
    elif choice == "G":
        print(f"I'll be watching, {name}")
    else:
        print(f"Invalid choice")
    menu_display()
    choice = input(">>> ").strip().upper()

print("Finished")