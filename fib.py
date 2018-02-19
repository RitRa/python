# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 19
ans = fib(x)
print("Fibonacci number", x, "is", ans)

#r = 18
#a = 1
#n = 19 


