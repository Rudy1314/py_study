#!/usr/bin/python3
# !/usr/bin/env python3
# if False:
#     print("true")
# else:
#     print("false")
#     print("i am null")
# test 1 2017-8-31
item_one = 1
item_two = 2
item_three = 3

total = item_one + \
        item_two + \
        item_three
print(total)

print(u"this is an unicode string")

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以用多行组成
"""


# test 2
# input("\n\n按下 enter 键后退出")
# import sys;x='runoob';sys.stdout.write(x+'\n')


# if expression:
#     suite
# elif expression:
#     suite
# else:
#     suite

# x="a"
# y="b"
# # 换行输出
# print( x )
# print( y )
#
# print('---------')
# # 不换行输出
# print( x, end=" " )
# print( y, end=" " )
# print()

# import sys
# print('================Python import mode==========================');
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)
#

# from sys import argv, path  # 导入特定的成员
#
# print('================python from import===================================')
# print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

def example(anything):
    '''形参为任意类型的对象，
       这个示例函数会将其原样返回。
    '''
    return anything


tt = example('hello world')
# print(tt)

# counter =100
# miles =1000.0
# name ="runoob"
# print(counter)
# print(miles)
# print(name)
# a,b,c,d=20,5.5,True,4+3j
# print(type(a),type(b),type(c),type(d))
# isInt = isinstance(a,int)
# print(isInt)

# str = "hello world"
# print(str)
# print(str[0:-1])
# print(str*2)

# print(r'ru\test')
