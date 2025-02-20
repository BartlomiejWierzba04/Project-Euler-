import math 
## Project Euler 7

## What is the 10,001st prime?

def find_nth_prime(n):
    if n == 1:
        return 2
    primes = [2]
    candidate = 3
    while len(primes) < n:
        is_prime = True
        sqrt_candidate = math.isqrt(candidate)
        for p in primes:
            if p > sqrt_candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2  # Check next odd number
    return primes[-1]

# Find and print the 10,001st prime
print(find_nth_prime(10001))
