## Project Euler Problem 4
## "a palindromic number reads the same both ways. The largest palindrome
## made from the product of two 2-digit numbers is 9009 = 91x99

## PROBLEM:

## Find the largest palindrome made from the product of two 3-digit numbers


## the solutions lays nowhere near the bottom so let's start at 999 

def solution():
    palindromes = []
    for x in range(1000,900,-1): #estimating the range to be around 900-999
        for y in range(1000,900,-1):
            if str(x*y) == str(x*y)[::-1]:
                palindromes.append(x*y)##if string of number is reverse number.
    return palindromes

y = solution()
print(y[]) #the solution will be first since we did this from the top.
print("ended")

#solution is 906609

#think what would automatically not make something a palindrome. 
            
