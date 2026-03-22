import os

filepath = os.getcwd()
fullpath = os.path.join(filepath, "CT08_08/sherlock.txt")

# ## Task 1: Open and read the file
# **Write a program that opens sherlock.txt and displays its content.​**

# Open sherlock.txt in read mode.​
# - Read the entire file content using .read().​
# - Print the content to the console.

# If the file does not exist, display an error message.

if os.path.exists(fullpath):
    with open(fullpath, "r") as file:
        print(file.read())
else:
    print("Error message. File does not exist.")


# ## Task 2: Count All Characters in the File
# **Write a program to count the total number of characters in the file, including spaces and punctuation.​**

# Open and read the file as before.​

# Use Python’s len() function to count the total number of characters in the file.​

# Print the total character count.

totalCharacters = 0
with open(fullpath, "r") as file:
    counter = 1
    for lines in file:
        for words in lines:
            counter += 1
    print(f"This text has {counter} characters.")
totalCharacters = counter


# ## Task 3: Identify Vowels and Count Them
# **Write a program to count how many vowels are in the file​**

# Define a set of vowels: {'a', 'e', 'i', 'o', 'u'} (case-insensitive).​

# Loop through each character in the file and check if it’s a vowel.​
# - Use a dictionary to store the count of each vowel (e.g., {'a': 500, 'e': 800}).

# Display the total vowel count.

def identifyLetters(vowel):
    with open(fullpath, "r") as file:
        counter = 0
        for lines in file:
            for words in lines:
                if words.lower() == vowel.lower():
                    counter += 1
    print(f"This text has {counter} of the letter {vowel}")
    return counter

totalLetters = 0

print(" ")

totalLetters += identifyLetters("a")

totalLetters += identifyLetters("e")

totalLetters += identifyLetters("i")

totalLetters += identifyLetters("o")

totalLetters += identifyLetters("u")

print(" ")

# ## Task 4: Find the Percentage of Vowels
# **Calculate the percentage of vowels relative to the total number of characters in the file.​**

# Use the total vowel count and the total character count from previous tasks.​

# Calculate the percentage using the formula: ​
# - (total vowels / total characters) * 100.​

# Display the percentage with 2 decimal places.

print(f"The percentage of vowels is {(totalLetters / totalCharacters) * 100}%")

print(" ")


# ## Task 5: Output the results into a file
# **Save the vowel counts to a new file named vowel_counts.txt.​**

# Open a new file vowel_counts.txt in write mode.​

# Write the following into the file in a clear format:​
# - counts for each vowel​
# - the percentage of vowels ​
# ​
# Confirm the file has been created successfully.

fullpath2 = os.path.join(filepath, "CT08_08/vowel_count.txt")

with open(fullpath2, "w") as file:
    file.write(f"""
This text has {identifyLetters("a")} of the letter a
This text has {identifyLetters("e")} of the letter e
This text has {identifyLetters("i")} of the letter i
This text has {identifyLetters("o")} of the letter o
This text has {identifyLetters("u")} of the letter u
The percentage of vowels is {(totalLetters / totalCharacters) * 100}%
""")
    
    print("Successfully saved values")