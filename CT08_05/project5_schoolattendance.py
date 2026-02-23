# Lesson 5 - School Attendance System (SAS)

## Task 1: Create Student Database
# **Create the Initial Attendance Database​**

# - Create a dictionary to store the names of students and their attendance records.​
# - Initialize a dictionary where each key is a student’s name, and the value is a list of booleans representing attendance ​
# - (True for present, False for absent).​
# - This dictionary will serve as the database for all subsequent tasks.

attendance = {    
    "alice": [True, False, True],
    "bob": [False, False, True],
    "charlie": [True, True, True],
    "darius": [True, False, False],
    "emma": [False, True, False],
    "faith": [True, True, True],
    "gabriel": [False, False, True],
    "isabella": [True, False, True],
    "john": [False, True, False],
}

counter = 0
random = 0
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
# takeAttendance(attendance)

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

    return sumPresent / len(attendance) * 100

# print(attendancePercentage("Alice", attendance))

# ## Task 4: Notify low attendance
# **Identify students with attendance below a defined threshold and notify them.​**

# Function : notify_low_attendance()​

# Params:​
# - attendance_dict (dictionary): Attendance database with student names as keys and attendance records as values.​
# - threshold (float): Minimum attendance percentage required.​

# Return:​
# - low_attendance_students(list): A list of student names with attendance below the threshold

def lowAttendence(attendanceDictionary, threshold):
    lowAttendenceStudent = [

]
    for name in attendanceDictionary:
        attendancePercentageStudent = attendancePercentage(name, attendanceDictionary)
        if attendancePercentageStudent < threshold:
            lowAttendenceStudent.append(name)
    return lowAttendenceStudent

# print(lowAttendence(attendance, 50))


# ## Task 5: Create the Menu System
# **Build an interactive menu to access the attendance system's features.**​

# Display a menu with the following options:​
# - 1: Take Attendance​
# - 2: Calculate Attendance Percentage for a Student​
# - 3: Notify Low Attendance​
# - 4: Exit Program​

# Based on the user’s choice:​
# - Call the respective function with the necessary inputs.​
# - Display the results of the chosen action


def menu():
    counter2 = 0
    counter3 = 0
    counter4 = 0
    print(" ")
    print("Welcome to the School Attendance System (SAS)")
    print(" ")
    print("What would you like to do:")
    print("1: Take Attendance")
    print("2: Calculate Attendance Percentage for a Student")
    print("3: Notify Low Attendance")
    print("4: Exit Program")
    print(" ")
    counter = input("Please key in (1, 2, 3, 4): ").strip()
    while counter2 == 0:
        while counter != "1" and counter != "2" and counter != "3" and counter != "4":
            print("Please only enter 1 - 4")
            counter = input("Please key in (1, 2, 3, 4): ").strip()

        while counter3 == 0:
            if counter == "1":
                takeAttendance(attendance)
                counter3 = 1
                counter2 = 1
            elif counter == "2":
                while counter4 == 0:
                    student = input("Please key in your student name: ").lower().strip()
                    if student not in attendance:
                        print(" ")
                        print("Please type a name from the class")
                    elif student in attendance:
                        print(f"The percentage is {attendancePercentage(student, attendance)}%")
                        counter3 = 1
                    else:
                        random = 1 
                    counter4 = 1   
            elif counter == "3":
                print(lowAttendence(attendance, 50)) 
                counter = 0
            else:
                counter2 = 1
            break
menu()