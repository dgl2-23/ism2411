# Self-Assessment
#
# 1. The accumulator pattern starts with a variable, goes
# through each item in a loop, and updates the variable.
#
# 2. The while loop was longer than the for loop. The for loop
# is easier to read and simpler to use with a list.
#
# 3. I could use a loop with sales data in my major. I could
# add the sales together and print the total and average.


# --- Exercise 1 ---

sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0

for sale in sales:
    total += sale

print(f"Total: ${total}")

# --- Exercise 2 ---

total = 0
count = 0

for sale in sales:
    total += sale
    count += 1

average = total / count

print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

# --- Exercise 3 ---

current_max = 0

for sale in sales:
    if sale > current_max:
        current_max = sale

print(f"Largest sale: ${current_max}")

# --- Exercise 4 ---

over_100_count = 0
over_100_total = 0

for sale in sales:
    if sale > 100:
        over_100_count += 1
        over_100_total += sale

print(f"Sales over $100: {over_100_count}")
print(f"Total of those sales: ${over_100_total}")

# --- Exercise 5 ---

for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found — ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")

    # --- Exercise 6 ---

total = 0
i = 0

while i < len(sales):
    total += sales[i]
    i += 1

print(f"While loop total: ${total}")

# I would use the for loop in production because it is shorter and easier to read.

# --- Exercise 7 ---

for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0

    discounted_price = sale * (1 - discount)

    print(f"${sale} → {discount * 100:.0f}% discount → ${discounted_price:.2f}")