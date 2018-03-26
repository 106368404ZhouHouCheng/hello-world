# -*- coding: utf-8 -*-
#python 转义字符

print "I am 6'2\" tall." # \" 双引号
print 'I am 6\'2" tall' # \' 单引号

tabby_cat = "\tI'm tabbed in." #\t tab键
persian_cat = "I'm split \non a line." #\n,换行
backslash_cat = "I'm \\ a \\ cat." #\\,斜杆

#三引号
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
#打印
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#比较 %s ,%r 
print "I said: %s" % tabby_cat
print "I said: %r" % backslash_cat
print "I said: %s" % persian_cat

print "I said: %r" % "I am 6'2\" tall."
print "I said: %s" % 'I am 6\'2" tall'

'''
while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" %i,
'''
