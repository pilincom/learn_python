#!/usr/bin/python

"""
Program that rolls a pair of dice and asks the user to guess a number. \
Based on the user's guess, the program should determine a winner. \
If the user's guess is greater than the total value of the dice roll, \
they win! Otherwise, the computer wins.

The program does the following:

-Randomly roll a pair of dice
-Add the values of the roll
-Ask the user to guess a number
-Compare the user's guess to the total value
-Decide a winner (the user or the program)
-Inform the user who the winner is
"""

from random import randint
from time import sleep

def get_user_guess():
    user_guess = int(raw_input("Your guess: "))
    return user_guess
    
def roll_dice(number_of_sides):
    first_roll = randint(1,number_of_sides)
    second_roll = randint(1,number_of_sides)
    max_val = number_of_sides * 2
    print "Enter your guess. Max Value is:", max_val
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_val:
        print "You guess is greater than maximum possible value."
        return
    else:  
        print "Rolling..."
        sleep(1)
        print "First roll is %d" % first_roll
        sleep(1)
        print "Second roll is %d" % second_roll
        sleep(1)
        total_roll = first_roll + second_roll
        print "Total dice roll: %d" % total_roll
    if user_guess == total_roll:
        print "You guessed correctly and have won!"
        return
    elif user_guess < total_roll:
        print "Your guess is less than dice roll. You lost."
        return
    elif user_guess > total_roll:
        print "Your guess is more than dice roll. You lost."
        return

roll_dice(6)