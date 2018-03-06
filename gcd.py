# Rita Raher 06-03-2018
# Greatest common divisor
def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

print("GCD of 6 and 15", gcd(6, 15))

print("GCD of 56 and 1544", gcd(56, 1544))

z = gcd(221, 323)
print("GCD of 56 and 1544", z)