# -*- coding: utf-8 -*-

'''
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );
print str.split(' ');
'''

def break_words(stuff):
	"""This function will break up words for us.q"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Print the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Print the last word after popping if off."""
	word = words.pop(-1)
	print word

def sort_sentence(words):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(words)
	return sorted(words)

def print_first_and_last(sentence):
	"""Print the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


# str = "Line2-abc Line1-abcdef Line4-abcd";

# print break_words(str)
# print sort_words(str)

# print_first_word(break_words(str))
# print_last_word(break_words(str))

# print sort_sentence(str)

# print_first_and_last(str)