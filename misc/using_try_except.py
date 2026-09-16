###################################################
# temp practice exercises for csteele Python class
###################################################

import os

os.system("cls")


# To trap an input and ensure it is an integer between 1 and 10, use a loop with a try/except block to convert the input to an integer and check the range.

# Trapping Input in Python

# To ensure that user input is an integer between 1 and 10, you can use a loop combined with a try/except block. This method allows you to handle invalid inputs gracefully.

# Steps to Implement Input Trapping

#     1) Use a Loop: This will keep asking the user for input until a valid integer is provided.
#      2)Try/Except Block: This will attempt to convert the input to an integer and catch any errors if the conversion fails.


# Example Code
# Here’s a simple example of how to implement this:


while True:
    user_input = input("Please enter an integer between 1 and 10: ")
    try:
        value = int(user_input)  # Attempt to convert input to an integer
        if 1 <= value <= 10:  # Check if the value is within the range
            print("Valid input:", value)
            break  # Exit the loop if input is valid
        else:
            print("Error: The number must be between 1 and 10.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")


# Explanation of the Code

#     Input Prompt: The user is prompted to enter a number.
#     Conversion Attempt: The int() function tries to convert the input to an integer.
#     Range Check: The code checks if the integer is between 1 and 10.
#     Error Handling: If the input is not an integer, a ValueError is raised, and an error message is displayed.

# This approach ensures that the program only accepts valid integers within the specified range, providing a user-friendly experience.


print("\n\n-- End of Line --\n")
