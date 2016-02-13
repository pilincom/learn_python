#!/usr/bin/python


#Pyg game
"""
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print "Empty input or non-alpha characters. Please re-enter."
"""
    

###############
###Functions###
###############

#Plan your trip
"""
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost
    
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days) + spending_money
    
print  trip_cost("Los Angeles",5,600)
"""

###########
###Lists###
###########
"""
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

#Add to the list:
backpack.append('konserva')

#Replace element at second index
backpack[2] = 'mattress'

#Remove specific item from the list:
backpack.remove('xylophone')

#Remove element at 3-rd index
backpack.pop(3)

#Remove element at 3-rd index without printing at console
del(backpack[3])

#Sort list
backpack.sort()

#Slicing
#From start of the list to index 2, but not including index 2 
first = backpack[:2]
#The following will print indexes 1 and 2
middle = backpack[1:3]

print first + middle

#Prints everything starting at index 2 inclusive to index 9 exclusive with interval 2
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print list[2:9:2]


#List comprehensions
#Builds a list that include the squares of the even numbers between 1 to 11
even_squares = [x ** 2 for x in range(1,12) if x % 2 == 0]
print even_squares    

#Builds a list that consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.
cubes_by_four = [x ** 3 for x in range(1,11) if (x ** 3) % 4 == 0]
print cubes_by_four

#Prints a list in areverse order (note negative stride)
list = [1,2,3,4,5]
print list[::-1]    
"""

##################
###Dictionaries###
##################
"""
inventory = {
    'Sloth' : 105,
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Prints Puffin's room number
print inventory['gold'] 

#Add a new key:
inventory['Horek'] = 108
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

#Remove entry
del inventory['Sloth']

#Add/remove entry to a list in the dictionary:
inventory['pouch'].remove('twine')
inventory['pouch'].append('kamupo')

#Print all keys
for key in inventory
    print key

#Print all definitions
for key in inventory:
    print inventory[key]
"""

###########
###Stock###
###########
"""
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}

stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

print "What we have in stock:"

for key in prices:
    print ""
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]


#Calculates sum of the whole inventory    
total_stock = 0
for key in prices:
    
    total_stock += prices[key] * stock[key]
print ""
print "What we worth: %s" % total_stock

#Stocking out
shopping_list = ["banana", "orange", "apple"]
print ""
print "Here is what in your shopping cart: %s" % shopping_list

def compute_bill(food):             #Defines checkout function
    total = 0                       #Initial total equals 0
    for item in food:               
        if stock[item] > 0:         #If item is is in stock,
            total += prices[item]   #add price to total
            stock[item] -= 1        #Substract one from the stock dictionary
    return total
    
print ""
print "Here is your total: %s" % compute_bill(shopping_list)

print ""
print "Our updated inventory:"

for key in prices:
    print ""
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
"""


#####################################
###Challenge: Grades for the class###
#####################################
"""
#List (dictionaries) of students and their grades
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

#List of students in the class
students = [lloyd, alice,tyler]

#Calculate average
def average(numbers):
    total = float(sum(numbers)) / len(numbers)
    return total
    
#Calculates weighted average
#homework weighs 10%, quizzes weigh 30% and tests weigh 60%     
def get_average(student):
    homework = average(student["homework"]) * 0.1
    quizzes = average(student["quizzes"]) * 0.3
    tests = average(student["tests"]) * 0.6
    total = homework + quizzes + tests
    return total

#Converts score to a letter grade    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#Calculates average score for the class
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
    
print ""

#Prints weighted average scores and grades for each student in he class
for student in students:
    print "%s's weighted average score is: %s and grade is: %s" % \
    (student["name"], get_average(student), get_letter_grade(get_average(student)))

print ""

#Prints to the console weighted average score and grade for the class
print "Class's average score is %s and grade is %s" \
% (get_class_average(students), get_letter_grade(get_class_average(students)))
print ""       
"""            

###########
###Loops###
###########
"""
#zip creates pairs of elements when passed two lists, and will stop at the end of the shorter list
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    print "This is form list a: %s" % a
    print "This is form list b: %s" % b
"""

