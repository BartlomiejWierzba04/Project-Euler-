## Project Euler Problem 5

##2520 is the smallest number divisible by each of the numbers from 1-10 without remainder

## what is the smallest possible number that is evenly divisible by all of the numbers 1-20 

## 20 - 2^2 x 5
## 19 - prime - needed
## 18 - 2x9
## 17 - prime - needed
## 16 - 2^4
## 15 - 3x5
## 14 - 2x7
## 13 - prime - needed
## 12 - 2^2 x 3
## 11 - prime - needed
## 10 - 2x5
## 9 - 3^2
## 8 - 2^3
## 7 - prime - needed
## 6 - 2x3
## 5 - prime - needed
## 4 - 2^2
## 3 - 3 - prime - needed
## 2 - prime - needed
## 1 - not prime, not needed? ;)

## largest fac of 2 = 2^4
## largest fac of 3 = 3^2
## largest fac of 5 = 5
## largest fac of 7 = 7
## largest fac of 11 = 11
## largest fac of 13 = 13
## largest fac of 17 = 17 , also 19 = 19


## this would be unwise for larger numbers lol - just thought it would be fun.
def solution():
    num = 19*17*13*11*7*5*16*9
    print (str(num))


solution() #232792560
# bingo

