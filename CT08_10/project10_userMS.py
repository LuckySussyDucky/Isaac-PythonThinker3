import random
# # Lesson 10- User Management System

# ## Task 1: Generate a strong password

# ### Generate a strong password that meets security guidelines.

# - **Function name**: `generate_password()`
# - **Params**: length (int) – desired password length
# - **return**: password (string) - randomly generated password string.

# ### Notes
# *Use the ASCII table and what you have learned earlier to generate a random and strong password*:
# - *12 characters*
# - *Uppercase*
# - *Lowercase*
# - *numbers*
# - *special characters*

def generate_password(length):
    password = ""
    for i in range(length):
        option = random.randint(1, 3)
        if option == 1:
            password += chr(random.randint(33, 57))
        elif option == 2:
            password += chr(random.randint(65, 90))
        elif option == 3:
            password += chr(random.randint(97, 122))
    return(password)

generate_password(12)   


# ## Task2: Create a new user

# ### creates a new username and assigns a strong password using the `generate_password()` function.

# - **Function name**: `create_new_user()`
# - **Params**: user_db (dictionary) – A dictionary to store usernames and passwords.
# - **return**: user_db (dictionary) – Updated dictionary
#   - Prints the username and password

# ### Notes
# *Use the earlier password generation program to generate a strong password for the user.*

user_db = {}

def create_new_user(user_db):
    username = input("Enter a username: ")
    while True:
        if len(username) < 8:
            username = input("Username must be at least 8 characters: ")
        else:
            break
    while True:
        if username in user_db:
            username = input("Username already taken please choose another one: ")
        else:
            break
    password = generate_password(12)
    print(f"Username created: {username}")
    print(f"Password generated: {password}")
    
    user_db.setdefault(username, []).append(password)

    print(user_db.values())
    return(user_db)

# ## Task 3: Update password
# Allows an existing user to reset their password by verifying their current password first.

# - **Function name**: `update_password()`
# - **Params**: user_db (dictionary) – A dictionary to store usernames and passwords.
# - **return**: user_db (dictionary) – Updated dictionary
#   - Prints the username and password
# ### Notes
# *Checks for username existence in user_db.*

# *Verifies the user’s current password before allowing updates.*

# *Generates a new strong password using generate_password.*

def update_password(user_db):
    username = input("Enter Your username: ")
    Cpassword = input("Enter your current password: ")
    if username in user_db:
        print(f"Changed password to {password} for {username}.")
        password = generate_password(12)
        user_db[username] = password
    else:
        print("Could not find account.")
    return(user_db)


# ## Task 4: Login

# ## Allows users to log in by verifying their username and password.

# - **Function name**: `login()`

# - **Params**: user_db (dictionary) – A dictionary to store usernames and passwords.

# - **returns**: auth_status(boolean) – True or False indicating success or failure.

# ### Notes
# *Ensures the username exists in user_db.*

# *Matches the entered password with the stored password for validation.*

def login(user_db):
    attempts = 0
    if attempts < 4:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in user_db and user_db[username] == password:
            print("Successfully login!")
            return True
        else:
            print("The username or password is incorrect.")
            attempts += 1 
    else:
        print("Too many tries. ")


# ## Task 5: View Username and passwords
# ### Displays all stored usernames and their masked passwords (e.g., ********)

# - **Function name**: `view_user_data()`

# - **Params**: user_db (dictionary) – A dictionary to store usernames and passwords.

# - **returns**: none
#   - Prints a list of username and passwords

# ### Notes
# *Strictly speaking, this function should not exist in any system, as it could lead to abuse of a user’s private data.*

# *But for verifying whether your program works, we have put this in.*

# *Challenge: Mask part of the password. i.e. put (*) instead of the real password.*

def view_user_data(user_db):
    for key, value in user_db.items():
        print(f"Username: {key}")
        print(f"Password: {value}")

# ## Task 6: Build a menu system

# ### Build a menu that allows you to access all the functions in the system.

# - **Function name**: view_menu()

# - **Params**: none

# - **returns**: none

# ### Notes
# *The following menu options should be available to you.*

# *Your menu should validate the available options inputted by the user.*

while True:
    print("""
Menu
1. Create new user
2. Update password
3. Login
4. View username and passwords
5. Exit program

    """)
    choice = input("What would you like to do (1, 2, 3, 4, 5): ")

    if choice == "1":
        create_new_user(user_db)
    elif choice == "2":
        update_password(user_db)
    elif choice == "3":
        login(user_db)
    elif choice == "4":
        view_user_data(user_db)
    elif choice == "5":
        break