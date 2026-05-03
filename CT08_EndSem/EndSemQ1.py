"""
============================================================
Q1. Customer VIP Classification
============================================================
You are working with a dictionary of customer spending.
The program must classify customers into VIP and non-VIP groups.

Program Requirements:
- Use the dictionary:
  customer_spending = {
      "Alice": 950, "Bob": 1200, "Charlie": 500, 
      "Diana": 1800, "Ethan": 2200, "Fiona": 700, 
      "John": 685, "Hor Kee": 1389, "Siew Ling": 235, 
      "Matt": 452, "Kristen": 985, "Johnson": 785, 
      "Charles": 2352, "Tommy": 741, "Laura": 689 }

- Create two dictionaries:
  vip → spending > 1000
  non_vip → spending ≤ 1000

- Loop through the dictionary and classify customers

Print the result in this format for each customer:
    Hi Bob, you are now a VIP! Congratulations!
    Hi Charlie, spend $500 more to become a VIP member!

Note:
- These are example lines only
- Your program should print a message for every customer

============================================================
"""

# ============================================================
# Step 1: Create dictionaries
# ============================================================

customer_spending = {
    "Alice": 950, 
    "Bob": 1200, 
    "Charlie": 500, 
    "Diana": 1800, 
    "Ethan": 2200, 
    "Fiona": 700, 
    "John": 685, 
    "Hor Kee": 1389, 
    "Siew Ling": 235, 
    "Matt": 452, 
    "Kristen": 985, 
    "Johnson": 785, 
    "Charles": 2352, 
    "Tommy": 741, 
    "Laura": 689
    }

# ============================================================
# Step 2: Loop through customer_spending
# ============================================================

for item, value in customer_spending.items():

# ============================================================
# Step 3: Group customers into vip / non_vip
# ============================================================

    if value < 1000:

        # ============================================================
        # Step 4: Print customer messages
        # ============================================================

        print(f"Hi {item}, spend ${1000 - value} more to become a VIP member!")
    else:

        # ============================================================
        # Step 4: Print customer messages
        # ============================================================
        
        print(f"Hi {item}, you are now a VIP! Congratulations!")



