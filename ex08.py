# -*- coding: utf-8 -*-
#格式化字符串， '%r'显示的是变量的“原始”的数据值，%r在打印的时候能够重现它所代表的对象
formatter = "%r %r %r %r"
#采用 '%s'，可以打印出汉字（中文），或者其他非ASCII字符
formatter2 = "%s %s %s %s "
#打印，传递的参数个数多了或者少了，程序都会报错误
print formatter % (1,2,3,4)
print formatter2 % ("一","二","三","四")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goognight."
	)
