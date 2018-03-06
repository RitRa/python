# Rita Raher 26-02-18
# formatting data
# https://docs.python.org/3/tutorial/inputoutput.html

for i in range(1, 11):
    #use .format()   
    print('{:2d} {:3d} {:4d} {:5d}'.format(i, i**2, i**3, i**4))
  

# f string
a = 5 
print(f'The value of a is {a} and a+1 is {a+1}')

for i in range(1, 11):
    print(f'{i} {i**2} {i**3} {i**4}')