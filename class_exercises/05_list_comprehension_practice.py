# Clear Screen
import subprocess
import os

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# Class Practice Problems


# Print first letter of each name in the list
# -------------------------------------------------------
# answer = [char[0] for char in ["Elie", "Tim", "Matt"]]
# print(answer)


# Print all even numbers in the list
# -------------------------------------------------------
# answer2 = [x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]
# print(answer2)


# Print all the numbers that are in both list's
# -------------------------------------------------------
# answer = [item for item in [1, 2, 3, 4, ] if item in [3, 4, 5, 6]]
# print(answer)


# Reverse the list and lowercase the letters
# -------------------------------------------------------
# answer2 = [name[::-1].lower() for name in ["Ellie", "Tim", "Matt"]]
# print(answer2)


# Print the numbers between 1 and 100 that are divisible by 12
# -------------------------------------------------------
# answer = [num for num in range(1, 101) if num % 12 == 0]
# print(answer)


# Remove all the vowels from the string
# This methods returns a list
# -------------------------------------------------------
answer = [letter for letter in "amazing" if letter not in "aeiou"]
print(answer)

# This method returns a string
answer2 = "".join(letter for letter in "amazing" if letter not in "aeiou")
print(answer2)
