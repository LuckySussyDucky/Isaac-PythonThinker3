stuff = {
    "notebook": 250,
    "pen": 125,
    "pencil": 50,
    "ruler": 150,
    "eraser": 50,
    "writing pad": 250,
    "marker": 200,
    "glue": 300,
    "calculator": 3500
}

ordered = {

}

price = 0

print(" ")
print("Welcome to the Bookshop")
print("Ordering System (BOS)!")
print(" ")
print("Here is the stuff we have:")
for key, value in stuff.items():
    print(f"{key}: ${value}")

while True:
    order = str(input("What would you like to order. Type 'end' when you are done. ").lower().strip())

    if order == "end":
        break

    if order not in stuff:
        print("Sorry but we do not have that.")
        continue

    if order in stuff:
        yes_or_no = input(f"Do you want to add {order} into your cart? Yes/No ").lower().strip()
        if yes_or_no == "no":
            continue

        if yes_or_no == "yes":
            print(f"We have added {order} into your cart")         
            # check if order is in ordered, if it is not in order, the below is ok
            if order in ordered:
                ordered[order] += stuff[order]
            else:
                ordered[order] = stuff[order]
            # if it is in order, you need to add the unit price to the current price in the dictionary
            print(f"{order} cost ${stuff[order]}.")
            continue

        if yes_or_no != "yes" or "no":
            print(f"We did not add {order} into your cart. Please type a proper answer.")

print(" ")
print(" ")
print(" ")            
print("This is your total amount:")
for key, value in ordered.items():
    print(f"{key.title()}: ${value}")
for key, value in ordered.items():
    price = price + value

    if price > 2000:
        price = (price / 100) * 90
        print(f"Total: ${price}")
    else:
        print(f"Total: ${price}")

input("Please key in your credit card password here: ")
input("Please key in your credit card number here: ")
input("Please key in your home address here: ")