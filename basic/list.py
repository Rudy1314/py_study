# list = ['abcd', 786, 2.23, 'hello', 70.6]
# tynylist = [123, 'world']
# print(list)
# print(list[0])
# print(list[1:3])
# print(list + tynylist)
#
# tuple = (1, 2, 3, 'a', 'b', 'c');
# 'aaa'
#
# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
# if ('Rose' in student):
#     print('Rose 在集合中')
# else:
#     print('Rose 不在集合中')
#
# if ('ax' in tuple):
#     print('a 在集合中')
# else:
#     print('a 不在集合中')
'''
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
'''

# print(a)
#
# print(a - b)  # a和b的差集
#
# print(a | b)  # a和b的并集
#
# print(a & b)  # a和b的交集
#
# print(a ^ b)  # a和b中不同时存在的元素

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
