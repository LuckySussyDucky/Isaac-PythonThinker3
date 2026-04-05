import os
import string

filepath = os.getcwd()
fullpath = os.path.join(filepath, "CT08_09/encrypted_note.txt")

filepath2 = os.getcwd()
fullpath2 = os.path.join(filepath, "CT08_09/hidden_message.txt")
# # Lesson 9 - Message in a Message

# ## Task 1: Open and read the file
# **Open and read the content of a mysterious file called encrypted_note.txt.​**

# A file named encrypted_note.txt has been discovered, and its contents appear cryptic.​

# Write a program to open this file in read mode and display its content.​

# If the file is missing, display an error message:​
# - "ERROR: The encrypted note has vanished. Is someone trying to hide the truth?"

if os.path.exists(fullpath):
    with open(fullpath, "r") as file:
        print(file.read())
else:
    print("ERROR: The encrypted note has vanished. Is someone trying to hide the truth?")


# ## Task 2: Extract Meaningful Data
# **Preprocess the passage by removing all punctuation and converting it to lowercase.​**

# Read the content of encrypted_note.txt.​

# Write a program to:​
# - Remove all punctuation ​(., ,, !, ?, etc.).​
# - Convert all text to lowercase for uniformity.​

# Display the cleaned passage on the console.

with open(fullpath, "r") as file:
        print(file.read().lower())

with open(fullpath, "r") as file:
    files = file.read().lower()

clear_text = files
for p in string.punctuation:
    clear_text = clear_text.replace(p, " ")
print(clear_text)

words = clear_text.lower().split()

# ## Task 3: Decode the message!
# **Decode the Secret Using a Hidden Pattern​**

# Use the cleaned passage from the previous step.​
# ​
# Display the decoded secret message on the console.
letters = []

for word in words:
    letters.append(word[0])
sentence = " ".join(letters)
print(sentence)


# ## Task 4: Protect the Secret
# **Save the decoded message to a secure file, hidden_message.txt.​**

# Create a new file, hidden_message.txt.​
# ​
# After decoding the secret message, write its reverse into the file instead of the plain message.​
# ​
# Write the decoded message into this file.

reversed_sentence = sentence[::-1]
print(reversed_sentence)