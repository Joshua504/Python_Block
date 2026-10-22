# # comparision operators
# print("comparision operators")
# print(42 == 42)
# print(42 == 99)
# print(2 != 3)
# print(2 != 2)
# print()
# print(42 < 100)
# print(42 > 100)
# print(42 < 42)
# eggCount = 42
# print(eggCount <= 42)
# myAge = 23
# print(myAge >= 10)
# print()
#
# #binary boolean operators
# print("binary boolean operators")
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# print()
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
# print()
# print(not True)
# print(not False)
# print(not not not not False)
# print(not not not not True)
# print()
#
# # mixing Boolean and comparision operators
# print("mixing Boolean and comparision operators")
# print((4 < 5) and (5 < 6))
# print((4 < 5) and (9 < 6))
# print((1 == 5) and (2 == 2))
# print()
#
# # elements of flow control
# print('elements of flow control')
# name = 'Mary'
# passWord = 1234
# if name == 'Mary':
#     print('Hello Mary')
#     if passWord == 1234:
#         print('Access granted')
#     else:
#         print('Wrong password')
# print()
# if name == 'obi':
#     print('hi obi')
# elif passWord == 1234:
#     print('access granted')
# print()
#
# # while statement
# print('while statements')
# spam = 0
# while spam < 2:
#     print('I WILL WIN.')
#     spam = spam + 1
# print()
#
# name = ''
# while name != 'bishop':
#     print('please type your name.')
#     name = input()
#     print('thank you!')
# print()
#
# # break statement
# print('break statement')
# while True:
#     print('Hell YAAA!!!')
#     name = input('enter your name')
#     if name == 'obi':
#         break
#     print('Lets GOOOO!!!')
# print()
import random
from operator import truediv
from random import *

import sys

# continue statement
# print('continue statement')
# while True:
#     print('Who Goes You!!!.')
#     name = input('enter your name')
#     if name != 'obi':
#         continue
#     print('Okay Do You Have a Code?')
#     passCode = input('enter your passCode')
#     if passCode == '1234':
#         break
#     print('Get Out.')
# print('Get In')
# i = 0
# while i < 5:
#     print('Jimmy Five Times (' + str(i) + ')')
#     i = i + 1

# for loops and range function
# print('for loops and range function ')
# for i in range(5):
#     print('jimmy five times (' + str(i) + ')')
# total = 0
# for num in range(101):
#     total = total + num
# print(total)

# for i in range(0, 10):
    # print(i)

# for i in range(0, 10, 2):
#     print(i)

# for i in range(5, -1, -1):
#     print(i)

# importing modules
# print('importing modules')
# for i in range(5):
#     print(randint(1, 10))

# while True:
#     response = input('Type exit to exit.')
#     if response == 'exit':
#         sys.exit()
#     print('you typed' + response + '.')

# while True:
#     spam = input('enter number')
#     if spam == '1':
#         print('hello')
#     elif spam == '2':
#         print('howdy')
#     else:
#         print('greetings!')

# for i in range(1, 11):
#     print(i)
# print()

# count = 1
# while count <= 10:
#     print(count)
#     count = count + 1

# functions
print('functions')
def hello():
    print('howdy')
    print('howdy')
    print('howdy')

hello()