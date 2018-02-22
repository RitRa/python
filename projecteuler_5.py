# Rita Raher 20-02-2018
# Project Euler
# Problem 5: Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# https://projecteuler.net/problem=5

number = 2520

for i in range(1, 11):
    # use the double // to get rid of the decimal
    print(i, number // i)

a = 1

#for i in newnumber:
#range equals 5
#for i in range(1, 11):
#    if a % i == 0:
#        print(a)
#        a +=1

# Greatest Common Divider  
# https://docs.python.org/3/library/math.html
#   
#import math

import math

number = 1

for factor in range(1, 11):
    number *= factor // math.gcd(number,factor)
print(number)

number = 1

for factor in range(1, 21):
    number *= factor // math.gcd(number,factor)
print(number)
      