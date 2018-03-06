# Rita Raher 26-02-18
# exercise6 
# Write a Python script containing a function called factorial() 
# that takes a single input/argument which is a positive integer and returns its factorial. 
# The factorial of a number is that number multiplied by all of the positive numbers less than it. 
# For example, the factorial of 5 is 5x4x3x2x1 which equals 120. 
# You should, in your script, test the function by calling it with the values 5, 7, and 10.

def factorial(x):
    result = 1
    for i in range(1, x +1):
        result *= i

    return result

print("Factorial for 5: ", factorial(5))
print("Factorial for 7: ", factorial(7))
print("Factorial for 10: ", factorial(10))
