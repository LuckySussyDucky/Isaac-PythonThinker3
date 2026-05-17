# # Lesson 14 - Car Showroom

# ## Learning Exercise 1 - 4

# ```python
# # Step 1: Define the ZooAnimal class

#         # Initialize the animal's name and species

#         # A method to make the animal "speak"
        
#         # A method to describe the animal

class ZooAnimals:
    def __init__ (self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def description(self):
        if self.name == "Ruff":
            print(f"{self.name} is a {self.species} and has a brother called Puff")
        elif self.name == "Puff":
            print(f"{self.name} is a {self.species} and has a brother called Ruff")
        else:
            print(f"{self.name} is a {self.species} and makes the sound {self.sound}")

Wolf = ZooAnimals("Ruff", "wolf", "woof")
Wolf.description()

Wolf = ZooAnimals("Puff", "wolf", "woof")
Wolf.description()

Duck = ZooAnimals("Cluckers 🐣", "duck", "quack")
Duck.description()

# # Step 2: Create objects (instances) of ZooAnimal

# # Create a few zoo animals

# # Call methods on the objects
# ```

print(" ")

# ## Car Showroom Task 1: Create Car Class

# Create 3 cars from this class
# 1. BMW, Z4, 500000
# 2. Toyota, Corolla, 180000
# 3. Kia, Cerato, 165000

class Cars:
    def __init__ (self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def description(self):
        print(f"{self.brand} has a car model, {self.model}, which is priced at ${self.price}")

    def start_engine(self):
        print(f"The {self.brand} {self.model} is starting it engine. Vroom vroom")

BMW = Cars("BMW", "Z4", "500000")
BMW.description()

Toyota = Cars("Toyota", "Corolla", "180000")
Toyota.description()

Kia = Cars("Kia", "Cerato", "165000")
Kia.description()

print(" ")

# ## Car Showroom Task 2: Add a method!
# - Print out the method in the class.
# - Try adding other methods like “start_engine()” to your class.

BMW.start_engine()
Toyota.start_engine()
Kia.start_engine()

print(" ")

# ## Car Showroom Task 3: Show all cars in the showroom
# - Create a list called showroom.
# - Add car objects to the list using .append().
# - Use a for loop to go through the list and call show_details for each car.

showroom = [

]

showroom.append(Cars("BMW", "Z4", "500000"))
showroom.append(Cars("Toyota", "Corolla", "180000"))
showroom.append(Cars("Kia", "Cerato", "165000"))

for car in showroom:
    print(f"{car.brand} has a car model, {car.model}, which is priced at ${car.price}")


## chiken nuggets 🐣