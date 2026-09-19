# Clear Screen
import subprocess
import os
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# Create a list called instructors
instructors = []

# Add the following strings to the instructors list
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(['Colt', 'Blue','Lisa'])
print(instructors)

# Remove the last value in the list
instructors.pop()
print(instructors)

# Remove the first value in the list
instructors.pop(0)
print(instructors)

# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')

# Run the tests to make sure you've done this correctly!
print(instructors)