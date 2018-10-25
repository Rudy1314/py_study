#!/usr/bin/env python3
# coding=utf-8

# classmates = ['tom', 'how']
# classmates.append('Adam')
# print(classmates)
# print(len(classmates))
# print(classmates[-1])
#
# age = 21
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')
# print('-------------------------------------------')
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)


def test_1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        print('大于0')
    else:
        print('小于0')

test_1(12)
