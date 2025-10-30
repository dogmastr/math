"""

    Author: @dogmastr
    Description: Implementation of the Sieve Of Erathosthenes for generating primes.

"""

def sieve_of_erathosthenes(n):

    # Initialize a boolean list marking all numbers from 0 to n as prime.
    # We'll later mark non-primes as False.
    is_prime = [True] * (n + 1)

    # By definition, 0 and 1 are not prime.
    is_prime[0] = is_prime[1] = False

    # Once you pass √n, the pairs of factors just repeat, so it is sufficient to sieve till this upper bound.
    for i in range(2, int(n ** 0.5) + 1):
        # Stop redundant checking.
        if is_prime[i]:
            # Mark all multiples of i starting from i^2 as non-prime.
            # Any smaller multiple of i like 2i, 3i, ..., (i-1)i would have already been marked as non-prime when sieving numbers < i.
            # Starting from i^2 begins at the first multiple of i that has not been previously handled by smaller primes.
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # We finally return all integers in the rage marked as a prime in a set for easy lookup.
    return set(i for i in range(2, n+1) if is_prime[i])

"""

    Example Usage

"""

# Prints all primes up to 10000.
print(sieve_of_erathosthenes(10000))