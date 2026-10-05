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
# numbers = dict(key1=1, key2=2, key3=3)
# print(numbers)
# print()
#
#    - return the numbers squared
# numbers_squared = {key: value**2 for key, value in numbers.items()}
# print(numbers_squared)
#       - - returns {'key1': 1, 'key2': 4, 'key3': 9}
# ----------------------------------------------------
#
# another example : create a dictionary from a list with comprehension
# ---------------------------------------------------------------------
# new_diction = {num: num**2 for num in [1, 2, 3, 4, 5]}
# print(new_diction)
#
# returns: {
#      1: 1,
#      2: 4,
#      3: 9,#
#      4: 16,
#      5: 25
# }
#
#      - the first num: - assigns each number in the list as a key
#      - the num ** 2 - squares each number in the list and assigns it to the value of each key
# ---------------------------------------------------------------------


# Another Example:
# create a dictionary using two strings with string1 becoming the keys and string2 becoming the values
#
# str1 = "ABC"
# str2 = "123"
#
# diction_combined = {str1[i]: str2[i] for i in range(0, len(str1))}
# print(diction_combined)
#
# returns {
#   'A': 1,
#   'B': 2,
#   'C': 3
# }
#
# - we're running a for loop from 0 to the length of str1 (3)
# - at each iteration,
#       we're assigning the current str1[i] as the key,
#       and str2[i] as the value
# ---------------------------------------------------------------------


# Using Conditional Logic with Dictionary Comprehension
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

# Example:
# num_list = [1, 2, 3, 4, 5]

# add the numbers in the list to a dictionary and define if they are an even or an odd number
#
# output = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
# print(output)
#
# - we're just running a for loop to iterate through num_list
#   - each num in the list becomes the key
#   - depending on the outcome of the logic test, the value becomes either "odd" or "even"
# ---------------------------------------------------------------------


# Practice Exercises#
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# Combine two list's into a dictionary with:
#
#   - list1 providing the key,
#   - list2 providing the value
# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]
#
# print({list1[i]: list2[i] for i in range(0, len(list1))})
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# Given a variable:
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# Create a dictionary called answer , that makes each first item in each list a key and the second item a corresponding value.
# answer = {thing[0]: thing[1] for thing in person}
#
# or
#
# answer = {k: v for k, v in person}
#
# or
#
# answer = dict(person)
# print(answer)
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# Create a dictionary with the key as a vowel in the alphabet and the value as 0.
# Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.
#
# answer = {k: 0 for k in "aeiou"}
#
# or
#
# answer = dict.fromkeys("aeiou", 0)
# print(answer)
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# Python has a function called chr() that will return a string if you
#   provide the corresponding integer ASCII code.
#
# Create dictionary that maps ASCII keys to their corresponding letters.
#   - Use a dictionary comprehension and chr().
#   - Save the result to the answer variable.
#   - You only need to care about capital letters (65-90).
#
answer = {k: chr(k) for k in range(65, 91)}
print(answer)
