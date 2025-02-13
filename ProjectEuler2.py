## Project Euler Problem 2
## By considering the terms in the Fibonacci sequence
# whose values do not exceed four million,
# find the sum of the even-valued terms.


def solution():
    values = [1,2]
    sumfib = 2
    while True:
        nextval = values[0] + values[1]
        if nextval>4000000:
            break
        if nextval%2 ==0:
            sumfib+=nextval
        values[0] = values[1]
        values[1] = nextval
        
    return sumfib

print(solution())
# solution is 4613732
        

