# Clear Screen
import subprocess
import os

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# LIST COMPREHENSION PRACTICE
# List Comprehension expands on the For/In loop
#
# Basic for/in : for x in (list/range/dictionary/tuple, whatever)
#
# List Comprehension condenses the for/in code to run in one line
#
# Basic List comprehension : [x for x in (whatever)]
# the initial variable let's you set conditions for the fo/in loop
# any "logic" processing is added at the end
#
# processing a list [x for x in (whatever)] : returns a list
# processing a string (x for x in (whatever)) : returns a string
# ---------------------------------------------------------------------


# Print first letter of each name in the list
# -------------------------------------------------------
# answer = [char[0] for char in ["Elie", "Tim", "Matt"]]
# print(answer)  # returns ["E", "T", "M"]


# Print all even numbers in the list
# -------------------------------------------------------
# answer2 = [x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]
# print(answer2)  # returns [2,4,6]


# Print all the numbers that are in both list's
# -------------------------------------------------------
# answer = [item for item in [1, 2, 3, 4, ] if item in [3, 4, 5, 6]]
# print(answer)  # returns [3,4]


# Reverse the list and lowercase the letters
# -------------------------------------------------------
# answer2 = [name[::-1].lower() for name in ["Ellie", "Tim", "Matt"]]
# print(answer2)  # returns


# Print the numbers between 1 and 100 that are divisible by 12
# -------------------------------------------------------
# answer = [num for num in range(1, 101) if num % 12 == 0]
# print(answer)  # returns ['eille', 'mit', 'ttam']


# Remove all the vowels from the string
# This methods returns a list
# -------------------------------------------------------
# answer = [letter for letter in "amazing" if letter not in "aeiou"]
# print(answer)  # returns ['m', 'z', 'n', 'g']

# This method returns a string
# answer2 = "".join(letter for letter in "amazing" if letter not in "aeiou")
# print(answer2)  # returns 'mzng'


# Use List Comprehension to create a nested list
# Output should be : [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
# answer = [[list for list in range(0, 3)] for num in range(0, 3)]
# print(answer)


# Use nested list comprehension and range() to accomplish the following
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

answer = [[num for num in range(0, 10)] for val in range(0, 10)]
print(answer)
