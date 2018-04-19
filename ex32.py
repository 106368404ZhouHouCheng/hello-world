# -*- coding: utf-8 -*-

hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weight = [1,2,3,4]

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# this fruit kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(6):
	print "Adding %d to tht list" % i
	# append is function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Elements %d" % i

my_list = range(6)
print my_list

'''
1. Take a look at how you used range. Look up the range function to understand it.
2. Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6)
directly to elements?
3. Find the Python documentation on lists and read about them. What other operations
can you do to lists besides append?

1. The range function can create a integer list, and which be used in for-loop usually.
2. ok
'''