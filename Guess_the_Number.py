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

from math import nextafter
import random

# Assign a random number to mystery_number

mystery_number = random.randint(0,10)

print ("This is a game to guess a random number between 0 and 10")
print (mystery_number)

guess = int(input("What is your first guess?"))
print ("You guessed ",guess)

# Logic to determine if guess is greater than, less than or equal to mystery_number

if guess == mystery_number:
   print ("Congratualtions, you guessed it!")
elif guess > mystery_number:
    print ("That's too big, try again")
elif guess < mystery_number:
    print ("That's too big, try again")

next_guess = int(input("What is your next guess?"))
print ("You guessed ",next_guess)

#blah blah blah