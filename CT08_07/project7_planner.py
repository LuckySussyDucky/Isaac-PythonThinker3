import os

filepath = os.getcwd()
fullpath = os.path.join(filepath, "CT08_07/planner.txt")

# ## Task 1: Display a Menu
# **Create a menu-driven system that lets the user choose actions for the task list program.​**

# Start the program by displaying a menu with the following options:​
# - Create a new task file ​
# - View all tasks.​
# - Add a new task.​
# - Delete a task.​
# - Mark a task as done.​
# - Exit the program.​

# Prompt the user to input their choice by entering the corresponding number.

while True:

    print("""
    What would you like to do?
      
    1: Create a new task file
    2: View all tasks.
    3: Add a new task.
    4: Mark a task as done.
    5: Unmark completed task.
    6: Delete a task.
    7: Exit the program.
    """)

    choice = input("What would you like to do? ")
    
# ## Task 2: Create a new task file
# **Initialize a new file for tasks and write a title to the file.​**


# Check if tasks.txt already exists:​
# - If the file exists, notify the user and ask if they want to overwrite it.​
# - If the file doesn’t exist, create the file and write "My Task List" as the title.​
# Confirm the creation of the file.

    if choice == "1":
        if os.path.exists(fullpath):
            overwrite = input("File already exists. Overwrite? (y/n): ")
            if overwrite.lower() == "y":
                with open(fullpath, "w") as file:
                    file.write("My Task List\n")
                print("Task file created.")
            elif overwrite.lower() == "n":
                print("File not overwritten.")
            else:
                print("You did not answer properly. File not overwritten.")
        else:
            with open(fullpath, "w") as file:
                file.write("My Task List\n")
            print("Task file created.")


# ## Task 3: View all tasks
# **Display all tasks from the file.​**

# Open tasks.txt and read its contents.​
# - Display tasks with numbering.​
# - If no tasks are found (i.e., only the title exists), display "No tasks found!".
    
    elif choice == "2":
        with open(fullpath, "r") as file:
            tasks = file.readlines()

        if len(tasks) <= 1:
            print("No tasks found!")
        else:
            num = 0
            for i in range(1, len(tasks), 1):
                if "[HIGH]" in tasks[num]:
                    tasks[num] == tasks[num]
                elif "[MEDUIM]" in tasks[num]:
                    tasks[num] == tasks[num]
                elif "[LOW]" in tasks[num]:
                    tasks[num], tasks[num + 1] = tasks[num + 1], tasks[num]
                num += 1
            for i, task in enumerate(tasks[1:], start = 1):
                print(f"{i}. {task.strip()}")


# ## Task 4: Add a new task
# **Append new tasks to the file​**

# Prompt the user to input a new task.​
# - Append the task to tasks.txt without overwriting the existing tasks.​
# - Confirm the task has been added.

    elif choice == "3":
        new_task = input("Enter the new task: ")

        piority = input("How important is this task? (high/meduim/low): ").strip().lower()

        if piority == "high":
            with open(fullpath, "a") as file:
                file.write(new_task + " [HIGH]" + "\n")
                print("Task added.")

        elif piority == "meduim":
            with open(fullpath, "a") as file:
                file.write(new_task + " [MEDUIM]" + "\n")
                print("Task added.")

        elif piority == "low":
            with open(fullpath, "a") as file:
                file.write(new_task + " [LOW]" + "\n")
                print("Task added.")

        else:
            print("Please key in the piority properly.")
            print("Task has not been added.")

            ## Autoset to low piority
            # with open(fullpath, "a") as file:
            #     file.write(new_task + " [LOW]" + "\n")
            #     print("Task added.")



# ## Task 5: Mark a Task as “done”
# **Update a task to indicate completion.​**

# Display all tasks with numbers.​
# - Prompt the user to input the number of the task to mark as done.​
# - Update the task in the file to show it is completed (e.g., "Go for a run (Done)").​
# - Save the updated tasks back to the file.

    elif choice == "4":
        with open(fullpath, "r") as file:
            tasks = file.readlines()

        for i, task in enumerate(tasks[1:], start=1):
            print(f"{i}. {task.strip()}")

        num = int(input("Enter the task number to mark as done: "))

        if "(Done)" in tasks[num]:
            print("You already marked this done.")
        else:
            tasks[num] = tasks[num].strip() + " (Done)\n"

            with open(fullpath, "w") as file:
                file.writelines(tasks)

            print("Task marked as done.")

    elif choice == "5":
        with open(fullpath, "r") as file:
            tasks = file.readlines()

        for i, task in enumerate(tasks[1:], start=1):
            print(f"{i}. {task.strip()}")

        num = int(input("Enter the task number to unmark as done: "))

        if "(Done)" in tasks[num]:
            tasks[num] = tasks[num].replace("(Done)", "")
            print(tasks)

            with open(fullpath, "w") as file:
                file.writelines(tasks)

            print("Task undone.")
        else:
            print("This task was not marked as done")

# ## Task 6: Delete a Task
# **Remove a task from the file.​**

# Display all tasks with numbers.​
# - Prompt the user to input the number of the task to delete.​
# - Remove the selected task from the file.​
# - Save the updated tasks back to tasks.txt.

    elif choice == "6":
        with open(fullpath, "r") as file:
            tasks = file.readlines()

        if len(tasks) <= 1:
            print("No tasks found!")
        else:
            for i, task in enumerate(tasks[1:], start=1):
                print(f"{i}. {task.strip()}")

            num = int(input("Enter the task number to delete: "))

            tasks.pop(num)
            with open(fullpath, "w") as file:
                file.writelines(tasks)

            print("Task deleted.")

    elif choice == "7":
         print("Exiting program...")
         break
    
    else:
        print("Key in the options properly")
        continue