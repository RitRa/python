# Rita Raher 18-02-2018
# Project Euler
# Problem 3: Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# https://projecteuler.net/problem=3
# prime factors of a positive integer are the prime numbers that divide that integer exactly

# using SymPy
# SymPy is a Python library for symbolic mathematics
# Ref: http://docs.sympy.org/latest/modules/ntheory.html

from sympy import primefactors

# prime factors for 13195
print(primefactors(13195))

# prime factors for 600851475143
print(primefactors(600851475143))


def prime_factors(n):
    #create an empty list to hold the factors
    factors = []
    # start with 2
    i = 2
    # check the number is greater than 1 to continue
    while n > 1:
        # while the number divided i with no remainder
        while n % i == 0:
            # add the number to the list
            factors.append(i)
            # number = number / factor
            n = n / i  
        #increase i 
        i += 1
    #return list
    return factors

print(prime_factors(13195))



