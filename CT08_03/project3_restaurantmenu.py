# # Lesson 3 - Restaurant Menu

# ## Task 1: Display the Menu
# **Display the Menu**

# Write a program that:​
# - Creates a dictionary with at least 5 menu items and their prices.​
# - Prints all the items in the menu with their prices, one item per line.

# ## Task 2: Check if item exists
# **Take the Customer’s Order and Check if it Exists**

# Asks the customer for the item they want to order.​

# Checks if the item exists in the menu.​
# - If it exists: Print the item and its price.​
# - If it does not exist: Display a message saying the item is unavailable.​

# Keep asking again and again until customer says “no more”

# ## Task 3: Add ordered item to another Dictionary
# **Add the Ordered Item to Another Dictionary**

# Extend your program so that it:​
# - If the item exists, asks the customer if they want to add it to their order.​
# If the customer says "yes," ​
# add the item and its price to a separate dictionary that stores the customer’s order.​
# If the customer says "no," ​
# display a message confirming the item was not added.

# ## Task 4: Display Order Summary and Total Cost
# **Display the Order Summary and Total Cost**

# After the customer finishes ordering:​
# - Display all the items in their order with the prices.​
# - Calculate and display the total cost of the order.

# ## Challenge 1: Wallet Feature
# Assign a wallet balance to the customer (e.g., $10).​

# Before confirming an order, check if the total cost will exceed the customer’s wallet balance.​
# - If the total exceeds the wallet balance, display a message and do not add the item.​
# - If the total is within the wallet balance, confirm the order as usual and reduce the balance

# Task 1

dishes = {
    "rice": 1.00,
    "beef": 2.00,
    "pork": 1.50,
    "fish": 1.75,
    "water": 100.00
}

order = {

}

dish = ""
end = False
price = 0

remove = ""
removeCount = False

add = ""
addCount = False

print("Here is our menu:")
for key, value in dishes.items():
    print(f"{key}: {value}")

dish = input("What would you like to order? Key in 1 dish and type end when you are done: ").lower().strip()

# while True:
#     dish = input("What would you like to order? Key in 1 dish and type end when you are done: ").lower().strip()

#     if dish == "end":
#         break
    
#     if dish in dishes:
#         while True:


while True:
    if dish in dishes:
        for key, value in dishes.items():
            price = price + value 
        print(price)          
        print(dish)
dish = input("Would you like anything else? ").lower().strip()
if dish == "end":
    end = True
else:
    print("We do not have that sadly")

while removeCount == False and addCount == False and end == False:
    if dish == "end":
        remove = input("Would you like to remove anything? Yes or No. ").lower().strip()
        if remove == "yes":
            removeCount = False
        elif remove == "no":
            removeCount = True
            while addCount == False:
                add = input("Would you like to add anything? Yes or No. ").lower().strip()
                if add == "yes":
                    addCount = False
                elif add == "no":
                    addCount = True
                else:
                    removeCount = False
        else:
            removeCount = False
    else:
        dish = input("Would you like anything else? ").lower().strip()
        for key, value in dishes.items():
            price = price + value 
            print(price)   
print("Your total bill is " + str(price))