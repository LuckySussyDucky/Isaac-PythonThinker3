import random
import os
import string
import turtle

"""
============================================================
Q2. Review Text Analysis
============================================================
You are given a text file containing customer reviews.
The program must analyse the reviews and generate a rating.

Program Requirements:
- Read the contents of the file "reviews.txt"
- Count the total number of characters in the file
- Count how many reviews contain "good"
- Count how many reviews contain "bad"
- Calculate the percentage of good reviews
- Determine the overall rating:
    70% and above → Positive
    40% to 69% → Mixed
    Below 40% → Negative
- Save the results into "review_results.txt" and also print the results to the console

Note:
- The counting must be case-insensitive
- The percentage must be rounded to 2 decimal places
- If there are no valid reviews, the percentage should be 0

Print and save the result in this format:
    Review Text Analysis
    ------------------------------
    Total Characters: <number>
    Good Reviews: <number>
    Bad Reviews: <number>
    Percentage of Good Reviews: <value>%
    Overall Rating: <rating>

============================================================
"""

# ============================================================
# Step 1: Read file contents
# ============================================================

filepath = os.getcwd()
review_fullpath = os.path.join(filepath, "CT08_EndSem/review.txt")

# ============================================================
# Step 2: Count characters and good or bad reviews
# ============================================================

character_counter = 0
good_counter = 0
bad_counter = 0
line = 0

with open(review_fullpath, "r") as file:
    for lines in file:
        if "good" in lines.lower().strip():
            good_counter += 1
        if "bad" in lines.lower().strip():
             bad_counter += 1
        line += 1
        for char in lines:
            character_counter += 1

# ============================================================
# Step 3: Calculate percentage and rating
# ============================================================

rating = ""

good_percentage = (good_counter / int(line)) * 100

if good_percentage > 70:
    rating = "Positive"
elif good_percentage > 40:
    rating = "Mixed"
else:
    rating = "Negative"

# ============================================================
# Step 4: Write results to file
# ============================================================

results_fullpath = os.path.join(filepath, "CT08_EndSem/results.txt")

with open(results_fullpath, "w") as file:
    file.write(f'''
Review Text Analysis
------------------------------
Total Characters: {character_counter}
Good Reviews: {good_counter}
Bad Reviews: {bad_counter}
Percentage of Good Reviews: {good_percentage}%
Overall Rating: {rating}
''')

# ============================================================
# Step 5: Print results to console
# ============================================================

print(f'''
Review Text Analysis
------------------------------
Total Characters: {character_counter}
Good Reviews: {good_counter}
Bad Reviews: {bad_counter}
Percentage of Good Reviews: {good_percentage}%
Overall Rating: {rating}
''')
