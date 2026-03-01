# Predefined data
answerKey = ["A", "B", "B", "D"]  # Correct answers for the quiz
studentAnswers = {
    "john": ["A", "C", "B", "D"],
    "jane": ["A", "B", "B", "D"],
    "alice": ["A", "C", "C", "D"],
    "bob": ["A", "B", "B", "D"]
}

# ## Task 1: Grade all Students
# **Grade all the student’s answers by answer key.​**

# You will be provided ​
# - A list containing answer keys​
# - A dictionary containing students and their answers.​

# Create a function called “grade_all_students()”​

# Purpose: Compare each student's answers with the answer key and calculate their score.​

# Params:​
# - student_answers (dictionary)​
# - answer_key (list)​

# Return:​
# - quiz_scores (dictionary)



def gradeScore(studentAnswer, correctAnswer):
    quizScore = {}
    
    for student, answer in studentAnswer.items():
        sumScore = 0
        for i in range(len(correctAnswer)):
            if answer[i] == correctAnswer[i]:
                sumScore += 1
        quizScore[student] = sumScore * (100 / len(correctAnswer))
    return quizScore


# ## Task 2: Calculate Class Average
# **Calculate the average score of the class.​**

# Create a function called “calculate_average_score()”​

# Purpose: Calculate the average score of the class​

# Params:​
# - quiz_scores(dictionary)​
# - Containing the student name and score for each student​

# Return:​
# - average_score (float) - Float representing the class average score.

quizScore = gradeScore(studentAnswers, answerKey)
def averageScore(quizScore):
    sum = 0
    average = 0
    for _, value in quizScore.items():
        sum = sum + value
    average = sum / len(quizScore)
    return average

# print(f"The class average score is {averageScore(quizScore)}%")


# ## Task 3: Find the Highest Scorer
# **Find the Highest Scorer​**

# Create a function called “find_highest_scorer()”​

# Purpose: Identify the student(s) with the highest score.​

# Params:​
# - quiz_scores(dictionary)​
# - Containing the student name and score for each student​

# Return:​
# - highest_scorers(list) - List of student names with the highest score​
# - List because there could be more than 1 student with the highest score.

def highestScore(quizScore):
    highestScorers = []
    maxScore = 0
    for _, value in quizScore.items():
        if maxScore < value:
            maxScore = value
    for name, value in quizScore.items():
        if maxScore == value:
            highestScorers.append(name)
    return highestScorers

# print(highestScore(quizScore))


# ## Task 4: Display all results
# **Display Class Results​**

# Create a function called “display_results()”​

# Purpose: Print all students and their respective scores.​

# Params:​
# - quiz_scores(dictionary)​
# - Containing the student name and score for each student​

# Return:​
# - None: results are printed to the console.

def displayResults(quizScore):
    for name, value in quizScore.items():
        print(f"{name.title()}: {value}%")

# displayResults(quizScore)


# ## Task 5: Build an interactive menu
# **Build an interactive menu for all the different functions​**

# Create a function called “menu_system()”​

# Purpose: Handle the main menu system, allowing access to the different functions.

# Params:​
# - None: This program starts the program.​

# Return:​
# - None: results are printed to the console.

def menu():
    while True:
        print(" ")
        print("Welcome to the School Grading System (SGS)")
        print(" ")
        print("What would you like to do:")
        print("1: Grade Scores")
        print("2: Calculate Class Average")
        print("3: Notify Highest Scorer(s)")
        print("4: View All Grades")
        print("5: Exit Program")
        print(" ")

        counter = input("Please key in (1, 2, 3, 4 or 5): ").strip()
        while counter != "1" and counter != "2" and counter != "3" and counter != "4" and counter != "5":
            print("Please only enter 1 - 5")
            counter = input("Please key in (1, 2, 3, 4 or 5): ").strip()

        
        if counter == "1":
            gradeScore(studentAnswers, answerKey)
            print("All students have been graded")
        elif counter == "2":
            print(f"The class average score is {averageScore(quizScore)}%")
        elif counter == "3":
            print(highestScore(quizScore))
        elif counter == "4":
            print("This is the results:")
            displayResults(quizScore)
        else:
            break
menu()