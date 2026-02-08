# Lesson 5 - School Attendance System (SAS)

## Task 1: Create Student Database
# **Create the Initial Attendance Database​**

# - Create a dictionary to store the names of students and their attendance records.​
# - Initialize a dictionary where each key is a student’s name, and the value is a list of booleans representing attendance ​
# - (True for present, False for absent).​
# - This dictionary will serve as the database for all subsequent tasks.

attendance = {    
    "Alice": [True],
    "Bob": [False],
    "Charlie": [True],
    "Darius": [True],
    "Emma": [False],
    "Faith": [True],
    "Gabriel": [False],
    "Isabella": [True],
    "John": [False],
}


## Task 2: Take Student Attendance
# **Take Attendance​**

# Create a function called take_attendance()​

# Params:​
# - dictionary containing the student name and previous attendance​

# Function purpose:​
# - Loop through all the students, and ask if the student present or absence, and update the attendance accordingly.​
# - You must validate the input.​

# Return:​
# - updated dictionary with attendance record

def takeAttendance(attendance):
    for student in attendance:
        attendanceChecker = input(f"Is {student} present? Y/N ").lower().strip()
        while True:
            if attendanceChecker == "y":
                attendance[student].append(True)
                break

            if attendanceChecker == "n":
                attendance[student].append(False)
                break

            if attendanceChecker != "n" and attendanceChecker != "y":
                attendanceChecker = input(f"Is {student} present? Y/N ").lower().strip()
                print("Please type your answer properly.")
                continue

    return attendance


## Task 3: Calculate Attendance Percentage
# **Create a function called attendance_percentage()​**

# Params:​
# - student: String – containing the student name​
# - attendance_dict: Dictionary – containing the class names and attendance​

# Function purpose:​
# - Lookup the student in the dictionary.​
# - Calculate the percentage of True values.​
# - Return the percentage of True values​

# Return:​
# - attendance_percentage: Float – containing the attendance percentage.

def attendancePercentage(name, attendanceDictionary):
    attendance = attendanceDictionary[name]
    sumPresent = 0
    for status in attendance:
        if status:
            sumPresent += 1

    return sumPresent / len(attendance)
