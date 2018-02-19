# Rita Raher 19-02-18
# Lists
# A list is an ordered collection of items. For example, the list [1,2,3] is a list where the second item is 2.

# sums the numbers fro 1 to 100

i = 0
sum = 0

while (i <= 100):
    # sum adds i 
    sum = sum + i
    # increase to stop the loop
    i = i + 1

print("The sum of numbers of 1 to 100: ", sum)



#     
# sums the numbers fro 1 to 100 only even numbers
i = 0
sum = 0

while (i <= 100):
    # if it is even. You can divide by 2 and there is no remainder
    if i % 2 == 0:
        # sum adds i
        sum = sum + i
    # increase to stop the loop
    i = i + 1

print("The sum of even numbers of 1 to 100: ", sum)

# A different way to do it    
# sums the numbers fro 1 to 100 only even numbers
i = 0
sum = 0

while (i <= 100):
    sum = sum + i
    # increase to stop the loop i = i + 2
    i += 2

print("The sum of even numbers of 1 to 100: ", sum)
   