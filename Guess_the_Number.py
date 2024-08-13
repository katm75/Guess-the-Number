# Guess the Number 

#  Kathryn Marks
#  kathryn.pythonprograms@gmail.com
#  Created April 26, 2024
#  Last modified August 13, 2024



# This is a game to guess a random number from 1 - 10
# Using a RNG pick a number
# Using a loop to decide if the number is too big, too small or the correct one.
# Print a message to the player with the feedback
# Continue until the player guess the correct number

# The random module allows us to generate the mystery number

import random

# Assign a random number to mystery_number

mystery_number = random.randint(0,10)

print ("This is a game to guess a random number between 0 and 10" )
# print (mystery_number)  This is for debugging

guess = int(input("What is your first guess?  "))


# Logic to determine if guess is greater than, less than or equal to mystery_number
# Need to rewrite this into a while look 
# Pseudocode something like
    # While guess != mystery_number
        # Test the guess using if elif else
        # break
                # You don't need to use elif because getting the right answer
                # breaks you out of the while loop.


while guess != mystery_number:
    print ("You guessed",guess)
    if guess < mystery_number:
        print ("That's too small, try again")
    else:
        print ("That's too big, try again")
 
    guess = int(input("What is your next guess? "))

print ("Congratulations, you guessed it!")
       
# Thanks to flabdabbet for helping me understand what I was doing wrong

# EOF