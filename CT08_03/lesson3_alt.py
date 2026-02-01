menu = {
    "rice": 1.00,
    "beef": 2.00,
    "pork": 1.50,
    "fish": 1.75,
    "water": 100.00
}

ordered = {

}

print("Here is our menu:")
for key, value in menu.items():
    print(f"{key}: {value}")

while True:
    order = input("What would you like to order. Type 'end' when you are done. ").lower.strip

    if order not in menu:
        print("Sorry but we do not have that.")
        continue
    
    if order in menu:
        ordered[order]