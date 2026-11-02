# Lucas Morschel
# ISM 2411 - Introduction to Python for Business
# Module 07 Lab - Functions + Debug First, Then Ask

# --- Self-Assessment ---

# Question 1:
#The first mistake I found was a missing colon in the for loop.
# I figured it out by looking at the error in the terminal.
# It helped me realize that I should read the error messages
# carefully because sometimes the problem is pretty simple.

# Question 2:
#The apply_discount function takes a price and a membership tier.
# Depending on the tier, it gives a different discount.
# It then returns the final price after taking off the discount.
# Someone else could use it without needing to look at the code.

# Question 3:
# AI use: I used Claude to help explain errors,
# understand the exercises, and review my code.

# --- Exercise 1 ---

def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")

# --- Exercise 3 ---

discounted_price = apply_discount(200, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

tax = calculate_tax(discounted_price, 0.07)
total = discounted_price + tax
print(f"After tax: ${total:.2f}")

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---

# Bug 1: The for loop was missing a colon.
# Bug 2: The while loop went past the last valid list index.
# Bug 3: The total was being replaced instead of added together.

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---

x = 100   # Global variable

def double_it():
    x = 999   # Local variable
    return x * 2

print(x)
print(double_it())
print(x)

# Scope explanation:
# The x outside the function is 100.
# Inside the function, x is set to 999.
# The function doubles 999, but the original x stays 100.