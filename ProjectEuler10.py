## Project Euler 10
## Find the sum of the primes below 2 million 

def primes(n):
    """Returns a list of primes < n."""
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            # Update the sieve using slicing
            sieve[i*i::2*i] = [False] * ((n - i*i - 1) // (2*i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

print(sum(primes(2000000)))
#142913828922