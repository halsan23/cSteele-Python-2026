# Clear Screen
import subprocess
import os
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)




# Define your code below:
instructors = []
instructors.extend(['Colt', 'Blue', 'Lisa'])
for name in instructors:
    print(name)

instructors.clear()
print(instructors)