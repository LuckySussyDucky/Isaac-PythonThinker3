"""
============================================================
Q2. Scrabble Game
============================================================
Write a PYTHON function that calculates the points
of a given word using a dictionary.

Requirements:
- Use a Python Dictionary for the letter points
- Ask for 5 words
- For each word, calculate the total score
- Print the score for each word in this format:
  Word #1:
  Score #1:

============================================================
"""

# ============================================================
# Step 1: Create the dictionary
# ============================================================

letters = {
    "A": [1],
    "B": [3],
    "C": [3],
    "D": [2],
    "E": [1],
    "F": [4],
    "G": [2],
    "H": [4],
    "I": [1],
    "J": [8],
    "K": [5],
    "L": [1],
    "M": [3],
    "N": [1],
    "O": [1],
    "P": [3],
    "Q": [10],
    "R": [1],
    "S": [1],
    "T": [1],
    "U": [1],
    "V": [4],
    "W": [4],
    "X": [8],
    "Y": [4],
    "Z": [10]
}

# ============================================================
# Step 2: Create a function calculate_score
# ============================================================
# - Loop through each letter in the word
# - Use the dictionary to find its value
# - Add up the total
# - Return the total score
# ============================================================

def calculate_score(word, letters):
    score = 0
    return score

# ============================================================
# Step 3: Ask for 5 words
# ============================================================

for i in range(1, 5, 1):
    word = input("Type out a word: ")
    score = calculate_score(word, letters)

# ============================================================
# Step 4: Print the score for each word in this format:
#         Word #1:
#         Score #1:
# ============================================================

    print("Word #" + i + ":" + word)
    print("Score #" + i + ":" + score)



















# ( - 0 - )