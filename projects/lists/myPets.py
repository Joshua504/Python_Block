
myPets = ['hulk', 'billy', 'steve', 'red']
name = input('Enter your pets name: ')
if name not in myPets:
    print('Your pets name is not in our database')
else:
    print('Pet name found: ' + name)