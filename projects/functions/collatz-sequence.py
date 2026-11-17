def collatz(number):
    if number % 2 == 0:
        even = number // 2
        print(even)
        return even
    else:
        odd = 3 * number + 1
        print(odd)
        return odd

def reduceNum():
    num = int(input('Enter a digit: '))
    while num != 1:
        num = collatz(num)

reduceNum()