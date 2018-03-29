# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file =argv

print "Copying from %s to %s" % (from_file,to_file)

# we coulud do these two on one line,how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()


'''
附加題
02

from sys import argv
from os.path import exists

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())

# we coulud do these two on one line,how?
# 打開文件，然後讀取文件的內容，這是兩個事情，兩個步驟
# 文件和文件的內容是兩個不同的對象，python 在定義它們的時候，用到了不同的方法
# in_file = open(from_file)
# indata = in_file.read()
#  打開文件，設作 “寫入” 狀態
# out_file = open(to_file, 'w')
# 將被拷貝的文件的內容寫到新文件當中
# out_file.write(open(from_file).read())

# 關閉文件，兩個都要
# out_file.close()
# open(from_file).close()
# in_file.close()


04.output.close(),關閉文件是爲了回收資源
'''
