# Qns: Student Results File Processing

# You are given a text file called results.txt.
# Each line contains a student's name and mark, separated by a space.

# Example:
# Alex 92
# Ben 43
# Clara 78

# Your task:

# 1. Read the data from results.txt.

student_results = {

}

student_ranges = {

}

import os

filepath = os.getcwd()
fullpath = os.path.join(filepath, "CT08_12/results.txt")

with open(fullpath, "r") as file:


# 2. Convert the data into a dictionary called student_results.
#    The name should be the key.
#    The mark should be the value.

    for line in file:
        name = ""
        mark = ""
        name = []
        mark = []
        for letter in line:
            if letter.isalpha():
                name.append(letter)
            elif letter.isdigit():
                mark.append(letter)

        student_name = "".join(name)
        student_mark = "".join(mark)
        student_results[student_name] = student_mark
# can use line.split() next time


# 3. With the dictionary, create another dictionary that count the student in the follow range:
# 0 - 50, 51 - 70, 71 - 90, 91 - 100

        if int(student_mark) <= 50:
            if "<50" not in student_ranges:
                student_ranges["<50"] = [student_name]
            else:
                student_ranges["<50"].append(student_name)
        elif int(student_mark) <= 70:
            if "<70" not in student_ranges:
                student_ranges["<70"] = [student_name]
            else:
                student_ranges["<70"].append(student_name)
        elif int(student_mark) <= 90:
            if "<90" not in student_ranges:
                student_ranges["<90"] = [student_name]
            else:
                student_ranges["<90"].append(student_name)
        else:
            if "<100" not in student_ranges:
                student_ranges["<100"] = [student_name]
            else:
                student_ranges["<100"].append(student_name)


# 4. Do a analysis of the score to get the following and print it to a output txt file 
# Min score: 
# Max Score:

# No of people in each range
# 0 - 50:  people
# 51 - 70: people
# 71 - 90: people
# 91 - 100: people

# the mode for range: __________
# average score:

print(f"The number of students scoring between 0 - 50 is {len(student_ranges["<50"])}")
print(f"The number of students scoring between 51 - 70 is {len(student_ranges["<70"])}")
print(f"The number of students scoring between 71 - 90 is {len(student_ranges["<90"])}")
print(f"The number of students scoring between 91 - 100 is {len(student_ranges["<100"])}")

