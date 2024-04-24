# How to check even or odd by user input?
def oddOrEven(number):
    if ( (number % 2) == 0 ):
        print('The number is even')
    else:
        print('The number is odd')


numEnter = 5
numArray = [0] * numEnter

for index in range(numEnter):
    numArray[index] = int(input('Enter an integer number: '))
    oddOrEven(numArray[index])









