# comparision operators
print("comparision operators")
print(42 == 42)
print(42 == 99)
print(2 != 3)
print(2 != 2)
print()
print(42 < 100)
print(42 > 100)
print(42 < 42)
eggCount = 42
print(eggCount <= 42)
myAge = 23
print(myAge >= 10)
print()

#binary boolean operators
print("binary boolean operators")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()
print(not True)
print(not False)
print(not not not not False)
print(not not not not True)
print()

# mixing Boolean and comparision operators
print("mixing Boolean and comparision operators")
print((4 < 5) and (5 < 6))
print((4 < 5) and (9 < 6))
print((1 == 5) and (2 == 2))
print()

# elements of flow control
print('elements of flow control')
name = 'Mary'
passWord = 1234
if name == 'Mary':
    print('Hello Mary')
    if passWord == 1234:
        print('Access granted')
    else:
        print('Wrong password')
print()
if name == 'obi':
    print('hi obi')
elif passWord == 1234:
    print('access granted')