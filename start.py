# def hello(name):
#     print('hello   ' + name)
#
# hello('bob')
import random
from random import randint

from pip._internal.utils import egg_link


def get_answer(num):
    if num == 1:
        return 'heaven'
    elif num == 2:
        return 'up'
    elif num == 3:
        return 'hell'
    elif num == 4:
        return 'down'
    elif num == 5:
        return 'choose'


# r = random.randint(1, 5)
# print(r)
# f = get_answer(r)
# print(f)

print(get_answer(random.randint(1, 5)))

spam = print('hello')
print(None == spam)

print('Hello', end='')
print('World')

print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep=',')

def spam():
    eggs = 1234

spam()
print(eggs)