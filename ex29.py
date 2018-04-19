# -*- coding: utf-8 -*-

people = 32
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."


if people==dogs:
	print "People are dogs."


'''
1. What do you think the if does to the code under it?
2. Why does the code under the if need to be indented four spaces?
3. What happens if it isn’t indented?
4. Can you put other boolean expressions from Exercise 27 in the if- statement? Try it.
5. What happens if you change the initial variables for people, cats, and dogs?
'''

