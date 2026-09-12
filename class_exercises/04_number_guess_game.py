###################################################
# Number Guess Game
# using randint and loops
#badDoggy | 9/11/26
###################################################

import os
from random import randint
os.system('cls')


#Title Bar
print('Can you guess my number between 1 and 10 ...')

#select a random number between 1 and 10
number = randint(1,10)
# set initial guess to zero
guess = 0


# Run the game
while guess != number:
   # print(f'number is: {number}')  # debug code
   guess = int(input('\nGuess my number: '))

   if guess > number:
      print('Too High, try again:')
      guess = 0

   elif guess < number:
      print('Too Low, try again:')
      guess = 0

   else:
      print(f'\n\nYou got me - My number was {number}')

      again = input('\nPlay Again (Y/N)? ')
      if again.lower() == "n":
         print('\nThanks for playing ...')

      else:
         os.system('cls')
         number = randint(1,10)
         guess = 0
         print('Can you guess my number between 1 and 10 ...')


print('\n\n-- End of Line --\n')