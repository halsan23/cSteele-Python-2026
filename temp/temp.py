###################################################
# temp practice exercises for csteele Python class
###################################################

import os
os.system('cls')

from random import randint  # use randint(a, b) to generate a random number between a and b

number = randint(1,10)
i = 0  # i should be incremented by one each iteration

while number != 5:
   i += 1
   # print(f'Run number is: {i}')
   # print(f'Random Number is: {number}\n')
   number = randint(1,10)

print('Random number generation between 1 and 10.\n')
print(f'took {i + 1} runs to generate a random number of 5.')


print('\n\n-- End of Line --\n')