# Self-Assessment
#
# 1. For an order total of $350, Python first checks if the
# total is at least $500. It is not, so it checks the $200
# tier. Since $350 is at least $200, the order gets a 10%
# discount, making the final price $315.
#
# 2. The "and" condition requires both conditions to be true.
# Two separate if statements check each condition separately,
# so they can produce different results.
#
# 3. I encounter tiered conditional systems when shopping
# online and getting discounts based on how much I spend.
# Python conditionals help me understand how these systems
# make decisions automatically.


# --- Exercise 1 ---

total = float(input("Enter cart total: $"))

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

final = total * (1 - discount)

print(f"Discount: {discount * 100:.0f}%")
print(f"Final price: ${final:.2f}")


# --- Exercise 2 ---

if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"

print(f"Status: {status}")


# --- Exercise 3 ---

region = "South"

if region == "South" and total >= 100:
    discount += 0.02
    print("Region bonus applied: additional 2% off")

final = total * (1 - discount)

print(f"Final discount: {discount * 100:.0f}%")
print(f"Final price: ${final:.2f}")


# --- Exercise 4 ---

customer_type = "wholesale"
extra_discount = 0

if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03

# The flat version is easier to read and test because
# all three conditions are checked in one line.


# --- Exercise 5 ---

for amount in [-50, 500, 15000]:
    if amount <= 0:
        print("SUSPICIOUS")
    elif amount < 10000:
        print("NORMAL")
    else:
        print("LARGE — REVIEW REQUIRED")


        # --- Exercise 6 ---

yearly_spending = 2500
orders = 8
outstanding_balance = False

if (yearly_spending > 2000 or orders > 10) and not outstanding_balance:
    print("VIP upgrade: eligible")
else:
    print("VIP upgrade: not eligible")