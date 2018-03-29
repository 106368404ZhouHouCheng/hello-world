# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

# create function print_all
def print_all(f):
	print f.read()
# create function rewind
# seek() 方法用於移動文件讀取指針到指定位置，0表示從文件開頭開始算起
def rewind(f):
	f.seek(0)
# create function print_a_line
def print_a_line(line_count, f):
	print line_count,f.readline(),

# create variable current_file，open the txt file  
current_file = open(input_file)
# print First let's print the whole file:\n
print "First let's print the whole file:\n"
# call function print_all, print the content of the txt file
print_all(current_file)
# print Now let's rewind, kind of like a tape.
print "Now let's rewind, kind of like a tape."
# call function rewind, 將指針移動到文件開頭
rewind(current_file)
# print Let's print three lines:
print "Let's print three lines:"

# create variable current_line, and 
current_line = 1
# call function print_a_line, print the first line of the file's content 
print_a_line(current_line,current_file)
# current_line+1
current_line = current_line+1
# call function print_a_line, print the second line of the file's content 
print_a_line(current_line,current_file)
# current_line+1
current_line=current_line+1
# call function print_a_line, print the third line of the file's content 
print_a_line(current_line,current_file)



'''
附加题
1.通读脚本，在每行之前加上注解，以理解脚本里发生的事情。
2.每次print_a_line运行时，都传递了一个叫current_line的变量。在每次调用函数时，打印出current_line的值，跟踪一下它在print_a_line中是怎样变成line_count的。
3.找出脚本中每一个用到函数的地方。检查def一行，确认参数没有用错。
4.上网研究一下file中的seek函数是做什么用的。试着运行pydoc file看看能不能学到更多。
  seek() 方法用于移动文件读取指针到指定位置。
  語法：fileObject.seek(offset[, whence])
  参数
  offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
  whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
5.研究一下+=这个简写操作符的作用，写一个脚本，把这个操作符用在里边试一下。

current_line += 1

'''

