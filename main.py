# Number guessing game

# The computer will generate a number
import random

computer_guess = random.randint(0, 1000000)
# The human will gues a number
human_guess = input("Please enter a number: ")
# Cast the human input to a number 
human_guess = int(human_guess)
# Check if the human guessed the correct number

while computer_guess != human_guess: 
  if computer_guess == human_guess:
  # If he/she did, print a congratz message
    print("Congratz! You did it! Your prize is... pineapples and a virtual hug")
  else: 
   # If the number guess was lower than the computer 
    if human_guess < computer_guess:
      print("your number was too low, lol, guess again")

   # If the number guess was hugher than the computer 
    if human_guess > computer_guess: 
      print("your number was too high, XD, try again")

  human_guess =input("please enter a number: ")
  human_guess =int(human_guess)






