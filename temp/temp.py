##################################
# Rock - Paper - Scissors
# Created by - badDoggy - | 09/26
##################################

# Imports
import subprocess
import os
from random import randint

# Clear Screen
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

# set variables
user_score = 0
comp_score = 0
tie_score = 0
win_score = 3
turn = 1

# Random Computer selection
rand_num = randint(0,2)
if rand_num == 0:
	comp = "rock"
elif rand_num == 1:
	comp = "paper"
else:
	comp = "scissors"

# Play the Game
while user_score < win_score or comp_score < win_score:
   # Title Bar
   print(f'User Score: {user_score} | Computer Score: {comp_score}\n\n')
   print('- Rock - Paper - Scissors -')
   print('- Player vs Computer -')
   print('- Best 3 out of 5 -\n')
   print(f'Round # {turn}\n')
   # User Input
   # Computer choice display
   user = input('Input Your Choice: ').lower()

   # option for user to end game early
   if user.lower() == 'q' or user.lower() == 'quit':
      print('\n- User Quit -')
      break
   # invalid input check
   elif user.lower() != 'rock' and user.lower() != 'paper' and user.lower() != 'scissors':
      print('-- Invalid Input --')
      print("Please enter Rock, Paper, Scissors, or Quit!\n")
      # input('\n- press any key to continue -')
      # # Clear Screen for next round
      # subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

   else:
      print(f'Computer Choice: - {comp.capitalize()} -\n')

      # if a tie
      if user == comp:
         print(f'This round is a tie:')
         tie_score += 1
         turn += 1
         print(f'\nCurrent score: {user_score} to {comp_score}.')
         input('\n- press any key to continue -')
         # Clear Screen for next round
         subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

      # test for win and display results
      elif user == 'rock' and comp == 'scissors':
            print(f'You win this round: - Rock smashes Scissors')
            user_score += 1
            turn += 1
            print(f'\nCurrent score: {user_score} to {comp_score}.')
            input('\n- press any key to continue -')
            # Clear Screen for next round
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
      elif user == 'paper' and comp == 'rock':
            print(f'You win this round: - Paper covers Rock')
            user_score += 1
            turn += 1
            print(f'\nCurrent score: {user_score} to {comp_score}.')
            input('\n- press any key to continue -')
            # Clear Screen for next round
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
      elif user == 'scissors' and comp == 'paper':
            print(f'You win this round: - Scissors cut Paper')
            user_score += 1
            turn += 1
            print(f'\nCurrent score: {user_score} to {comp_score}.')
            input('\n- press any key to continue -')
            # Clear Screen for next round
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

      elif comp == 'rock' and user == 'scissors':
            print(f'Computer wins this round: - Rock smashes Scissors')
            comp_score += 1
            turn += 1
            print(f'\nCurrent score: {user_score} to {comp_score}.')
            input('\n- press any key to continue -')
            # Clear Screen for next round
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
      elif comp == 'paper' and user == 'rock':
            print(f'Computer wins this round: - Paper covers Rock')
            comp_score += 1
            turn += 1
            print(f'\nCurrent score: {user_score} to {comp_score}.')
            input('\n- press any key to continue -')
            # Clear Screen for next round
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
      elif comp == 'scissors' and user == 'paper':
            print(f'Computer wins this round: - Scissors cut Paper')
            comp_score += 1
            turn += 1
            print(f'\nCurrent score: {user_score} to {comp_score}.')
            input('\n- press any key to continue -')
            # Clear Screen for next round
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)


print('- Game Over -')
if user_score == comp_score:
   print(f'\nGames ends in a TIE after {turn} rounds: {comp_score} to {user_score}.')
elif comp_score > user_score:
   print(f'\nComputer wins after {turn} rounds {comp_score} to {user_score}.')
else:
   print(f'\nPlayer wins after {turn} rounds {user_score} to {comp_score}.')
print('\nThanks for playing ...')
print('\n\n-- End of Line --\n')