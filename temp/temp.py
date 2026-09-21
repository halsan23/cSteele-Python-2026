# Clear Screen
import subprocess
import os

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# Class Practice Problems


# answer = [char[0] for char in ["Elie", "Tim", "Matt"]]
# print(answer)

# answer2 = [x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]
# print(answer2)


# answer = [item for item in [1, 2, 3, 4, ] if item in [3, 4, 5, 6]]
# print(answer)

# answer2 = [name[::-1].lower() for name in ["Ellie", "Tim", "Matt"]]
# print(answer2)
