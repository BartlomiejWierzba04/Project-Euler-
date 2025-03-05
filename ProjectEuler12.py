##ProjectEuler12
## What is the first triangle number to have over 500 divisors? 

## First generate nth triangle number 
## prime factor it 
## prime factoring gives you the number of divisors
import numpy as np
from sympy import factorint

def prime_factors_sympy(n):
    factors = factorint(n)  # Returns a dictionary of prime factors and their exponents
    return [p for p, exp in factors.items() for _ in range(exp)]

def number_of_divisors_from_factors(factors):
    # Count the exponents of each prime factor
    exponent_counts = {}
    for p in factors:
        exponent_counts[p] = exponent_counts.get(p, 0) + 1

    # Calculate the number of divisors
    divisors = 1
    for exp in exponent_counts.values():
        divisors *= (exp + 1)

    return divisors

# Example usage
factors = [2, 2, 2, 7]  # Prime factors of 56
print(f"Number of divisors: {number_of_divisors_from_factors(factors)}")


def nth_triangle_number(n):
    return  int((n*(n+1))/2)


for x in range(0,500000): ##irrelevant how large this number is 
    z = nth_triangle_number(x)
    factors = prime_factors_sympy(z)
    numberOfDivisors = number_of_divisors_from_factors(factors)
    if numberOfDivisors>500: 
        print(z)
        break 

