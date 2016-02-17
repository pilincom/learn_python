#!/usr/bin/python

"""
Python is especially useful for doing math and can be used to automate many calculations. 
In this project, you'll create a calculator than can compute the area of a given shape, 
as selected by the user. The calculator will be able to determine the area of the following shapes:

Circle
Triangle

The program should do the following:

-Prompt the user to select a shape
-Depending on the shape the user selects, calculate the area of that shape
-Print the area of that shape to the user
"""
#imports value of pi
from math import pi
#Imports sleep function
from time import sleep
#Imports date and time
from datetime import datetime

#Prints time in format MM/DD/YYYY HH:MM
now = datetime.now()
print '%s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute)

hint = "Dont' forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle:").upper()

if option == "C":
    radius = float(raw_input("Please enter radius of the circle: "))
    area = pi * (radius ** 2)
    print "The pie is baking..."
    sleep(1)
    print ("Circle area is: %.2f. \n%s" % (area, hint))
elif option == "T":
    base = float(raw_input("Please enter triangle's base: "))
    height = float(raw_input("Please enter triangle's height: "))
    area = (base * height) / 2
    print "Uni Bi Tri..."
    sleep(1)
    print ("Triangle area is: %.2f. \n%s" % (area, hint))
else:
    print "Options are only T - for triangle or C - for circle. Please re-enter..."