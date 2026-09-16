###################################################
# Nesting While and For Loops
# using emoji \U0001f600
# badDoggy | 9/11/26
###################################################

import os

os.system("cls")


for num in range(1, 11):
    print("\U0001f600" * num)
print()


times = 10
while times > 0:
    print("\U0001f600" * times)
    times -= 1
print()


spc = 9
smiley = 1
for num in range(1, 11):
    print(" " * spc + "\U0001f600" * num)
    spc -= 1

print()


print("\n\n-- End of Line --\n")
