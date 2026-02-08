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

ordered = {

}

removeDish = " "
addDish = " "

print("Here is our menu:")
for key, value in dishes.items():
    print(f"{key}: {value}")

while True:
    dish = input("What would you like to order? Key in 1 dish and type end when you are done: ").lower().strip()
    
    if dish == "end":
        break

    # for removal of item, can consider checking here
    # need to check for the remove in the response 

    if dish not in dishes:
        print("Sorry but we do not have that.")
        continue  
            
    if dish in ordered:
        ordered[dish] += dishes[dish] 
        print(f"{dish} cost ${dishes[dish]}.")  
    else:
        ordered[dish] = dishes[dish]           
        print(f"{dish} cost ${dishes[dish]}.")
        continue        
    
print("Here is your order:")
for key, value in ordered.items():
    print(f"{key}: {value}")

while True:
    # task 3 is being done partially. need to have a while loop to repeatedly ask qns
    # the condition will be that as long as the response is not yes/y or no/n, the question will be repeat itself
    # the below will be inside the condition when the response is yes.
    removeDish = input("Would you like to remove any dishes? Type end when you are done. ").lower().strip()

    if removeDish in ordered:
        ordered[dish] -= ordered[removeDish]
        # ordered[order] += stuff[order]
    elif removeDish not in ordered and removeDish in dishes:
        print("You did not even order this dish.")
    else:
        print("This dish does not exist")
        continue     
    print(ordered)   

    if removeDish == "end":
        break

while True:
    # task 3 is being done partially. need to have a while loop to repeatedly ask qns
    # the condition will be that as long as the response is not yes/y or no/n, the question will be repeat itself
    # the below will be inside the condition when the response is yes.
    addDish = input("Would you like to add any dishes? Type end when you are done. ").lower().strip()

    if dish in ordered:
        ordered[dish] += dishes[dish] 
        print(f"{dish} cost ${dishes[dish]}.")  
    elif dish not in ordered and dish in dishes:
        ordered[dish] = dishes[dish]           
        print(f"{dish} cost ${dishes[dish]}.")   
        # ordered[order] += stuff[order]
    else:
        print("This dish does not exist")
        continue     
    print(ordered)   

    if addDish == "end":
        break

print(" ")
print(" ")
print(" ")            
print("This is your total amount:")
for key, value in ordered.items():
    print(f"{key.title()}: ${value}")
for key, value in ordered.items():
    price = price + value   
# suggestions: reconsider the method to do the remaining task 3,4, challenge 1 and 2
# there is no need to do another while loop, can do in the above while loop