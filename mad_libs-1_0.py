#!/usr/bin/python

#Mad libs. There is a story template with blanks which will be filled according to user's input

print "Mab Libs has started!"
print ""
char_name = raw_input("Please enter main character name:")
print ""
print "Now we will need to collect three adjectives..." 
adj1 = raw_input("Enter first adjective:")
adj2 = raw_input("Enter second adjective:")
adj3 = raw_input("Enter third adjective:")
print""
print "Now we will need to collect three verbs..." 
verb1 = raw_input("Enter first verb:")
verb2 = raw_input("Enter second verb:")
verb3 = raw_input("Enter third verb:")
print""
print "Now we will need to collect four nouns..." 
noun1 = raw_input("Enter first noun:")
noun2 = raw_input("Enter second noun:")
noun3 = raw_input("Enter third noun:")
noun4 = raw_input("Enter fourth noun:")
print ""
print "Now it gets really fun.."
print ""
animal = raw_input("Please enter an animal:")
food = raw_input("Please enter a food:")
fruit = raw_input("Please enter a fruit:")
number = raw_input("Please enter a number:")
name = raw_input("Please enter a superhero name:")
country = raw_input("Please enter a country:")
dessert = raw_input("Please enter a dessert:")
year = raw_input("Please enter a year:")
print ""
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. \
On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to \
the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. \
Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. \
%s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (adj1,char_name,verb1,adj2,noun1,noun2,animal,food,verb2,noun3,fruit,adj3,char_name,verb3,number,char_name,name,name,char_name,country,char_name,dessert,char_name,year,noun4)