## Project Euler 6


## Find the difference between the square of the sum and sum of squares of the first 100 natural numbers


def SquareOfSum():
    sumOfNum= 0
    for x in range(1,101):
        sumOfNum +=x
    print(sumOfNum)
    return sumOfNum

def SumOfSquares():
    sumOfNum = 0
    for x in range(1,101):
        sumOfNum+= (x**2)
    print(sumOfNum)
        
    return sumOfNum


def solution():
    sumOfSquares = 0
    Sum = 0
    for x in range(1,101):
        sumOfSquares +=(x**2)
        Sum +=x
    return sumOfSquares - (Sum)**2


print(abs(solution()))



