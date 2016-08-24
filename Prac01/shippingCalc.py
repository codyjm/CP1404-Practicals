"""
shipping calculator
"""
total = 0
num_items = int(input("Number of items: "))

while num_items < 0:
    print("Invalid number of items")
    num_items = int(input("Number of items: "))

for i in range(1, num_items + 1, 1):
    total += float(input("Price of item: "))

if total > 100:
    print("Total price for", num_items, "items is ${:.2f}".format(total - (total * 0.1)))
else:
    print("Total price for", num_items, "items is ${:.2f}".format(total))
