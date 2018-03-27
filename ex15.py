# -*- coding: utf-8 -*-

# open file and read the content of the file
#improt argv
from sys import argv
#argv
script, filename = argv
#open file
txt = open(filename)
#print filename
print "Here's you file %r:" % filename
# read the contents of the file and print it out on the console
print txt.read()
txt.close()


print "Type the filename again:"
# input the file name
file_again = raw_input("-> ")
# open file
txt_again = open(file_again)
# read the contents of the file and print it out on the console
print txt_again.read()
txt_again.close()
