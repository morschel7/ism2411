
# ISM2411 - Lab 10
# Inventory List Manager

# Reflection 1:
# TODO: Write 2-3 sentences about what surprised you about lists.

# Reflection 2:
# TODO: Write 2-3 sentences about a real business use of lists.


# Exercise 1 - Build the list

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))


# Exercise 2 - Index Practice

print("First item:", inventory[0])
print("Last item:", inventory[-1])
print("Middle item:", inventory[len(inventory) // 2])


# Exercise 3 - Slicing

print("First three:", inventory[:3])
print("Last two:", inventory[-2:])
print("Every other:", inventory[::2])


# Exercise 4 - Modify Inventory

inventory.append("envelope")
print("After append:", inventory)

inventory.remove("tape")
print("After remove:", inventory)

inventory.sort()
print("After sort:", inventory)


# Exercise 5 - Tuple Comparison

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Cannot change a tuple because it is immutable.")
    print("Tuples are useful for keeping coordinates fixed.")

print("Original coordinates:", coords)



# Exercise 6 - Average of a List of Sales

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7 - Accumulator Pattern

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original prices:", prices)
print("Discounted prices:", discounted)


# Exercise 8 - Filter Above Threshold

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average high sales:", round(sum(high_sales) / len(high_sales), 2))
