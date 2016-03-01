#!/usr/bin/python

"""
Basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:

-View the calendar
-Add an event to the calendar
-Update an existing event
-Delete an existing event
-The program should behave in the following way:

Print a welcome message to the user
Prompt the user to view, add, update, or delete an event on the calendar
Depending on the user's input: view, add, update, or delete an event on the calendar
The program should never terminate unless the user decides to exit
"""

from time import sleep,strftime

FIRST_NAME = "Zheka"

calendar = {}

def welcome():
    print "Hello " + FIRST_NAME + "\nCalendar is opening...\n"
    sleep(1)
    print "Today is: " + strftime("%A, %d-%b-%Y") + "\nCurrent time: " + strftime("%H:%M:%S")
    print "\nWhat would you like to do?\n"

def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input("Please enter one of the follwoing choices: (A)Add, (U)Update, (V)View, (D)Delete or (X)Exit: ").upper()
        if user_choice == 'V':
            if len(calendar.keys()) < 1:
                print "Calendar is empty"
            else:
                print calendar
        elif user_choice == 'U':
            date = raw_input("What date? ")
            update = raw_input("Enter the update: ")
            calendar[date] = update
            print "\n" + date + " has been updated\n"
            print calendar
        elif user_choice == 'A':
            event = raw_input("Enter event: ")
            date = raw_input("Enter date in format MM/DD/YYYY: ")
            if len(date) != 10 or str(date[6:10]) < strftime("%Y"):
                print "Date format is wrong or date is in the past. Please re-enter"
            else:
                calendar[date] = event
                print "\nEvent has been successfully addedd on " + date
                print "\n", calendar, "\n"
        elif user_choice == 'D':
            if len(calendar.keys()) <= 1:
                print "There is nothing to delete. Calendar is empty"
            else:
                event = raw_input("What event? ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del(calendar[date])
                        print "Record has been succesfully deleted.\n"
                        print calendar
                    else:
                        print "No such event"
        elif user_choice == 'X':
            print "Exiting..."
            sleep(1)
            start = False
        else:
            print "Wrong option has been entered. Exiting..."
            start = False
            
start_calendar()