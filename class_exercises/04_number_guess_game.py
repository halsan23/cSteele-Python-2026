###########################################################
# Number Guessing Game
# using randint, loops and Try/Except for input validation
# badDoggy | 9/12/26
###########################################################

# Initial Setup
import os
from random import randint
os.system('cls')

#select a random number between 1 and 25
number = randint(1,25)

#Title Bar
print('Can you guess my number between 1 and 25 ...')


# Run the game
while True:
   # input user's guess
   guess = input('\nGuess my number or (Q)uit: ')

   # option for user to end game early
   if guess.lower() == 'q':
      print('\nThanks for playing ...')
      print('\n\n-- End of Line --\n')
      break

   # Try/Except for Input Validation
   try:
      value = int(guess)     # Attempt to convert input to an integer
      if 1 <= value <= 25:   # Check if the value is within the range

         # Input is a Valid Integer between 1 and 25
         # check if guessed number is too high or too low
         if value > number:
               print('Too High, try again:')
         elif value < number:
            print('Too Low, try again:')

         # correct guess - ask to play again
         else:
            print(f'\n\nYou got me - My number was {number}')
            again = input('\nPlay Again (Y/N)? ')

            # end game if user selects not to play again
            if again.lower() == "n":
               print('\nThanks for playing ...')
               print('\n\n-- End of Line --\n')
               break

            # setup to play again
            else:
               os.system('cls')
               number = randint(1,25)
               print('Can you guess my number between 1 and 25 ...')

      # if user inputs an integer outside the range of 1-10
      else:
         print("Invalid input: The number must be between 1 and 25.")

   # if user inputs a non-integer
   except ValueError:
        print("Invalid input: Please enter a number must be between 1 and 25.")