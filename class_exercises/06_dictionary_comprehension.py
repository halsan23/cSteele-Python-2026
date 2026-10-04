# Clear Screen
import subprocess
import os

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# DICTIONARY COMPREHENSION
# Just like List Comprehension, Dictionary Comprehension expands on
# the For/In loop to search through a list for a specific criteria

# ---------------------------------------------------------------------
#
# a basic for loop, print the numbers 1 to 10:
#
# for num in range(1, 11):
#     print(num)
#
# ---------------------------------------------------------------------


# Dictionary Comprehension condenses the for/in code to run in one line
# ---------------------------------------------------------------------
#
# Basic Dictionary Comprehension Syntax:
#    variable_x = {key for key, value in dictionary}
#
# Example:
# ---------------------------------------------------------------------
# numbers = dict(key1 = 1, key2 = 2, key3 = 3)
#
#    - return the numbers squared
#    numbers_squared = {key: value ** 2 for key, value in numbers.items()}
#       - - returns {'key1': 1, 'key2': 4, 'key3': 9}
# ----------------------------------------------------
