## Project Euler Problem #1

## Project Euler Problem 1
## Find All the multiples of 3 or 5 under 1000



def solution():
    sumOfMultiples = 0 
    for x in range(0,1000):
        if (x%3==0) or (x%5==0):
            sumOfMultiples+=x

    return sumOfMultiples


x = solution()
print(x)

## Solution is 233168
        