#####################
###GAME BATTLESHIP###
#####################
"""
from random import randint

board = []

#Create 10x10 board
for x in range(10):
    board.append(["O"] * 10)
#Print board (lists) without quotes
def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print ""
print_board(board)

#Takes random integer in range from 1 to 10 and assigns to variables for row and column
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)

#Start of debugging
print ""
message = "This part is for debugging only. It tells you location of the ship upfront"
print "#" * len(message)
print message
print "This is random row: %s" % ship_row
print "This is random column: %s" % ship_col
print "#" * len(message)
print ""
#End of debugging

#'For loop' will iterate through the whole process 5 times
for turn in range(5):
    print "Turn", turn + 1
    
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
            
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col] = "*"
        print_board(board) 
        break
    else:
        if guess_row not in range(10) or guess_col not in range(10):
            print "Oops, that's not even in the ocean. Grid size is 10 x 10."
            print "Try again:"
        elif (board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
    if turn == 4:
            print "Game over"
"""

##############
###PRACTICE###
##############

#Sum of digits
"""
def digit_sum(n):
    total = 0
    for i in str(n):
        total += int(i)
    print total
digit_sum(125)   
"""
#Factorial
"""
def factorial(x):
    total = 1
    list = []
    list.append(x)
    while x > 1:
        x -= 1
        list.append(x)
    for i in list:
        total *= i
    print total 

factorial(4) 
"""

#Prints reversed string
"""
def reverse(text):
    list = []
    for letter in text:
        list.append(letter)
    reverse_list = []
    x = len(text)
    while x != 0:
        x -= 1
        reverse_list.append(list[x])
    print "".join(reverse_list)
   
reverse("Python!")
"""

#Removes vowels from the string
"""
def anti_vowel(text):
    list = []
    for letter in text:
        if letter not in "aeiouAEIOU":
            list.append(letter)
    print ''.join(list)
    
anti_vowel("hello world")
"""

#Game "Scrabble"
#Each letter worth a certain amount of points. 
#The following sums points for the entered word(string)
"""
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         

def scrabble_score(word):
    total = 0
    word = word.lower()
    for i in word:
        total += score[i]
    print total
    

scrabble_score("AbgdtyDWKJHdhsjauhd")
"""

#Censor. Takes two arguments: sentence and word (both strings). 
#If word is found in sentence - replaces it with "*".
"""
def censor(text,word):
    stars = "*" * len(word)
    list = []
    for i in text.split():
        if i == word:
            list.append(stars)
        else:
            list.append(i)
    print " ".join(list)
    
censor('this is test','is')
"""    

#Count. Takes two arguments: list if numbers and a single digit.
#Counts how many times digit appears in the list.
"""
def count(sequence,number):
    match = 0
    for num in sequence:
        if num == number:
            match += 1
    print match
    
count([1,2,31,1,2,31,1],1)
""" 

#Remove all odd numbers i a provided list of numbers
"""
def purify(numbers):
    list = []
    for num in numbers:
        if num % 2 == 0:
            list.append(num)
    print list
    
purify([1,2,3,4,5])
"""

#Returns product of numbers supplied in a list
"""
def product(numbers):
    total = 1
    for num in numbers:
        total *= num
    print total
    
product([4, 5, 5])
"""
#Removes duplicate numbers for a supplied list
"""
def remove_duplicates(numbers):
    list = []
    for num in numbers:
        if num not in list:
            list.append(num)
    print list

remove_duplicates([1,1,1,2,3,3,3,2,2,3,1])    
"""

#Prints median numbers from a supplied sequence

"""
def median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        print float((numbers[(len(numbers) / 2)] + numbers[(len(numbers) / 2) - 1])) / 2
    else:
        print numbers[len(numbers) / 2]
        
median([6,5,4,3,2,1])
"""        

######################
####Exam statistics###
######################

"""
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#Prints all grades
def print_grades(grades):
    for grade in grades:
        print grade

#Returns sum of the grades
def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total

#Returns average grade
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

#Returns variance (how grades varied against the average)
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    result = variance / len(scores)
    return result

#Returns standard deviation (square root of variance)
def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)

print "Grades", print_grades(grades)
print "Sum of grades:", grades_sum(grades)
print "Average grade:", grades_average(grades)
print "Variance:", grades_variance(grades)
print "Standard deviation:", grades_std_deviation(variance)
"""

############
###Lambda###
############ 
#Quick anonymous function that doesn't require a definition
"""
#Filters list languages to display only 'Python'
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == 'Python', languages)

#Creates list of squares of numbers from 1 to 10 and 
#prints only squares between 30 and 70
squares = [i ** 2 for i in range(1,11)] 
print filter(lambda x: x >= 30 and x <= 70, squares)
"""


    
    
    
    
    
    
    









