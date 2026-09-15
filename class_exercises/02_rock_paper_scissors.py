######################################
# Rock - Paper - Scissors
# Created by - badDoggy - | 09/15/26
######################################

# Imports
import subprocess
import os
from random import randint


# set variables
computer_choices = ['rock', 'paper', 'scissors']
user_score = 0
comp_score = 0
tie_score = 0
win_score = 3
turn = 1

# Random Computer selection
rand_num = randint(0,2)
comp = computer_choices[rand_num]


# function to test for win
def win_check(user, comp):
   # if a tie
   if user == comp:
      winner = None
      win_text = 'This round is a tie:'
      return winner, win_text

   # user win scenarios
   elif user == 'rock' and comp == 'scissors':
      winner = 'user'
      win_text = 'You win this round: - Rock smashes Scissors'
      return winner, win_text
   elif user == 'paper' and comp == 'rock':
      winner = 'user'
      win_text = 'You win this round: - Paper covers Rock'
      return winner, win_text
   elif user == 'scissors' and comp == 'paper':
      winner = 'user'
      win_text = 'You win this round: - Scissors cut Paper'
      return winner, win_text

   # computer win scenarios
   elif comp == 'rock' and user == 'scissors':
      winner = 'computer'
      win_text = 'Computer wins this round: - Rock smashes Scissors'
      return winner, win_text
   elif comp == 'paper' and user == 'rock':
      winner = 'computer'
      win_text = 'Computer wins this round: - Paper covers Rock'
      return winner, win_text
   else:
      comp == 'scissors' and user == 'paper'
      winner = 'computer'
      win_text = 'Computer wins this round: - Scissors cut Paper'
      return winner, win_text


# Play the Game
while user_score < win_score and comp_score < win_score:

   # Clear Screen
   subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

   # Title Bar
   print(f'Winning Score: {win_score} | User Score: {user_score} | Computer Score: {comp_score} | Tie Games: {tie_score}\n\n')
   print('- Rock - Paper - Scissors -')
   print('- Player vs Computer -')
   print('- Best 3 out of 5 -\n')
   print(f'Round # {turn}\n')

   # User Input
   user = input('Enter Your Choice: ').lower()


   # option for user to end game early
   if user.lower() == 'q' or user.lower() == 'quit':
      print('\n- User Quit -')
      break


   # invalid input check
   elif user.lower() != 'rock' and user.lower() != 'paper' and user.lower() != 'scissors':
      print('\n- Invalid Input -\n')
      if user == '':
         print('- Empty User Input -')
      print("- Enter (Q)uit or Rock, Paper, Scissors only! -\n")
      # Pause play so reader can see the error info
      input('- Press any key to continue -')

   # Display computer pick
   else:
      print(f'Computer Choice: - {comp.capitalize()} -\n')


      # No errors - Check for win
      winner, win_text = win_check(user, comp)
      print(win_text)


      # Update Scores and round
      if winner == 'user':
         user_score += 1
      elif winner == 'computer':
         comp_score += 1
      else:
         tie_score += 1
      turn += 1
      # Pause play so reader can see the results of this round
      input('\n- Press any key to continue -')



# Game Over
# Clear Screen
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

# Title Bar
print(f'Winning Score: {win_score} | User Score: {user_score} | Computer Score: {comp_score} | Tie Games: {tie_score}\n\n')
print('- Rock - Paper - Scissors -')
print('- Player vs Computer -')
print('- Best 3 out of 5 -\n')
if user_score > comp_score:
   print(f'\n\nYou Won, {user_score} games to {comp_score}, in {turn} rounds :)')
else:
   print(f'\n\nThe computer wins, {comp_score} games to {user_score}, in {turn} rounds :(')
print('\nThanks for playing ...')
print('\n\n-- End of Line --\n')