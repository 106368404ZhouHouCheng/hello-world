# -*- coding: utf-8 -*-

# put the formatted variable 'x' in the string,and then a % character,followed by the variable x
x = "There are %d types of people." %10
# put the variable 'binary' in the string
binary = "binary"
# put the variable 'do_not' in the string
do_not = "don't"
# put the formatted variable 's' in the string,and then a % character,followed by the variable s
y = "Those who know %s and those who %s." %(binary,do_not)
#print x,y
print x
print y

#print 
# %r 
print "I said: %r." %x
print "I also said: '%s'." %y
# put the variable 'hiarious' in the bool
hilarious = False
# put the variable 'joke_evaluation' in the string,and then prints
joke_evaluation = "Isn't that joke so funny! %r"
# print the variable 'joke_evaluation' in the string,followed by the variable 'hilarious'
print joke_evaluation % hilarious
# put the variables 'w' and 'e' in the string  
w = "This is the left side of..."
e = "a string with a right side."
# print the variable 'w' in the string,followed by the variable 'e'
print w+e

print w*2