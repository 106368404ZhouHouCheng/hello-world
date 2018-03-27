# -*- coding: utf-8 -*-


from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


'''
#study drill 02
from sys import argv

script,name,age = argv

print "What's your name?", name
print "How old are you?", age


from sys import argv
height,weight,eye_colour,hair_colour = argv

print "How tall are you?", height
print "How many are you heavy?",weight
print "What's the colour of your eyes?",eye_colour
print "What's the colour of you hair?", hair_colour


#study drill
from sys import argv

script, name, age = argv 

height = raw_input("How tall are you?")
weight = raw_input("How much is your weight?")

print "So, Hello,%s, %s old, %s tall, %s weight" % (name,age,height,weight)
'''