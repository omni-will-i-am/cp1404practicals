DISCOUNT_RATE = 0.10

#define valid price input
def valid_money(s: str) -> bool:
    s = s.strip()
    if s.count(".") > 1:
        return False
    if s.startswith("-"):
        return False
    if "." in s:
        dollars, cents = s.split(".", 1)
        return dollars.isdigit() and cents.isdigit() and len(cents) <= 2
    return s.isdigit()

#request input for n of items
while True:
    try:
        num_items = int(input("Number of items: "))
        if num_items <= 0:
            print("Invalid number of items!")
            continue
        break
    except ValueError:
        print("Invalid number of items!")

#define total and request input price of each item
total = 0.0
for _ in range(num_items):
    price_str = input("Price of item: ").strip()
    if not valid_money(price_str):
        print("Invalid price!")
        raise SystemExit
    price = float(price_str)
    total += price

#apply discount if required
if total > 100:
    total -= total * DISCOUNT_RATE

print(f"Total price for {num_items} items is ${total:.2f}")

#doesnt code for quantity of items, could be refined to do so.
#i.e. item 1 -> price -> qty -> running total -> next item