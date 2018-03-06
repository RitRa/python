# Rita Raher 06-03-2018
# functions
def sumall(upto):
    sumupto = 0 
    for i in range(1, upto + 1):
        sumupto = sumupto + i
    return(sumupto)

print("The sum of the values from 1 to 50 inclusive is: ", sumall(50))
print("The sum of the values from 1 to 5 inclusive is: ", sumall(5))
print("The sum of the values from 1 to 10 inclusive is: ", sumall(10))


