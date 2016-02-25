#!/usr/bin/python

"""
The program does the following:

-Prompt the user to select either Rock, Paper, or Scissors
-Instruct the computer to randomly select either Rock, Paper, or Scissors
-Compare the user's choice and the computer's choice
-Determine a winner (the user or the computer)
-Inform the user who the winner is
"""

from random import randint 
from time import sleep 

options = ["R", "P", "S"]

LOST_MESSAGE = "You lost!"
WIN_MESSAGE = "You win!"

def decide_winner(user_choice,computer_choice):
    print "User's choice: ", user_choice
    print "Computer selecting..."
    sleep(1)
    print "Computer's choice: ",computer_choice
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice == computer_choice:
        print "It's a tie"
    elif user_choice_index == 0 and  computer_choice_index == 2:
        print WIN_MESSAGE
    elif  user_choice_index == 1 and  computer_choice_index == 0:
        print WIN_MESSAGE
    elif  user_choice_index == 2 and  computer_choice_index == 1:
        print WIN_MESSAGE
    elif user_choice_index > 2:
        print "Unaaceptable option"
        return
    else:
        print LOST_MESSAGE
    
def play_RPS():
    print "This is Rock, Papaer and Scissors game. Have fun!"
    user_choice = raw_input("Please enter R for Rock, P for Paper, or S for Scissors: ").upper()
    if user_choice != 'R' and user_choice != 'P' and user_choice != 'S':
        print "Please re-enter you choice. Correct choices are R for Rock, P for Paper, or S for Scissors"
        return
    sleep(1)
    computer_choice = options[randint(0,len(options)-1)]
    decide_winner(user_choice,computer_choice)

play_RPS()    

