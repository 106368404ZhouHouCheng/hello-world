# -*- coding: utf-8 -*-
'''
my_name = 'Zed A. shaw'
my_age = 35 # not a lie
my_height = 74 #inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teech = 'While'
my_hair = 'Brown'

print "Let's talk about %s." %my_name
print "He's %d inches tall." %my_height
print "He's %d pound heavy." %my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes,my_hair)
print "His teech are usually %s depending on the office." %my_teech

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(my_age,my_height,my_weight,my_age+my_height+my_weight)
'''

#介紹Zed A. shaw 的身高，體重，眼睛，牙齒和頭發的顏色
#ex study Drills 01,02

name = 'Zed A. shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 # lbs
eyes = 'Blue'
teech = 'While'
hair = 'Brown'

#inches_transform_cm = 2.54
height = height * 2.54

#lbs_transform_kg = 0.4536
weight = weight * 0.4536



print "Let's talk about %s." %name
print "He's %d centimetres tall." %height
print "He's %d kilograms heavy." %weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes,hair)
print "His teech are usually %s depending on the office." %teech

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age,height,weight,age+height+weight)

world = "J"
print "Hello %c" %world


print "%+8x" % 10
print "%08d" % 5
print "%10.6f" % 2.5
