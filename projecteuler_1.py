# Rita Raher 18-02-2018
# Project Euler
# Problem 
# https://projecteuler.net/problem=1

i = 1
sum = 0 

while i < 1000:
    if i % 3 == 0:
        sum = sum + i
    elif i % 5 == 0:
        sum = sum + i
    i = i + 1
print("sum ", sum)

        
