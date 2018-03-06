# Rita Raher 06-03-2018
# Greatest common divisor
def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

print("GCD of 6 and 15: ", gcd(6, 15))
print("GCD of 56 and 1544: ", gcd(56, 1544))
z = gcd(221, 323)
print("GCD of 56 and 1544: ", z)

#optimising the function using the %
def gcd2(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            # % = remainder
            y = y % x
    if x == 0:
        return y
    else:
        return x
    
print("GCD of 6 and 15: ", gcd2(6, 15))
print("GCD of 56 and 1544: ", gcd2(56, 1544))
z = gcd2(221, 323)
print("GCD of 56 and 1544: ", z)
