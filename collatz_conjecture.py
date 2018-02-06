# Collatz conjecture
# The conjecture is that no matter what value of n, the sequence will always reach 1.

#n = 17

#asking the user to pick an interger to test
n = int(input("Pick a number:  "))

while (n > 1):
    #check it is even using the modulus %2
    if(n % 2 == 0): 
        # divide it by 2
        n = (n / 2)
        print(n)
    #else odd: multiple it by 3 and add 1
    else:
        n = (3 * n + 1)
        print(n)
