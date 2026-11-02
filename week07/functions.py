# Self-Assessment
#
# 1. I found the bugs by checking the error messages and testing the code.
# This helped me understand how to find and fix errors.
#
# 2. apply_discount(price, tier) takes a price and a discount tier.
# It returns the price after the discount is applied.
#
# 3. AI disclosure: I used ChatGPT to help explain the instructions.

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

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)

discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")

taxed_price = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${taxed_price:.2f}")

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


    # --- Exercise 5 ---
# Bug 1: Added the missing colon after the for loop.
# Bug 2: Changed <= to < to prevent an index error.
# Bug 3: Changed total = sale to total += sale.

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

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

# Scope means a variable inside a function is separate
# from a variable outside the function.