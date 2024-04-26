# Guess the Number 
#  Kathryn Marks
#  kathryn.pythonprograms@gmail.com
#  Created April 26, 2024
#  Last modified April 26, 2024



# This is a game to guess a random number from 1 - 10
# Using a RNG pick a number
# Using a loop to decide if the number is too big, too small or the correct one.
# Print a message to the player with the feedback
# Continue until the player guess the correct number

# The random module allows us to generate the mystery number

import random

# Assign a random number to mystery_number

mystery_number = random.randint(0,10)

print ("This is a game to guess a random number between 0 and 10")

guess = int(input("What is your first guess?"))

print ("You guessed ",guess)
