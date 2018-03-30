# -*- coding: utf-8 -*-


# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1,arg2)

# ok,that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1,arg2)

# this just takes one argument 
def print_one(arg1):
	print "arg1: %r" % arg1

# this just takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()



'''
附加题

为自己写一个函数注意事项以供后续参考。你可以写在一个索引卡片上随时阅读，直到你记住所有的要点为止。注意事项如下：

        函数定义是以 def 开始的吗？    #是的
        函数名称是以字符和下划线 _组成的吗？    #是的
        函数名称是不是紧跟着括号 ( ？   #是的
        括号里是否包含参数？多个参数是否以逗号隔开？   #是的，可以
        参数名称是否有重复？（不能使用重复的参数名）  #不能
        紧跟着参数的是不是括号和冒号 ): ？   #是的
        紧跟着函数定义的代码是否使用了 4 个空格的缩进 (indent)？    #是的
        函数结束的位置是否取消了缩进 (“dedent”)？  #是的

当你运行（或者说“使用use”或“调用call”）一个函数时，记得检查下面的点：

        调运函数时是否使用了函数的名称？     #是的
        函数名称是否紧跟着 (？    #是的
        括号后有无参数？多个参数是否以逗号隔开？      #可以有参数，也可以无参数，多个参数以逗号隔开
        函数是否以 ) 结尾？     #是的

按照这两份检查表里的内容检查你的代码，直到你不需要检查表为止。

最后，将下面这句话阅读几遍：

‘运行函数(run)’、‘调用函数(call)’、和‘使用函数(use)’是同一个意思
'''
