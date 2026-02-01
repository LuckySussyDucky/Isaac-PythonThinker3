# Exercise 1

students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 70
}

print(f"Students Grades: {students}")

students["David"] = 55
students["Ella"] = 75
students["John"] = 60 
  
print(f"New Grades: {students}")

    # Try using an input() to ask which student you want to check the score for?
    # What happens if you try accessing a student that does not exist?

name = input("Which students would you like to find the score for? ")
if name in students:   
    print(students[name])
else:
    print(name + "dosen't exist")

for key, value in students.items():
    print(f"{key}: {value}")

for student in students:
    print(student)