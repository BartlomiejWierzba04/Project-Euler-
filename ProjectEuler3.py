## Project Euler Problem 3 
## What is the largest prime factor of the number 600851475143


num = 600851475143
def largest_prime_factor(n):
    if n <= 1:
        return None  # Handle cases where input is 1 or less
    
    largest_prime = -1
    
    # Divide out factors of 2
    while n % 2 == 0:
        largest_prime = 2
        n = n // 2
    
    # Check odd numbers starting from 3
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            largest_prime = divisor
            n = n // divisor
        divisor += 2  # Increment by 2 to skip even numbers
    
    # If remaining n is a prime greater than 2
    if n > 2:
        largest_prime = n
    
    return largest_prime

print(largest_prime_factor(num))
#6857
    
    
